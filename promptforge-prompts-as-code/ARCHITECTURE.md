# Architecture

1. Source layer: 재사용 가능한 `.prompt.md` 파일입니다.
2. Compiler domain: include graph, 변수 치환, 순환 의존성과 경로 검사를 담당합니다.
3. Build artifact: 결정적인 Markdown과 SHA-256, dependency manifest를 생성합니다.
4. Delivery adapter: CLI가 CI와 로컬 빌드에서 같은 컴파일러를 실행합니다.

런타임 모델 호출과 분리되어 있으므로 프롬프트 오류를 배포 전에 발견하는 것이 목적입니다.
