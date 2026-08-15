# Architecture

1. Request domain: 실행 목적과 필요한 capability를 선언합니다.
2. Policy engine: deny-by-default 규칙으로 결정을 만듭니다.
3. Sandbox profile adapter: 격리 런타임에 전달할 제한을 만듭니다.
4. CLI adapter: CI와 서비스가 JSON 요청을 같은 규칙으로 검사합니다.

정책 통과는 실행 허가 조건 중 하나일 뿐이며 실제 OS 격리는 별도 런타임이 담당합니다.
