
# SSL 발급 명령어 히스토리 (Step 1)


> 작성일: 2026-03-10

> 내용: 우분투(Ubuntu) EC2 환경에서 `j14b206.p.ssafy.io` 도메인에 대한 Let's Encrypt SSL 인증서를 실제 발급받기 위해 사용된 모든 명령어의 흐름과 트러블슈팅 내역입니다.

---
## 🚀 실제 사용된 명령어 전체 흐름

### 1. (사전 작업) 충돌하는 옛날 패키지 제거 및 Snap 코어 업데이트

우분투 기본 패키지 매니저(apt)에 있는 오래된 certbot을 지우고, 최신 snap 환경을 세팅합니다.

```bash

sudo apt-get remove certbot

sudo snap install core; sudo snap refresh core

```

  

### 2. Certbot 설치 (과거에 이미 설치되어 있었음)

아래 명령어를 쳤을 때 `snap "certbot" is already installed`라는 메시지가 나오며 실패했는데, 이는 **이전에 이미 완벽하게 설치되었다는 성공의 의미**입니다.

```bash

sudo snap install --classic certbot

sudo ln -s /snap/bin/certbot /usr/bin/certbot

```

*(결과: 이미 잘 설치되어 있어서 에러가 났으므로 기분 좋게 무시하고 다음 단계로 넘어감)*


### 3. 포트 충돌 방지를 위한 Nginx 강제 종료 (트러블슈팅 포인트)

Certbot의 `--standalone` 모드는 본인이 직접 80번 포트 웹페이지를 열어서 도메인을 인증받는 방식입니다.

```bash

# Nginx 컨테이너 구동 강제 중지

docker stop playlist-nginx

```

  

### 4. 대망의 인증서 발급 🌟

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


