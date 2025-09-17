
# Servlet 구조

- `@WebServlet(...)`: URL 매핑 설정
- `public class HelloServlet extends HttpServlet`: HttpServlet 상속
- `doGet(), doPost()`: 재정의
![[Pasted image 20250917102041.png]]
- 예외는 tomcat 같은 WAS가 받게 됨.
- 예외 처리 또한 WAS가

