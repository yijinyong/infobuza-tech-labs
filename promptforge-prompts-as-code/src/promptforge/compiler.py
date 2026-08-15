from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

INCLUDE = re.compile(r'\{\{\s*include\s+"([^"]+)"\s*\}\}')
VARIABLE = re.compile(r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}")


class CompileError(ValueError):
    pass


@dataclass(frozen=True)
class BuildArtifact:
    content: str
    dependencies: tuple[str, ...]
    sha256: str


class PromptCompiler:
    def __init__(self, source_root: str | Path):
        self.root = Path(source_root).resolve()

    def compile(self, entry: str, variables: dict[str, object]) -> BuildArtifact:
        dependencies: list[str] = []
        rendered = self._render(entry, variables, (), dependencies)
        unresolved = sorted(set(VARIABLE.findall(rendered)))
        if unresolved:
            raise CompileError("undefined variables: " + ", ".join(unresolved))
        content = rendered.strip() + "\n"
        return BuildArtifact(
            content=content,
            dependencies=tuple(dict.fromkeys(dependencies)),
            sha256=hashlib.sha256(content.encode()).hexdigest(),
        )

    def _safe_path(self, relative: str) -> Path:
        target = (self.root / relative).resolve()
        try:
            target.relative_to(self.root)
        except ValueError as exc:
            raise CompileError(f"include escapes source root: {relative}") from exc
        if not target.is_file():
            raise CompileError(f"missing include: {relative}")
        return target

    def _render(self, relative: str, variables: dict[str, object], stack: tuple[str, ...], dependencies: list[str]) -> str:
        if relative in stack:
            raise CompileError("circular include: " + " -> ".join((*stack, relative)))
        path = self._safe_path(relative)
        dependencies.append(relative)
        text = path.read_text(encoding="utf-8")
        text = INCLUDE.sub(
            lambda match: self._render(match.group(1), variables, (*stack, relative), dependencies),
            text,
        )
        return VARIABLE.sub(
            lambda match: str(variables[match.group(1)]) if match.group(1) in variables else match.group(0),
            text,
        )

    @staticmethod
    def verify_golden(artifact: BuildArtifact, golden: str | Path) -> None:
        path = Path(golden)
        if not path.is_file() or path.read_text(encoding="utf-8") != artifact.content:
            raise CompileError("compiled prompt differs from committed golden file")
