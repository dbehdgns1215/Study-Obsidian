
Node 서버 + mysql ?

```powershell
# Docker는 각 운영 체제별로 설치 지침을 제공합니다.
# 공식 문서는 https://docker.com/get-started/에서 확인하세요.

# Node.js Docker 이미지를 풀(Pull)하세요:
docker pull node:24-alpine

# Node.js 컨테이너를 생성하고 쉘 세션을 시작하세요:
docker run -it --rm --entrypoint sh node:24-alpine

# Verify the Node.js version:
node -v # Should print "v24.11.1".

npm 버전 확인:
npm -v # 11.6.2가 출력되어야 합니다.

```

```powershell
docker pull mysql:8.1
```

![[Pasted image 20251126232047.png]]

