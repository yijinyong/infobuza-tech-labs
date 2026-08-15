# InfoBuza Tech Labs

인포부자 기술 블로그에서 소개한 실행 가능한 예제 프로젝트를 한 곳에 관리하는 공개 모노레포입니다.

각 하위 프로젝트는 다음을 포함합니다.

- 전체 소스 코드
- 독립 실행 방법
- 자동 테스트
- 블로그에서 주장한 실험의 재현 범위와 한계

## Labs

| 프로젝트 | 설명 | 실행 |
|---|---|---|
| [mcp-2026-stateless-routing](./mcp-2026-stateless-routing) | MCP 2026-07-28 자기완결 요청과 로컬 세션의 라우팅 의존성 비교 | `python -m pytest` |
| [okf-hermes-knowledge-graph](./okf-hermes-knowledge-graph) | OKF 그래프의 관련 노드만 Hermes 컨텍스트로 전달하는 최소 브리지 | `python -m pytest` |
| [promptforge-prompts-as-code](./promptforge-prompts-as-code) | 모듈 프롬프트 컴파일·정적 검사·golden drift 재현 | `python -m pytest` |

## Clone

```bash
git clone https://github.com/yijinyong/infobuza-tech-labs.git
cd infobuza-tech-labs
```

## 원칙

블로그에 새로운 코드를 제시할 때는 이 저장소에 완전한 프로젝트와 테스트를 먼저 올리고, push 후 새 clone 환경에서 재검증합니다.
