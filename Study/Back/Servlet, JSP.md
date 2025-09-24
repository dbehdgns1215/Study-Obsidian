
# Servlet 구조

- `@WebServlet(...)`: URL 매핑 설정
- `public class HelloServlet extends HttpServlet`: HttpServlet 상속
- `doGet(), doPost()`: 재정의
![[Pasted image 20250917102041.png]]
- 예외는 tomcat 같은 WAS가 받게 됨.
- 예외 처리 또한 WAS가

## Servlet 주요 API
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



### HttpServletRequest
![[Pasted image 20250917104023.png]]

![[Pasted image 20250917104434.png]]
- `<form>` 또는 queryString을 통해서 클라이언트가 전달한 값으로 언제나 문자열
	- 처음 클라이언트에서 설정된 이후 조작은 불가능함.



### HttpServletResponse
![[Pasted image 20250917104047.png]]

#### Http Status
![[Pasted image 20250917105232.png]]


#### Content-Type, Character Encoding
- Content-Type
	- 서버가 전송하는 데이터의 MIME 타입으로 데이터의 형식과 인코딩 방식을 포함함
	- 주요 Content-Type
![[Pasted image 20250917105506.png]]

- Character Encoding
	- 데이터를 컴퓨터가 이해하고 처리할 수 있는 형태로 변환하는 방법
	- 응답의 기본 encoding은 `IOS-8859-1`로 한글 전송이 불가능함.
		- `setContentType`을 통해서 UTF-8로 지정 가능.



## 기존 서블릿 작성 방식의 문제점
![[Pasted image 20250918091603.png]]

# Front Controller Pattern
![[Pasted image 20250918091635.png]]
- 그럼 main은 어떻게 요청들을 구별할 수 있을까?

![[Pasted image 20250918092012.png]]
- url에 파라미터 추가
	- `<form>`에서는 `hidden` 옵션을 이용하면 된다
- 와일드 카드를 이용한 URL 매핑


## Front Controller 작성
![[Pasted image 20250918092431.png]]

![[Pasted image 20250918092743.png]]

`FrontController`
```java
package com.ssafy.live.controller;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * Servlet implementation class MainController
 */
@WebServlet("/main")
public class MainController extends HttpServlet implements ControllerHelper {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// 1. action 파라미터 추출
		String action = preProcessing(request, response);
		switch(action) {
			
		}
		
		
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// 1. action 파라미터 추출
		String action = preProcessing(request, response);
		switch(action) {
		case "login" -> login(request, response);
		}
	}
	
	// Controller
	protected void login(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// 1. 파라미터 추출
		String id = request.getParameter("id");
		String pass = request.getParameter("pass");
		
		// 2. 비즈니스 로직 호출
		String result = null;
		if("ssafy".equals(id) && "1234".equals(pass)) {
			result = "로그인 성공";
		} else {
			result = "id/pass 확인해라";
		}
		
		// 3. 화면 처리
		responseHtml(response, "로그인 결과", result);
	}
	
	protected void template(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// 1. action 파라미터 추출
		String action = preProcessing(request, response);
		switch(action) {
			
		}
	}

}

```

# Filter
- 여러 개의 컨트롤러에서 부분적으로 필요한 공통 기능이 있다면?
![[Pasted image 20250918100829.png]]

![[Pasted image 20250918101328.png]]

## Filter의 주요 용도
![[Pasted image 20250918101305.png]]


## Filter의 작성
![[Pasted image 20250918101505.png]]
![[Pasted image 20250918101705.png]]
![[Pasted image 20250918101840.png]]

**아래와 같은 경우에도 필터가 사용됨**
![[Pasted image 20250918103435.png]]

![[Pasted image 20250918103408.png]]


# Listener
- 웹 애플리케이션에서 발생하는 이벤트에 대한 모니터링 객체
- 웹 애플리케이션에서 발생하는 이벤트?
![[Pasted image 20250918104615.png]]
- ServletContextListener: 웹 애플리케이션 생성에서 소멸까지의 주요 사항 모니터링
	- 개별 서블릿 동작 전에 초기화하는데 비용이 많이 드는 공유 자원의 초기화에 주로 사용




# JSP

![[Pasted image 20250923102122.png]]


## Life Cycle
![[Pasted image 20250923102107.png]]


## 구성 요소
![[Pasted image 20250923102145.png]]

![[Pasted image 20250923102338.png]]
```jsp
<%@page import="java.time.LocalDateTime"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Insert title here</title>
	</head>
	<body>
	<%-- JSP 주석: 클라이언트에게는 가지 않는다. --%>
	<!-- HTML 주석: 클라이언트에게 전달 된다. -->
	<%
		// Script let: 실행문 작성
		LocalDateTime now = LocalDateTime.now();
		out.println(now);
		String temp = sayHello();
		out.println(temp);
	%>
	
	<%!
		// declaration: 선언부, 멤버 변수 또는 메서드
		private String sayHello() {
			return "Hello";
		}
	%>

	<%=
		// expression: 표현식, 출력할 내용
		sayHello()
	%>
	</body>
</html>
```

## 내장 객체
![[Pasted image 20250923102357.png]]

## 정리
![[Pasted image 20250923102415.png]]


# MVC

## MVC 1
![[Pasted image 20250923102443.png]]

## MVC 2
![[Pasted image 20250923102456.png]]
![[Pasted image 20250923102513.png]]



# EL & JSTL

- JSP를 좀 더 JSP답게 만드는 요소
```jstl
<%
Object error = request.getAttribute("error")
	if (error != null) {
		out.println("...");
	}
%>
```
- 기존 방식


- JSP에서 최대한 프로그래밍 요소 제거
	- 많은 부분을 진짜 태그 중심으로 변경
	- 디자이너, 퍼블리셔 등이 쉽게 접근하고 이해할 수 있도록
- EL (Expression Language)
	- 표현, 즉 출력을 위한 언어로 JSP의 expression (`<%=...%>`)대체
	- 단순한 출력, 특히 웹 스코프에 저장된 attribute를 사용하는 데 편리
- JSTL (JSP Standard Tag Library)
	- 자주 사용되는 기능들에 대해 정형화된 태그 제공

