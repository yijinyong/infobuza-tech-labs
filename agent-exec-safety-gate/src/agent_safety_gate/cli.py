import argparse,json
from pathlib import Path
from .policy import ExecutionRequest,Policy,evaluate

def main():
    p=argparse.ArgumentParser()
    p.add_argument("request")
    p.add_argument("--allow-network",action="store_true")
    p.add_argument("--allow-write",action="store_true")
    a=p.parse_args()
    data=json.loads(Path(a.request).read_text(encoding="utf-8"))
    decision=evaluate(ExecutionRequest(**data),Policy(allow_network=a.allow_network,allow_write=a.allow_write))
    print(json.dumps({"allowed":decision.allowed,"reasons":decision.reasons,"sandbox_profile":decision.sandbox_profile},ensure_ascii=False,indent=2))
    raise SystemExit(0 if decision.allowed else 2)

if __name__=="__main__": main()
