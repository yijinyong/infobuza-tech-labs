# PromptForge: Prompts-as-Code Lab

시스템 프롬프트를 모듈로 나누고 빌드 시점에 include, 변수, 순환 의존성, 경로 이탈과 golden drift를 검사하는 교육용 컴파일러입니다.

```bash
python -m venv .venv
python -m pip install -e ".[test]"
promptforge prompts sre.prompt.md --vars examples/sre.json --output build/sre.md
python -m pytest
```

업무용 SRE·고객지원 예제와 생활용 가족 일정 도우미 예제를 제공합니다. 특정 LLM SDK에 의존하지 않으며, 생성된 Markdown을 사용하는 에이전트의 system instruction 입력에 연결할 수 있습니다.

- [구조](./ARCHITECTURE.md)
- [실행 예제](./EXAMPLES.md)
- [한계](./LIMITATIONS.md)
