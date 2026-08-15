from pathlib import Path

import pytest

from promptforge import CompileError, PromptCompiler

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("entry,vars_file,expected", [
    ("sre.prompt.md", "sre.json", "checkout-api"),
    ("support.prompt.md", "support.json", "InfoBuza Pro"),
    ("home.prompt.md", "home.json", "4명"),
])
def test_practical_scenarios(entry, vars_file, expected):
    import json
    variables = json.loads((ROOT / "examples" / vars_file).read_text(encoding="utf-8"))
    artifact = PromptCompiler(ROOT / "prompts").compile(entry, variables)
    assert expected in artifact.content
    assert "shared/safety.prompt.md" in artifact.dependencies


def test_missing_variable_fails_before_runtime(tmp_path):
    (tmp_path / "main.md").write_text("Hello {{ missing }}", encoding="utf-8")
    with pytest.raises(CompileError, match="undefined variables"):
        PromptCompiler(tmp_path).compile("main.md", {})


def test_circular_include_is_rejected(tmp_path):
    (tmp_path / "a.md").write_text('{{ include "b.md" }}', encoding="utf-8")
    (tmp_path / "b.md").write_text('{{ include "a.md" }}', encoding="utf-8")
    with pytest.raises(CompileError, match="circular include"):
        PromptCompiler(tmp_path).compile("a.md", {})


def test_path_escape_is_rejected(tmp_path):
    root = tmp_path / "prompts"
    root.mkdir()
    (tmp_path / "secret.md").write_text("secret", encoding="utf-8")
    (root / "main.md").write_text('{{ include "../secret.md" }}', encoding="utf-8")
    with pytest.raises(CompileError, match="escapes source root"):
        PromptCompiler(root).compile("main.md", {})


def test_golden_drift_is_rejected(tmp_path):
    artifact = PromptCompiler(ROOT / "prompts").compile("home.prompt.md", {"family_members": 4})
    golden = tmp_path / "home.compiled.md"
    golden.write_text("stale output", encoding="utf-8")
    with pytest.raises(CompileError, match="differs"):
        PromptCompiler.verify_golden(artifact, golden)
