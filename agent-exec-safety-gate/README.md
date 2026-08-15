# Agent Execution Safety Gate

AI가 만든 코드를 실행하기 전에 runtime, network, filesystem, secret, timeout, purpose를 결정적으로 검사하고 샌드박스 실행 profile을 만드는 예제입니다. 실제 격리 런타임을 대체하지 않으며 Cloud Run sandbox, microVM, container 앞의 정책 계층으로 사용합니다.

```bash
python -m pip install -e ".[test]"
agent-safety-gate examples/margin-analysis.json
python -m pytest
```

- [구조](ARCHITECTURE.md) · [활용 예제](EXAMPLES.md) · [운영 한계](LIMITATIONS.md)
