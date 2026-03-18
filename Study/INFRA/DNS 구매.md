
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

