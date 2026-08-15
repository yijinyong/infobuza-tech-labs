# OKF × Hermes Agent Knowledge Graph Lab

OKF 스타일 Markdown bundle에서 질문과 관련된 노드와 연결된 이웃만 찾아 Hermes Agent의 `pre_llm_call` 훅 반환 형식인 `{"context": "..."}`로 만드는 최소 실험입니다.

이 코드는 완전한 OKF v0.2 validator나 공식 Hermes 플러그인이 아닙니다. 두 프로젝트의 통합 경계를 재현하기 위한 교육용 bridge입니다.

## 실행

```bash
python -m venv .venv
python -m pip install -e ".[test]"
okf-hermes-lab sample-bundle "배포 실패 시 어떻게 처리합니까?" --max-nodes 2
python -m pytest
```

Hermes 플러그인에서는 `pre_llm_call` 콜백이 `build_hermes_context(...)` 결과를 반환하도록 연결할 수 있습니다. 운영 적용 전에는 공식 OKF validator, 경로 접근 제어, 신뢰 등급, provenance 검증, 컨텍스트 크기 제한을 추가해야 합니다.
