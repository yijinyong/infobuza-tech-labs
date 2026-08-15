# Examples

```bash
# 업무: 네트워크 없는 매출 마진 계산
agent-safety-gate examples/margin-analysis.json
# 업무: 공개 웹 조사(명시적 허용 필요)
agent-safety-gate examples/web-research.json --allow-network
# 생활: 가계부 결과 저장(임시 쓰기 허용 필요)
agent-safety-gate examples/home-budget.json --allow-write
```
