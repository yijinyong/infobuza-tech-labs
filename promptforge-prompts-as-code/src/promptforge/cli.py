import argparse
import json
from pathlib import Path

from .compiler import PromptCompiler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root")
    parser.add_argument("entry")
    parser.add_argument("--vars", required=True)
    parser.add_argument("--output")
    parser.add_argument("--check")
    args = parser.parse_args()
    variables = json.loads(Path(args.vars).read_text(encoding="utf-8"))
    compiler = PromptCompiler(args.source_root)
    artifact = compiler.compile(args.entry, variables)
    if args.check:
        compiler.verify_golden(artifact, args.check)
    if args.output:
        Path(args.output).write_text(artifact.content, encoding="utf-8")
    print(json.dumps({
        "sha256": artifact.sha256,
        "dependencies": artifact.dependencies,
        "characters": len(artifact.content),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
