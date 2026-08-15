from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionRequest:
    runtime: str
    network: bool = False
    write_files: bool = False
    reads_secrets: bool = False
    timeout_seconds: int = 10
    purpose: str = ""


@dataclass(frozen=True)
class Policy:
    runtimes: tuple[str, ...] = ("python3",)
    allow_network: bool = False
    allow_write: bool = False
    max_timeout_seconds: int = 30
    require_purpose: bool = True


@dataclass(frozen=True)
class Decision:
    allowed: bool
    reasons: tuple[str, ...]
    sandbox_profile: dict[str, object]


def evaluate(request: ExecutionRequest, policy: Policy = Policy()) -> Decision:
    reasons=[]
    if request.runtime not in policy.runtimes: reasons.append("runtime_not_allowed")
    if request.network and not policy.allow_network: reasons.append("network_denied_by_default")
    if request.write_files and not policy.allow_write: reasons.append("filesystem_write_denied")
    if request.reads_secrets: reasons.append("secret_access_never_allowed")
    if request.timeout_seconds > policy.max_timeout_seconds: reasons.append("timeout_exceeds_limit")
    if policy.require_purpose and not request.purpose.strip(): reasons.append("purpose_required")
    return Decision(not reasons, tuple(reasons), {
        "network": "allow" if request.network and policy.allow_network else "deny",
        "filesystem": "temporary-write" if request.write_files and policy.allow_write else "read-only",
        "credentials": "isolated",
        "timeout_seconds": min(request.timeout_seconds, policy.max_timeout_seconds),
    })
