# Architecture

요청에서 응답 컨텍스트까지의 책임을 세 층으로 나눕니다.

1. **Knowledge domain** — `Concept`, 링크 그래프, 질문 관련도와 이웃 탐색입니다.
2. **Retrieval policy** — `RetrievalPolicy`가 노드 수와 문자 예산을 검증합니다.
3. **Hermes adapter** — `build_context_envelope`는 감사 metadata를 만들고, `build_hermes_context`는 Hermes `pre_llm_call` 계약에 맞춰 `context`만 반환합니다.
4. **Delivery adapter** — CLI가 bundle, 질문, 정책 값을 받아 JSON으로 출력합니다.

파일 시스템 밖으로 향하는 Markdown 링크는 그래프에 포함하지 않습니다. 운영 구현에서는 이 검사에 심볼릭 링크 정책과 노드별 ACL을 추가해야 합니다.
