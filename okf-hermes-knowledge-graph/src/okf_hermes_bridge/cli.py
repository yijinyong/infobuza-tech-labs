import argparse
import json

from .graph import KnowledgeGraph, build_hermes_context


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle")
    parser.add_argument("query")
    parser.add_argument("--max-nodes", type=int, default=3)
    args = parser.parse_args()
    payload = build_hermes_context(
        KnowledgeGraph.load(args.bundle), args.query, max_nodes=args.max_nodes
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
