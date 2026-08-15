from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class LegacyWorker:
    name: str
    sessions: set[str] = field(default_factory=set)

    def initialize(self, session_id: str) -> None:
        if not session_id:
            raise ValueError("session_id must not be empty")
        self.sessions.add(session_id)

    def call(self, session_id: str) -> bool:
        return session_id in self.sessions


@dataclass(frozen=True)
class StatelessWorker:
    name: str

    def call(self, request: dict[str, Any]) -> bool:
        params = request.get("params")
        if not isinstance(params, dict):
            return False
        meta = params.get("_meta")
        if not isinstance(meta, dict):
            return False
        return (
            request.get("jsonrpc") == "2.0"
            and request.get("method") == "tools/call"
            and meta.get("io.modelcontextprotocol/protocolVersion") == "2026-07-28"
            and isinstance(meta.get("io.modelcontextprotocol/clientInfo"), dict)
            and bool(params.get("name"))
        )


def build_self_describing_request(request_id: int = 1) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "method": "tools/call",
        "params": {
            "name": "search",
            "arguments": {"q": "stateless MCP"},
            "_meta": {
                "io.modelcontextprotocol/protocolVersion": "2026-07-28",
                "io.modelcontextprotocol/clientInfo": {
                    "name": "infobuza-lab",
                    "version": "1.0",
                },
            },
        },
    }
