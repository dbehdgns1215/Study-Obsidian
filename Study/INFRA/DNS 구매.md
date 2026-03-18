
https://www.hosting.kr/
- 호스팅.KR에서 세금 포함 + 개인정보 보호 포함 5720원에 구매


![[Pasted image 20260318222902.png]]
- 구매 후 네임서버/DNS 세팅
	- 유형 A로 하나는 `구매한 도메인` 으로 접속하는 경로
	- 또 하나는 `www`를 붙이고 접속하는 경로
	- 또한 `_acme-challenge`는 EC2 내부에서 `Let's Encrypt`의 `certbot` 명령어를 통해서 SSL 인증서를 발급받고, 이 과정에서 해당 도메인의 소유자가 정말 나인지를 확인하기 위해서 이렇게 DNS 레코드에 추가를 해주는 것.

```
sudo certbot certonly --manual --preferred-challenges dns -d plys.today
Saving debug log to /var/log/letsencrypt/letsencrypt.log

```


![[Pasted image 20260318223307.png]]
- 성공



### HTTP (80포트) 강제 이동 규칙 변경

- **기존 코드:**
```Nginx
server_name j14b206.p.ssafy.io;
return 301 https://$host$request_uri;
```
    
- **변경 코드:** 
```Nginx
server_name j14b206.p.ssafy.io plys.today;
return 301 https://plys.today$request_uri;
```
- **설명:** 기존에는 사용자가 구 주소로 접속하면 구 주소의 HTTPS로 보냈음.
- 변경된 코드에서는 구 주소와 신 주소 어느 쪽으로 80포트(일반 HTTP) 접속을 하든, 무조건 새 도메인인 `https://plys.today` 로 강제 이동시키도록 목적지를 하나로 고정
    

### 기존 구 주소 HTTPS (443포트) 블록의 역할 축소

- **기존 코드:** 구 주소용 HTTPS 블록 하나에 모든 API 라우팅(`location`) 로직이 다 들어있었습니다.
    
- **변경 코드:**
```Nginx
server {
	listen 443 ssl;
	server_name j14b206.p.ssafy.io;
	# 인증서는 그대로 유지
	return 301 https://plys.today$request_uri;
}
```
- **설명:** 이 블록은 이제 아무런 기능(로직)을 수행하지 않음. 
- 오직 구주소만을 알고있는 사용자가 접속했을 때 보안 경고창이 뜨지 않도록 기존 인증서만 유지한 채, 곧바로 새 주소로 튕겨내는(301 리다이렉트) 역할만 담당하도록 축소시킴

### 새로운 메인 서버 블록 생성 (신 주소 HTTPS)

- **기존 코드:** 없음
    
- **변경 코드:**
```Nginx
server {
listen 443 ssl;
server_name plys.today;
# 새 인증서 적용
# ... (이하 모든 location 로직 배치) ...
}
```
- **설명:** `plys.today` 라는 새 간판을 위한 전용 서버 블록이 통째로 추가되었음.
- 서버에서 직접 발급받은 새 도메인용 인증서 경로가 여기에 적용되었으며, 프론트엔드 연결, 백엔드 API 연결, 웹훅 연결 등 실제 서비스 구동에 필요한 모든 `location` 라우팅 설정들이 구 주소 블록에서 이 신 주소 블록으로 전부 옮겨졌음

