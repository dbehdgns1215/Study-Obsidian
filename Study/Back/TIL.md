
## ✅ 한 방에 비교 (이 표만 기억해라)

|구분|Axios Interceptor|Spring Interceptor|Servlet Filter|
|---|---|---|---|
|위치|**브라우저(프론트)**|**서버(Spring MVC)**|**서버(서블릿 컨테이너)**|
|실행 시점|요청 전 / 응답 후|컨트롤러 전 / 후|요청 가장 처음 / 응답 마지막|
|관리 주체|Axios|Spring|Tomcat|
|Spring 의존|❌|✅|❌|
|컨트롤러 접근|❌|✅|❌|
|보안/인증|❌|❌(보조만)|✅|
|JWT 검증|❌|❌|✅|
|대표 용도|AT 붙이기, 401 처리|로깅, 권한 체크 보조|인증, 인가, CORS|

---

## 🔥 실제 요청 흐름 (SPA + Spring)

`[Vue]  → Axios Interceptor         (AT 붙임)  → HTTP  → Servlet Filter            (JWT 검증)  → DispatcherServlet  → Spring Interceptor        (로그, 체크)  → Controller  → Spring Interceptor  → Servlet Filter  → HTTP  → Axios Interceptor         (401 처리)  → [Vue]`

👉 **각자 자기 영역만 건드린다**

---

## 🧠 각자 한 문장 요약

### Axios Interceptor

> “요청 보내기 전에 내가 좀 손보고,  
> 응답 오면 에러 있나 볼게”

### Spring Interceptor

> “컨트롤러 들어가기 전후에  
> 부가 작업 좀 할게”

### Servlet Filter

> “서버 입장권 검사부터 할게  
> 이상하면 바로 돌려보낸다”