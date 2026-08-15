# MCP Stateless Routing Lab

MCP 2026-07-28의 자기완결 요청이 라운드로빈 라우팅에서 숨은 로컬 세션 의존성을 어떻게 제거하는지 재현하는 완전한 예제 프로젝트입니다.

이 프로젝트는 MCP SDK 정합성 시험이나 성능 벤치마크가 아닙니다. 프로토콜 변경이 라우팅 구조에 미치는 영향만 고립해 보여줍니다.

## 실행 환경

- Python 3.11 이상
- 외부 런타임 의존성 없음
- 테스트에는 pytest 사용

## 다운로드와 실행

```bash
git clone https://github.com/yijinyong/infobuza-tech-labs.git
cd infobuza-tech-labs/mcp-2026-stateless-routing
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -e ".[test]"
mcp-routing-lab
pytest
```

## 예상 결과

```json
{
  "requests_per_mode": 20,
  "legacy_round_robin_success": 10,
  "legacy_round_robin_failure": 10,
  "stateless_round_robin_success": 20,
  "stateless_round_robin_failure": 0
}
```

## 코드 구조

```text
src/mcp_routing_lab/model.py       핵심 상태형·자기완결 요청 모델
src/mcp_routing_lab/experiment.py  반복 가능한 비교 실험
src/mcp_routing_lab/cli.py         JSON 결과를 출력하는 CLI
tests/                             정상·실패·입력 검증 테스트
```

## 해석 범위

- 검증함: 인스턴스 로컬 세션이 비고정 라우팅에서 만드는 의존성
- 검증하지 않음: 공식 MCP SDK 호환성, 네트워크 지연, 처리량, 인증 서버

## License

MIT
