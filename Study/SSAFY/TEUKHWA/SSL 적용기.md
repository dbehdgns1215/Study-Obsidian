
# Step 1 - EC2 내부에서 certbot 다운

## 실제 사용된 명령어 전체 흐름

### 1. (사전 작업) 충돌하는 옛날 패키지 제거 및 Snap 코어 업데이트

우분투 기본 패키지 매니저(apt)에 있는 오래된 certbot을 지우고, 최신 snap 환경을 세팅합니다.

```bash

sudo apt-get remove certbot

sudo snap install core; sudo snap refresh core

```

  
### 2. Certbot 설치 

```bash

sudo snap install --classic certbot

sudo ln -s /snap/bin/certbot /usr/bin/certbot

```


### 3. 포트 충돌 방지를 위한 Nginx 강제 종료 (트러블슈팅 포인트)

Certbot의 `--standalone` 모드는 본인이 직접 80번 포트 웹페이지를 열어서 도메인을 인증받는 방식입니다.

```bash

# Nginx 컨테이너 구동 강제 중지

docker stop playlist-nginx

```

  
### 4. 대망의 인증서 발급

80포트가 비워진 것을 확인한 후, 순수 네이키드 도메인명을 넣어 인증서를 발급받았습니다.

```bash

sudo certbot certonly --standalone -d j14b206.p.ssafy.io

```

이후에 뜨는 이메일 입력, 이용약관 동의(Y) 절차를 거쳐 최종적으로 `Congratulations!` 메시지와 함께 아래 경로에 인증서가 저장되었습니다.


> 만약 `Some challenges have failed.` 오류가 뜬다면?

Let's Encrypt 센터에서 사용자님의 `j14b206.p.ssafy.io` (IP: 3.34.144.211) 의 **80포트(HTTP)로** 접속해서 **"너 진짜 이 도메인 주인 맞니?"** 하고 검사하려고 들어왔는데, 문이 꽉 잠겨있어서 튕겨 나간 겁니다.

도커가 80포트를 쓸 때는 자기 마음대로 방화벽을 뚫고 나가서 그동안 접속이 됐던 거지만, 우분투 호스트 자체의 80포트는 현재 막혀있을 확률이 99%입니다.
*   인증서 경로: `/etc/letsencrypt/live/j14b206.p.ssafy.io/fullchain.pem`
*   비밀키 경로: `/etc/letsencrypt/live/j14b206.p.ssafy.io/privkey.pem`


```
ubuntu@ip-172-26-11-62:/var/jenkins_home/workspace/plys/plys-backend/infra$ sudo certbot certonly --standalone -d j14b206.p.ssafy.io
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Requesting a certificate for j14b206.p.ssafy.io

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/j14b206.p.ssafy.io/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/j14b206.p.ssafy.io/privkey.pem
This certificate expires on 2026-06-08.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
 * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
 * Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ubuntu@ip-172-26-11-62:/var/jenkins_home/workspace/plys/plys-backend/infra$ 
```

![[Pasted image 20260310124303.png]]



# Step 2 - Docker Compose

```yml
nginx:  
  image: ${DOCKER_USERNAME}/playlist-nginx:latest  
  container_name: playlist-nginx  
  ports:  
    - "80:80"  
    - "443:443"  // 포트 개방
  volumes:  
    - /etc/letsencrypt:/etc/letsencrypt:ro  // letsencrypt 볼륨 마운트
  networks:  
    - app-network  
  depends_on:  
    - backend-blue  
  restart: always
```
- 포트를 열고
- 호스트 PC의 /etc/letsencrypt와 컨테이너의 /etc/letsencrypt를 읽기 전용(ro)로 마운트해서 Nginx가 인증서를 읽을 수 있게끔 처리
	- 사실상 컨테이너는 독립된 공간이기에 호스트 PC의 파일을 읽을 수 없음.


# Step 3 - nginx.conf

```
# HTTPS (SSL) 메인 서버  
server {  
    listen 443 ssl;  
    server_name j14b206.p.ssafy.io;  
  
    # SSL 인증서 및 키 경로 (컨테이너 내부 기준)  
    ssl_certificate /etc/letsencrypt/live/j14b206.p.ssafy.io/fullchain.pem;  
    ssl_certificate_key /etc/letsencrypt/live/j14b206.p.ssafy.io/privkey.pem;  
  
    # SSL 최적화 설정  
    ssl_protocols TLSv1.2 TLSv1.3;  
    ssl_prefer_server_ciphers on;
```
- Nginx가 443 포트를 리스닝 하고있는데, 해당 포트로 들어오는 요청은 SSL 암호화 통신 적용할거임슨
- HTTP 요청 헤더의 호스트 이름이 `j14b206.p.ssafy.io`일 경우, Nginx가 이 서버 블록의 규칙을 적용할거임슨
- 인증서 경로와 인증서 키 경로 (이전에 certbot으로 다운함) 등록
- 최적화 설정은 구버전 프로토콜(SSLv3, TLS 1.0, TLS 1.1)의 연결 차단, 클라이언트가 지원하는 방식보다 서버(Nginx)에 설정된 암호화 알고리즘을 우선적으로 선택하도록 강제

이제 다시 배포하면 됨.

엔진엑스만 재시작하면 됨.

# 성공

![[Pasted image 20260310131046.png]]
