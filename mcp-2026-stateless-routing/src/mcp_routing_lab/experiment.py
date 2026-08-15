from __future__ import annotations

from .model import LegacyWorker, StatelessWorker, build_self_describing_request


def run_comparison(requests_per_mode: int = 20) -> dict[str, int | str]:
    if requests_per_mode <= 0:
        raise ValueError("requests_per_mode must be positive")

    legacy_workers = [LegacyWorker("legacy-a"), LegacyWorker("legacy-b")]
    legacy_workers[0].initialize("session-1")
    legacy = [
        legacy_workers[index % len(legacy_workers)].call("session-1")
        for index in range(requests_per_mode)
    ]

    stateless_workers = [StatelessWorker("stateless-a"), StatelessWorker("stateless-b")]
    request = build_self_describing_request()
    stateless = [
        stateless_workers[index % len(stateless_workers)].call(request)
        for index in range(requests_per_mode)
    ]

    return {
        "experiment_kind": "architecture_reproduction_not_conformance_test",
        "requests_per_mode": requests_per_mode,
        "legacy_round_robin_success": sum(legacy),
        "legacy_round_robin_failure": legacy.count(False),
        "stateless_round_robin_success": sum(stateless),
        "stateless_round_robin_failure": stateless.count(False),
    }
