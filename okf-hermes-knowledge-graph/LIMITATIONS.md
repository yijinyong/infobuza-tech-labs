# Limitations

- 완전한 OKF v0.2 parser나 validator가 아닙니다.
- 단순 lexical seed 검색이므로 동의어나 다국어 표현을 놓칠 수 있습니다.
- Markdown 본문을 신뢰하지 않습니다. 운영에서는 provenance, trust, 서명과 prompt injection 검사가 필요합니다.
- 노드별 ACL과 사용자 인증을 구현하지 않았습니다.
- Hermes Agent 프로세스에 자동 설치되는 공식 플러그인이 아니라 공개 훅의 payload를 재현한 교육용 브리지입니다.
