
# Servlet 구조

- `@WebServlet(...)`: URL 매핑 설정
- `public class HelloServlet extends HttpServlet`: HttpServlet 상속
- `doGet(), doPost()`: 재정의
![[Pasted image 20250917102041.png]]
- 예외는 tomcat 같은 WAS가 받게 됨.
- 예외 처리 또한 WAS가

## Servlet 주료 API
- `extends jakarta.servlet.http.HtttpServlet`
	- Jakarta EE의 패키지 (과거 Java EE)
	- tomcat 등 웹 컨테이너들이 Jakarta EE 구현
![[Pasted image 20250917102758.png]]

## Servlet Life Cycle 관리
![[Pasted image 20250917102819.png]]
- 개발자는 Servlet을 만들지만 객체를 만든다거나 호출하진 않음.
	- Container가 life cycle에 따라서 관리함
- 각각의 라이프 사이클 훅에서 할 일을 개발자가 적절히 작성 -> Container에게 넘겨주고 호출
- 이를 통해 Servlet이 효율적인 자원 관리, 최적화 된 성능 구현을 가능하게 함.

- 관련 메서드
	- `init()`: 어떤 요청도 init이 종료되기 전에는 처리될 수 없음.
		- Servlet에서 필요한 자원 초기화
	- `service()`: 실제 사용자의 요청을 처리하는 메서드
		- 요청 방식에 따라 doGet(), doPost() 호출
	- `destroy()`: 어떤 요청이라도 처리하고 있으면 destroy는 동작하지 않음.
		- init에서 초기화 한 자원의 정리 작업


## HttpServletRequest, HttpServletResponse
- 각각 Http의 `Request`, `Response`를 추상화하기 위한 JEE 인터페이스
- HTTP Request와 Response 포맷

![[Pasted image 20250917103652.png]]