from __future__ import annotations

import argparse
import json

from .experiment import run_comparison


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare hidden-session and self-describing routing")
    parser.add_argument("--requests", type=int, default=20, help="requests per mode")
    args = parser.parse_args()
    print(json.dumps(run_comparison(args.requests), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
