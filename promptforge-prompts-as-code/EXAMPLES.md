# Examples

```bash
# 업무: SRE 장애 대응
promptforge prompts sre.prompt.md --vars examples/sre.json --output build/sre.md

# 업무: 고객지원 정책
promptforge prompts support.prompt.md --vars examples/support.json --output build/support.md

# 생활: 가족 일정 정리
promptforge prompts home.prompt.md --vars examples/home.json --output build/home.md
```

CI에서는 `--check`로 커밋된 golden artifact와 새 빌드 결과를 비교할 수 있습니다.
