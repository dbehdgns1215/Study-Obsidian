
섹션 제목 `#`
섹션별 소제목 `##`
강의별 소제목 `####`

# 섹션 2. 웹 애플리케이션 이해

## 웹 서버, 웹 애플리케이션 서버
![[Pasted image 20250416234837.png]]

#### 모든 것이 HTTP!
**HTTP 메시지에 모든 것을 전송**

- HTML, TEXT
- IMAGE, 음성, 영상, 파일
- JSON, XML (API를 사용할 때 주로 사용)
- 거의 모든 형태의 데이터 전송 가능
- 서버간의 데이터를 주고 받는 경우에도 대부분 HTTP 사용

#### 웹 서버(Web Server)
- HTTP 기반으로 동작
- 정적 리소스 제공, 기타 부가 기능 제공
- 정적(파일) HTML, CSS, JS, 이미지, 영상 등을 지원
- 예) NGINX, APACHE

![[Pasted image 20250416235325.png]]


#### 웹 애플리케이션 서버(WAS - Web Application Server)
- HTTP 기반으로 동작
- 웹 서버 기능 포함(정적 리소스도 당연히 제공 가능)
- 프로그램 코드를 실행해서 애플리케이션 로직 수행
	- 동적 HTML 생성, HTTP API(JSON) 지원
	- 서블릿, JSP, 스프링 MVC 등을 지원
	- 예) 특정 사용자에 따라서 다른 페이지를 보여줄 수 있음.
- 예) 톰캣(Tomcat) Jetty, Undertow

![[Pasted image 20250416235510.png]]


#### 웹 서버, 웹 애플리케이션 서버
**차이**

- 웹 서버는 정적 리소스(파일)를 제공, WAS는 애플리케이션 로직을 실행할 수 있음
- 사실은 둘의 용어와 경계가 다소 모호함.
	- 웹 서버도 프로그램을 실행하는 기능을 포함하기도 함
	- WAS도 웹 서버의 기능을 제공함
- 자바는 서블릿 컨테이너 기능을 제공하면 WAS
	- 단, 서블릿 없이 자바 코드를 실행하는 서버 프레임워크도 있기는 함.
- WAS는 애플리케이션 코드를 실행하는데 더 특화되어있음


#### 웹 시스템 구성 - WAS, DB
- WAS, DB 만으로 시스템 구성 가능
- WAS는 정적 리소스, 애플리케이션 로직 모두 제공 가능하기 때문

![[Pasted image 20250417000107.png]]
- WAS가 너무 많은 일을 감당하고 있다는 생각이 들지 않나?..

![[Pasted image 20250417000148.png]]
- WAS가 너무 많은 역할을 담당하면 서버 과부하의 우려가 생김
- 가장 비싼 애플리케이션 로직이 정적 리소스(비교적 싼) 때문에 원할한 수행이 어려울 수 있음
- WAS 장애시 오류 화면조차도 노출 불가능
- 따라서 큰 시스템에서는 WAS + DB로 구축하기에는 어려움이 큼

 
#### 웹 시스템 구성 - WEB, WAS, DB (1)
 
- 정적 리소스는 **웹 서버가 처리**
- **웹 서버**는 애플리케이션 로직같은 **동적인 처리가 필요할 때마다** WAS에 요청을 위임
- **WAS**는 중요한 **애플리케이션 로직 처리 전담**
 ![[Pasted image 20250417000409.png]]

#### 웹 시스템 구성 - WEB, WAS, DB (2)
**추가적인 장점**
- 효율적인 리소스 관리가 가능해짐
	- 정적 리소스가 많이 사용되면 WEB 서버 증설하면 됨
	- 애플리케이션 리소스가 많이 사용되면 WAS 증설하면 됨
![[Pasted image 20250417000605.png]]

#### 웹 시스템 구성 - WEB, WAS, DB (3)
- 정적 리소스만 제공하는 웹 서버는 잘 죽지 않음
- 애플리케이션 로직이 동작하는 WAS는 잘 죽음
- WAS, DB 장애시에 웹 서버가 오류 화면 제공해줄 수 있어짐
![[Pasted image 20250417000744.png]]


---

## 서블릿

#### HTML Form 데이터 전송
**POST 전송 - 저장

![[Pasted image 20250417001021.png]]
- 만약 위와 같은 HTML 폼이 있다고 가정해보자.
- `전송` 버튼을 눌렀을 때 무슨 일이 발생할까?
	- 웹 브라우저가 요청 HTTP 메시지(우측)를 만들어냄
	-  만들어 낸 HTTP 요청 메시지를 서버에게 전달함

#### 서버에서 처리해야 하는 업무
**웹 애플리케이션 서버 직접 구현**

![[Pasted image 20250417001157.png]]
- 서버를 직접 구현하려면, 웹 브라우저가 생성한 HTTP 메서드를 파싱해서 분석해야함.
- 왼쪽 박스에 있는 순서대로 로직들을 실행해야만 함.

#### 서버에서 처리해야 하는 업무
**서블릿을 지원하는 WAS 사용**

![[Pasted image 20250418000202.png]]
- 전 세계 개발자가 모두 비효율적인 로직을 따를 필요가 없음.
- 따라서 대두된 것이 `서블릿` 이다.
- 서블릿은 왼쪽 박스의 초록 부분을 제외한 나머지 부분들을 자동으로 지원해준다.
#### 서블릿
**특징**

![[Pasted image 20250417001442.png]]
- urlPatterns(/hello)의 URL이 호출되면 서블릿 코드가 살행됨
- HTTP 요청 정보를 편리하게 사용할 수 있는 HttpServletRequest
- HTTP 응답 정보를 편리하게 제공할 수 있는 HttpServletResponse
- 개발자는 HTTP 스택을 매우 편리하게 사용함


![[Pasted image 20250418003128.png]]
- 웹 브라우저에서 먼저 `localhost:8080/hello`로 요청을 보냄
- WAS 에서는 요청 메시지를 기반으로 방금 본 `request`, `response` 객체를 만들어냄
- 이후 서블릿 컨테이너를 통해서 만들어낸 `request`, `response` 객체를 파라미터로 넘기면서 `helloServlet` 을 실행함
- `helloServlet`의 실행이 끝나고 리턴값 `response` 이 있을텐데, 이것을 바탕으로 HTTP 응답 메시지를 만들어냄
- 웹 브라우저에게 응답 메시지를 전달함.

#### HTTP 요청, 응답 흐름
- HTTP 요청시
	- WAS는 Request, Response 객체를 새로 만들어서 서블릿 객체를 호출함
	- 개발자는 Request 객체에서 HTTP 요청 정보를 편리하게 꺼내서 사용
	- 개발자는 Response 객체에 HTTP 응답 정보를 편리하게 입력
	- WAS는 Response 객체에 담겨있는 내용으로 HTTP 응답 정보를 생성


#### 서블릿 컨테이너

![[Pasted image 20250418003949.png]]
- 서블릿 객체는 사실 개발자가 직접 생성하는 것이 아님.
- WAS 안에는 서블릿을 지원하는 `서블릿 컨테이너`라는 것이 있음
- 이 서블릿 컨테이너는 서블릿 객체를 `자동`으로 `생성`, `호출`, `관리` 해줌.

**특징**
- 톰캣처럼 서블릿을 지원하는 WAS를 서블릿 컨테이너라고 함
- 서블릿 컨테이너는 서블릿 객체를 생성, 초기화, 호출, 종료하는 생명주기를 관리
- 서블릿 객체는 **싱글톤으로 관리**
	- 고객의 요청이 올 때 마다 계속 객체(helloServlet)를 생성하는 것은 비효율적임
	- 최초 로딩 시점에 서블릿 객체를 미리 만들어두고 재활용하면 됨
	- 모든 고객 요청은 동일한 서블릿 객체 인스턴스에 접근하면 됨
	- **공유 변수 사용 주의 필요함**
	- 서블릿 컨테이너 종료시에 함께 종료됨
- JSP도 서블릿으로 변환되어서 사용됨
- 동시 요청을 위한 `멀티 쓰레드 처리` 지원
	- *서블릿을 지원하는 WAS의 가장 큰 특징*


## 동시 요청 - 멀티 쓰레드

![[Pasted image 20250418004628.png]]
- 웹 브라우저나 특정 클라이언트에서 서버로 요청을 보내면 WAS 서블릿이 응답을 하게 됨
	- 또한 요청을 보내면 TCP/IP 커넥션 연결이 되게 됨

![[Pasted image 20250418004829.png]]
- 이후 `servlet`을 호출해줌
	- 그런데 누가?

![[Pasted image 20250418004921.png]]
- 서블릿 객체를 호출하는 애는 바로 `쓰레드` 이다.

#### 쓰레드
- 애플리케이션 코드를 하나하나 순차적으로 실행하는 것이 바로 쓰레드
- 자바 메인 메서드를 처음 실행하면 main 이라는 이름의 쓰레드가 실행됨
- 쓰레드가 없다면 자바 애플리케이션 실행이 불가능함
- 쓰레드는 한 번에 하나의 코드 라인만 수행함
- 동시 처리가 필요하면 쓰레드를 추가로 생성함

#### 단일 요청 - 쓰레드 하나 사용 (1)
![[Pasted image 20250418005223.png]]
- 쓰레드가 하나인 상황을 생각해보자.
- 웹 브라우저나 클라이언트로부터 요청이 오게되면

#### 단일 요청 - 쓰레드 하나 사용 (2)
![[Pasted image 20250418010448.png]]
- 요청이 오게되면 쓰레드를 할당하게 되고 쓰레드가 서블릿을 호출하는 구조인 것임

#### 단일 요청 - 쓰레드 하나 사용 (3)
![[Pasted image 20250418010557.png]]
- 이후 쓰레드를 통해서 응답까지 보낸 뒤

#### 단일 요청 - 쓰레드 하나 사용 (4)
![[Pasted image 20250418010619.png]]
- 그때 쓰레드는 휴식 상태에 들어가게 됨


#### 다중 요청 - 쓰레드 하나 사용 (1)
![[Pasted image 20250418010657.png]]
- 요청 1번에 대해서 쓰레드를 이용해서 처리를 시작함
- 만약 여기서 모종의 이유로 처리가 지연된다면?

#### 다중 요청 - 쓰레드 하나 사용 (2)
![[Pasted image 20250418010805.png]]

- 이 상황에서 요청 2가 들어오게 되면 쓰레드가 남아있지 않아서 처리할 수 없는 상황에 처하게 됨
- 결국 요청 2는 하염없이 기다리게 되고

#### 다중 요청 - 쓰레드 하나 사용 (3)
![[Pasted image 20250418010905.png]]
- 결국 두 요청 모두 뻗어버리게 될 수도 있음
- 요청 1의 경우 지연되어서 타임아웃이 나버리고, 요청 2는 요청 1의 작업이 끝나고 반환하는 쓰레드를 받아와야 하는데 그러지 못해서 뻗어버리게 되는 것


#### 요청마다 쓰레드 생성 (다중 요청 - 쓰레드 여러개 사용) (1)
![[Pasted image 20250418011057.png]]
- 해당 문제를 가장 간단하게 해결하는 방법은 쓰레드를 여러 개 사용하는 것
- 지연과는 관계 없이, **요청이 들어올 때 마다 쓰레드를 생성!**

**해당 방법의 장단점**
- 장점
	- 동시 요청을 처리할 수 있음
	- 리소스(CPU, 메모리)가 허용할 때 까지 처리 가능
	- 하나의 쓰레드가 지연되어도 나머지 쓰레드는 정상 동작함
- 단점
	- 쓰레드의 생성 비용은 상당히 비쌈
		- 고객의 요청이 올 때 마다 쓰레드를 생성하면 응답 속도가 늦어지게 됨
	- 쓰레드는 컨텍스트 스위칭 비용도 발생함
		- `Context Switching`: 쓰레드는 CPU의 코어 수만큼 동작하게 되는데, *코어 하나가 두 개 이상의 쓰레드를 동시에 수행할 수 없음*
		- 아주 찰나의 시간에 수행되기 때문에 동시에 수행한다고 착각할 수 있으나, 실제로는 그렇지 않음
		- 따라서 코어가 수행 중인 쓰레드를 변경하는 것, 다음 쓰레드를 실행하는 것에 대한 비용 발생을 `Context Switching` 이라고 함
	- 쓰레드 생성에 제한이 없다
		- 고객 요청이 너무 많이 오면 CPU, 메모리 등의 임계점을 넘어서 서버가 죽을 수도 있음

**이러한 단점들을 해결하기 위해서 보통 WAS들은 다음과 같이 구현되어 있음**

#### 쓰레드 풀 (1)
![[Pasted image 20250418011856.png]]
- 내부에서 `쓰레드 풀`이라는 것을 사용하게끔 구현되어 있음
- 쓰레드 풀 안에는 미리 만들어진 쓰레드들이 존재함
- 각 요청마다 쓰레드 풀에서 쓰레드를 꺼내서 사용하고 해당 요청이 종료되면 쓰레드를 죽이는 것이 아니라 쓰레드 풀에 다시 반납하는 방식

#### 쓰레드 풀 (2)
![[Pasted image 20250418012057.png]]
- 이렇게 했을 때 장점은, 서버의 쓰레드 임계값 보다 더 많은 요청이 들어와도 서버를 다운시키지 않게 `대기` 또는 `거절` 등의 응답을 보낼 수 있다는 것

#### 쓰레드 풀 (3)
**요청마다 쓰레드 생성하는 방식의 단점을 보완한..**
- 특징
	- 필요한 쓰레드를 쓰레드 풀에 보관하고 관리함
	- 쓰레드 풀에 생성 가능한 쓰레드의 최대치를 관리함
		- 톰캣은 최대 200개가 기본 설정 (변경 가능)
			- `tomcat max connection`, `spring boot max connection` ... `검색`
- 사용
	- 쓰레드가 필요하면, 이미 생성되어 있는 쓰레드를 쓰레드 풀에서 꺼내서 사용함
	- 사용을 종료하면 쓰레드 풀에 해당 쓰레드를 반납함
	- 최대 쓰레드가 모두 사용중이어서 쓰레드 풀에 쓰레드가 없으면?
		- 기다리고 있는 요청에 대해서 거절하거나 특정 숫자만큼 대기하도록 설정할 수 있음
- 장점
	- 쓰레드가 미리 생성되어 있으므로, 쓰레드를 생성하고 종료하는 비용(CPU)이 절약되고 응답 시간이 빠름
	- 생성 가능한 쓰레드의 최대치가 있으므로 너무 많은 요청이 들어와도 기존 요청은 안전하게 처리할 수 있음

#### 쓰레드 풀 (4)
**실무 팁**

- WAS의 주요 튜닝 포인트는 최대 쓰레드(max thread) 수이다.
	- 이 값을 너무 낮게 설정하면?
		- 동시 요청이 많을 때, 서버 리소스는 여유롭지만 클라이언트는 잦은 응답 지연을 받게 됨
	- 이 값을 너무 높게 설정하면?
		- 동시 요청이 많을 때, CPU와 메모리 리소스 임계점 초과로 서버가 다운될 수 있음
	- 장애 발생시에는?
		- 클라우드면 일단 서버부터 늘리고 이후에 튜닝하는 선택지
		- 클라우드가 아니라면 열심히 튜닝하면 됨


#### 쓰레드 풀 - 너무 낮게 설정
![[Pasted image 20250418014020.png]]
- 최대 쓰레드가 10개인데, 100개의 요청이 동시에 들어온다면?
- 90개의 요청이 대기하거나 거절당함
- 고객 서비스에 장애 발생
- 심지어 CPU 사용률이 5% 라는건 개발자가 세팅을 잘못한 것임을 시사
	- 못해도 50%는 써줘야 함

- 반대로 너무 높게 설정한다면?
	- 동시에 많은 요청이 몰리게 되고 CPU 메모리 리소스가 임계점 초과로 서버가 다운되어버림

#### 쓰레드 풀의 적정 숫자
- 적정 숫자는 어떻게 찾을 수 있을까?
	- 단순히 어디가 몇개 쓰고 있으니 참고해서 몇개 쓰자 라는 걸로 정의할 수는 없음
- 애플리케이션 로직의 복잡도, CPU, 메모리, IO 리소스 상황에 따라 모두 다름
- 결론은 잦은 성능 테스트가 필요함
	- 최대한 실제 서비스와 유사하게 성능 테스트를 시도
	- 툴: 아파치 ab, 제이미터, nGrinder


#### WAS의 멀티 쓰레드 지원
**이것이 핵심**
- 멀티 쓰레드에 대한 부분은 WAS가 처리
- **개발자가 멀티 쓰레드 관련 코드를 신경쓰지 않아도 됨**
- 개발자는 마치 **싱글 쓰레드 프로그래밍을 하듯이 편리하게 소스 코드를 개발하면 됨**
- 멀티 쓰레드 환경이므로 싱글톤 객체(서블릿, 스프링 빈)는 주의해서 사용해야 함

## HTML, HTTP API, CSR, SSR

#### 정적 리소스
- 고정된 HTML 파일, CSS, JS, 이미지, 영상 등을 제공함
- 주로 웹 브라우저들이 요청을 함
![[Pasted image 20250418140943.png]]

#### HTML 페이지
- 동적으로 필요한 HTML 파일을 생성해서 전달함
- 웹 브라우저는 HTML을 해석해서 클라이언트에게 보여줌
![[Pasted image 20250418141122.png]]


#### HTTP API (1)
- HTML이 아니라 데이터를 전달
- 주로 JSON 형식을 사용함
- 다양한 시스템에서 호출함
![[Pasted image 20250418141232.png]]

#### HTTP API (2)
- 다양한 시스템에서 호출함
	- 데이터만 주고받음
	- 만약 UI 화면이 필요하다면 클라이언트가 별도로 처리해주어야 함
	- 앱, 웹 클라이언트, 서버 to 서버
![[Pasted image 20250418141548.png]]

#### HTTP API (3)
**다양한 시스템 연동**

- 주로 JSON 형태로 데이터 통신
- UI 클라이언트 접점
	- 앱 클라이언트(아이폰, 안드로이드, PC 앱)
	- 웹 브라우저에서 자바스크립트를 통한 HTTP API 호출
	- React, Vue.js 같은 웹 클라이언트
- 서버 to 서버
	- 주문 서버 -> 결제 서버
	- 기업간 데이터 통신


#### 서버사이드 렌더링, 클라이언트 사이드 렌더링
- **SSR - 서버 사이드 렌더링**
	- HTML 최종 결과를 서버에서 만들어서 웹 브라우저에게 전달함
	- 주로 정적인 화면에 사용
	- 관련 기술: JSP, 타임리프 -> 백엔드 개발자의 정석
- **CSR - 클라이언트 사이드 렌더링**
	- HTML 결과를 자바스크립트를 사용해 웹 브라우저에서 동적으로 생성해서 적용함
	- 주로 동적인 화면에 사용, 웹 환경을 마치 앱처럼 필요한 부분을 변경할 수 있음
	- 예) 구글 지도, Gmail, 구글 캘린더
	- 관련 기술: React, Vue.js -> 웹 프론트엔드 개발자
- 참고
	- React, Vue.js를 CSR + SSR 동시에 지원하는 웹 프레임워크도 있음
	- SSR을 사용하더라도, 자바스크립트를 사용해서 화면 일부를 동적으로 변경 가능

#### SSR - 서버 사이드 렌더링
**서버에서 최종 HTML을 생성해서 클라이언트에게 전달**
![[Pasted image 20250418142321.png]]

#### CSR - 클라이언트 사이드 렌더링
![[Pasted image 20250418142350.png]]


#### 어디까지 알아야 할까?
**백엔드 개발자 입장에서의 UI 기술**
- **백엔드 - 서버 사이드 렌더링 기술**
	- JSP, **타임리프**
	- 화면이 정적이고, 복잡하지 않을 때 사용
	- 백엔드 개발자는 서버 사이드 렌더링 기술을 **필수로 학습해야함**
- **웹 프론트엔드 - 클라이언트 사이드 렌더링 기술**
	- React, Vue.js
	- 복잡하고 동적인 UI 사용
	- 웹 프론트 엔드 개발자의 전문 분야
- **선택과 집중**
	- 백엔드 개발자의 웹 프론트엔드 기술 학습은 어디까지나 **옵션**
	- 백엔드 개발자는 서버, DB, 인프라 등등 수 많은 백엔드 기술을 공부해야 함
	- 웹 프론트엔드도 깊이 있게 잘 하려면 오랜 시간이 필요함


## 자바 백엔드 웹 기술 역사
**과거 기술**

- 서블릿 - 1997
	- 개발자들이 TCP/IP 연결하고 멀티쓰레드 고민하고.. 어려움이 많아서 대두된 기술
	- *단, 자바 코드로 작성해야 되기 때문에 동적인 HTML 생성이 어려움*
- JSP - 1999
	- 서블릿의 단점을 보완.
	- 자바 코드로 작성된 JSP는 최종적으로 서블릿으로 변환됨
	- *HTML 생성은 편리하지만, 비즈니스 로직까지 파일에 담다보니 너무 많은 역할을 담당하게 되는 문제점 발생*
		- JSP 파일 하나에 코드가 수 천줄.. 유지보수가 완전 헬..
- 서블릿, JSP 조합 MVC 패턴 사용
	- 모델, 뷰, 컨트롤러로 역할을 나누어 개발 시작
- MVC 프레임워크 춘추 전국 시대 - 2000년 초 ~ 2010년 초
	- MVC 패턴 자동화, 복잡한 웹 기술을 편리하게 사용할 수 있는 다양한 기능 지원
	- 스트럿츠, 웹 워크, 스프링 MVC(과거 버전)


#### 현재 사용 기술
- **애노테이션 기반의 스프링 MVC 등장**
	- `@Controller`
	-  MVC 프레임워크의 춘추 전국 시대를 마무리함
- **스프링 부트의 등장 
	- 스프링 부트는 서버를 내장하고 있음 (과거엔 직접 설치-실행 했어야 함, 빌드는 따로 서버는 따로.. 비효율적)
	- 과거에는 서버에 WAS를 직접 설치하고, 소스는 War 파일을 만들어서 설치한 WAS에 배포하는 방식이었음
	- 스프링 부트는 빌드 결과(Jar)에 WAS 서버 포함 -> 빌드 배포 단순화

#### 최신 기술
**스프링 웹 기술의 분화**
- Web Servlet - Spring MVC
- Web Reactive - Spring WebFlux

> 참고: Spring WebFlux는 비교적 최신 기술
#### 스프링 웹 플럭스
- 특징
	- 완전한 비동기 넌 블러킹 처리
	- 최소 쓰레드로 최대 성능 추구 - 쓰레드 컨텍스트 스위칭 비용 효율화
	- 함수형 스타일로 개발 - 동시처리 코드 효율화
	- 서블릿 기술 사용 X
- 그런데
	- 웹 플럭스는 기술적 난이도 매우 높음
	- 아직은 RDB 지원이 부족함
	- 일반 MVC의 쓰레드 모델도 충분히 빠르다.
	- 실무에서 아직 많이 사용하지 않음 (전체의 1% 이하?..)


#### 자바 뷰 템플릿 역사
**HTML을 백엔드에서 동적으로 편리하게 생성하는 뷰 기능**

- JSP
	- 속도 느림, 기능 부족
- 프리마커(Freemarker), Velocity(벨로시티)
	- 속도 문제 해결, 다양한 기능
- 타임리프(Thymeleaf)
	- 내추럴 템플릿: HTML의 모양을 유지하면서 뷰 템플릿 적용 가능
	- 스프링 MVC와 강력한 기능 통합
	- **최선의 선택,** 단 성능은 프리마커, 벨로시티가 더 빠름


# 섹션 3. 서블릿

## 프로젝스 생성
`start.spring.io`
![[Pasted image 20250419184508.png]]

![[Pasted image 20250420001131.png]]
- 이렇게 해야 실행 속도가 빨라진다고 함

![[Pasted image 20250420001328.png]]
- 롬복 사용시 필수 세팅(?)

## Hello 서블릿
스프링 부트 환경에서 서블릿을 등록하고 사용해보자.

> **참고**
> 서블릿은 톰캣 같은 웹 애플리케이션 서버를 직접 설치하고 그 위에 서블릿 코드를 클래스 파일로 빌드해서 올린 다음 톰캣 서버를 실행하면 된다.
> 하지만 이 과정은 매우 번거롭다.
> 스프링 부트는 톰캣 서버를 내장하고 있으므로 톰캣 서버 설치 없이 편리하게 서블릿 코드를 실행할 수 있다.

```java
package hello.servlet;  
  
import org.springframework.boot.SpringApplication;  
import org.springframework.boot.autoconfigure.SpringBootApplication;  
import org.springframework.boot.web.servlet.ServletComponentScan;  
  
@ServletComponentScan // 자동으로 패키지 내의 서블릿을 찾은 뒤 실행할 수 있게끔 만들어줌  
@SpringBootApplication  
public class ServletApplication {  
  
    public static void main(String[] args) {  
       SpringApplication.run(ServletApplication.class, args);  
    }  

}
```


```java
package hello.servlet.basic;  
  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
  
@WebServlet(name = "helloServlet", urlPatterns = "/hello")  
public class HelloServlet extends HttpServlet {  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
        System.out.println("HelloServlet.service");  
        System.out.println("request = " + request);  
        System.out.println("response = " + response);  
    }  
}
```

```output
HelloServlet.service
request = org.apache.catalina.connector.RequestFacade@36b2c8c0
response = org.apache.catalina.connector.ResponseFacade@44ce524c
```
- 서버 실행시에 이전에 학습한 로직처럼 동작하는 것을 확인할 수 있음
- `이후 서블릿 컨테이너를 통해서 만들어낸 request, response 객체를 파라미터로 넘기면서 helloServlet 을 실행함`


`http://localhost:8080/hello?username=ryu`
- 쿼리 파라미터를 수정해보자!
- 이걸 꺼내서 사용하려면 어떻게 해야할까?

```java
@WebServlet(name = "helloServlet", urlPatterns = "/hello")  
public class HelloServlet extends HttpServlet {  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
        System.out.println("HelloServlet.service");  
        System.out.println("request = " + request);  
        System.out.println("response = " + response);  
  
        String username = request.getParameter("username");  
        System.out.println("username = " + username);  
    }  
}
```

```output
HelloServlet.service
request = org.apache.catalina.connector.RequestFacade@181bfa51
response = org.apache.catalina.connector.ResponseFacade@16dc1722
username = ryu
```
- `request.getParameter("변수명")` 으로 쉽게 꺼낼 수 있다.

**이번에는 응답 메시지를 보내보자!**
- `HttpServletResponse response` 에다가 넣어줘야 한다.
-  해당 변수에 값을 넣으면, 웹 브라우저에 응답하는 response HTTP 응답 메시지에 데이터가 담겨서 나가게 된다.

```java
@Override  
protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
    System.out.println("HelloServlet.service");  
    System.out.println("request = " + request);  
    System.out.println("response = " + response);  
  
    String username = request.getParameter("username");  
    System.out.println("username = " + username);  
  
    // 아래 두 줄은 ContentType, 즉 Header 정보로 들어감  
    response.setContentType("text/plain"); // 단순 문자  
    response.setCharacterEncoding("UTF-8");  
  
    response.getWriter().write("Hello " + username); // .write()를 사용하면 HTTP 메시지 Body에 데이터가 들어감  
}
```

![[Pasted image 20250421003806.png]]

- 요청
![[Pasted image 20250421003839.png]]
![[Pasted image 20250421004141.png]]

- 응답
![[Pasted image 20250421003859.png]]

**최초의 서블릿 요청 및 응답을 실습해봤다.**
사실 우리가 HTTP 스펙을 직접 다 맞춰서 요청/응답을 만들려면 굉장히 어려울 것임.
따라서 서블릿을 통한다면, 우리가 자주 쓰는 기능들을 굉장히 편리하게 이용할 수 있다는 걸 알 수 있음.

**정리**
- `@WebServlet`: 서블릿 애노테이션
	- name: 서블릿 이름
	- urlPatterns: URL 매핑

HTTP 요청을 통해 매핑된 URL이 호출되면 서블릿 컨테이너는 다음 메서드를 실행한다.
`protected void service(HttpServletRequest request, HttpServletResponse response)`

>**표준 동작**: 서블릿 컨테이너는 반드시 service() 메서드를 호출해서 요청을 처리해야 함.
>이 메서드는 HTTP 요청의 메서드(GET, POST 등)에 따라 내부적으로 doGet(), doPost() 등으로 분기함.
>즉, 서블릿 개발자가 doGet(), doPost() 등을 오버라이드하면 해당 HTTP 메서드에 맞게 자동으로 호출됨
>
>**예외 없음**: 특별한 예외 없이, 모든 HTTP 요청은 이 메서드를 통해 처리됨.
>만약 doGet()이나 doPost()를 오버라이드하지 않으면, 기본 구현(예: 405 Method Not Allowed 에러)이 반환될 뿐, service() 호출 자체가 생략되지는 않음

- 웹 브라우저 실행
	- `http://localhost:8080/hello?username=HelloWorld`
	- 결과: HelloWorld
- 콘솔 실행 결과
```output
HelloServlet.service
request = org.apache.catalina.connector.RequestFacade@181bfa51
response = org.apache.catalina.connector.ResponseFacade@16dc1722
username = HelloWorld
```

#### HTTP 요청 메시지를 로그로 확인하기
다음 설정을 추가하자.
`application.properties`
![[Pasted image 20250422000339.png]]

```output
2025-04-22T00:02:55.634+09:00 DEBUG 20316 --- [servlet] [nio-8080-exec-1] o.a.coyote.http11.Http11InputBuffer      : Before fill(): parsingHeader: [true], parsingRequestLine: [true], parsingRequestLinePhase: [0], parsingRequestLineStart: [0], byteBuffer.position(): [0], byteBuffer.limit(): [0], end: [0]
2025-04-22T00:02:55.634+09:00 DEBUG 20316 --- [servlet] [nio-8080-exec-1] o.a.coyote.http11.Http11InputBuffer      : Received [GET /hello?username=ryuyu HTTP/1.1

Host: localhost:8080
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7

]
HelloServlet.service
request = org.apache.catalina.connector.RequestFacade@51d1d3f4
response = org.apache.catalina.connector.ResponseFacade@2948858f
username = ryuyu

```

>**참고**
>운영 서버에 이렇게 모든 요청 정보를 다 남기면 성능 저하가 발생할 수 있음.
>개발 단계에서만 적용하자
>: 톰캣 내부의 디버깅 로깅 기능, Apache Coyote HTTP/1.1 프로토콜 구현체(`Http11InputBuffer`)


#### 서블릿 컨테이너 동작 방식 설명
**내장 톰캣 서버 생성**
![[Pasted image 20250422000947.png]]

**HTTP 요청, HTTP 응답 메시지**
![[Pasted image 20250422001014.png]]

**웹 애플리케이션 서버의 요청 / 응답 구조**
![[Pasted image 20250422001053.png]]

> 참고
> HTTP 응답에서 Content-Length는 웹 애플리케이션 서버가 자동으로 생성해줌


## HttpServletRequest - 개요
**HttpServletRequest 역할**
HTTP 요청 메시지를 개발자가 직접 파싱해서 사용해도 되지만 매우 불편할 것이다. 서블릿은 개발자가 HTTP 요청 메시지를 편리하게 사용할 수 있도록 개발자 대신에 HTTP 요청 메시지를 파싱한다.
그리고 그 결과를 `HttpServletRequest` 객체에 담아서 제공한다

HttpServletRequest를 사용하면 다음과 같은 HTTP 요청 메시지를 편리하게 조회할 수 있다.

**HTTP 요청 메시지**
```
POST /save HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded

username=ryu&age=20
```

- START LINE
	- HTTP 메소드
	- URL
	- 쿼리 스트링
	- 스키마 프로토콜
- HEADER
	- 헤더 조회
- BODY
	- form 파라미터 형식 조회
	- message body 데이터 직접 조회

HttpServletRequest 객체는 추가로 여러가지 부가 기능도 함께 제공한다
**임시 저장소 기능**
- 해당 HTTP 요청이 시작부터 끝날 때 까지(요청의 생명주기) 유지되는 임시 저장소 기능
	- 저장: `request.setAttribute(name, value)`
		- HTTP 요청 메시지 속 작은 저장소에 저장해서 요청 메시지가 살아있는 동안 꺼내 쓸 수 있게 해줌.
	- 조회: `request.getAttribute(name)`
		- # setAttribute, getAttribute


**세션 관리 기능**
`request.getSession(create: true);`

>**중요**
>HttpServletRequest, HttpServletResponse를 사용할 때 가장 중요한 점은 이 객체들이 HTTP 요청 메시지, HTTP 응답 메시지를 편리하게 사용하도록 도와주는 객체라는 점이다.
>따라서 이 기능에 대해서 깊이 있는 이해를 하려면 **HTTP 스펙이 제공하는 요청, 응답 메시지 객체를 이해해야 한다.**


## HttpServletRequest - 기본 사용법

```java
package hello.servlet.basic.request;  
  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.Cookie;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import javax.sql.rowset.serial.SerialException;  
import java.io.IOException;  
import java.util.Enumeration;  
import java.util.Locale;  
  
@WebServlet(name = "requestHeaderServlet", urlPatterns = "/request-header")  
public class RequestHeaderServlet extends HttpServlet {  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        printStartLine(request);  
        printHeaders(request);  
        printHeaderUtils(request);  
    }  

	// Header 정보 조회 기본 
    private static void printStartLine(HttpServletRequest request) {  
        System.out.println("--- REQUEST-LINE - start ---");  
        System.out.println("request.getMethod() = " + request.getMethod()); // GET  
        System.out.println("request.getProtocol() = " + request.getProtocol()); // HTTP/1.1  
        System.out.println("request.getScheme() = " + request.getScheme()); // http\  
        System.out.println("request.getRequestURL() = " + request.getRequestURL()); // http://localhost:8080/request-header  
        System.out.println("request.getRequestURI() = " + request.getRequestURI()); // /request-header  
        System.out.println("request.getQueryString() = " + request.getQueryString()); // username=hi  
        System.out.println("request.isSecure() = " + request.isSecure()); // https 사용 유무  
        System.out.println("--- REQUEST-LINE - end ---");  
        System.out.println();  
    }  
  
    //Header 모든 정보  
    private void printHeaders(HttpServletRequest request) {  
        System.out.println("--- Headers - start ---");  
  
        // 옛날 방식 (?)//        Enumeration<String> headerNames = request.getHeaderNames();  
//        while (headerNames.hasMoreElements()) {  
//            String headerName = headerNames.nextElement();  
//            System.out.println(headerName + " : " + headerName);  
//        }  
  
  
        // 요즘 방식 (?) 람다  
        request.getHeaderNames().asIterator()  
                .forEachRemaining(headerName -> System.out.println(headerName + " : " + headerName));  
  
        System.out.println("--- Headers - end ---");  
        System.out.println();  
    }  
  
    //Header 편리한 조회  
    private void printHeaderUtils(HttpServletRequest request) {  
        System.out.println("--- Header 편의 조회 start ---");  
        System.out.println("[Host 편의 조회]");  
        System.out.println("request.getServerName() = " + request.getServerName()); // Host 헤더  
        System.out.println("request.getServerPort() = " + request.getServerPort()); // Host 헤더  
        System.out.println();  
        System.out.println("[Accept-Language 편의 조회]");  
        Enumeration<Locale> locales = request.getLocales();  
        request.getLocales().asIterator()  
                .forEachRemaining(locale -> System.out.println("locale = " + locale));  
        System.out.println("request.getLocale() = " + request.getLocale()); // 우선순위 가장 높은 언어 꺼내기  
        System.out.println();  
        System.out.println("[cookie 편의 조회]");  
        if (request.getCookies() != null) {  
            for (Cookie cookie : request.getCookies()) {  
                System.out.println(cookie.getName() + ": " + cookie.getValue());  
            }  
        }  
        System.out.println();  
        System.out.println("[Content 편의 조회]");  
        System.out.println("request.getContentType() = " + request.getContentType());  
        System.out.println("request.getContentLength() = " + request.getContentLength());  
        System.out.println("request.getCharacterEncoding() = " + request.getCharacterEncoding());  
        System.out.println("--- Header 편의 조회 end ---");  
        System.out.println();  
    }  
}
```


![[Pasted image 20250424010141.png]]

![[Pasted image 20250424010254.png]]
- text가 잘 담겨서 넘어간 걸 알 수 있음
- 기존에는 null 이었음 (아무 것도 담겨있지 않았기 때문)


	지금까지 `HttpServletRequest`를 통해서 HTTP 메시지의 `start-line`, `header` 정보 조회 방법을 이해했다. 이제 본격적으로 HTTP 요청 데이터를 어떻게 조회하는지 알아보자

## HTTP 요청 데이터 - 개요
HTTP 요청 메시지를 통해 클라이언트에서 서버로 데이터를 전달하는 방법을 알아보자

**주로 다음 3가지 방법을 사용한다.**

- **GET - 쿼리 파라미터**
	- \/url**?username=hello&age=20
	- message body 없이, URL의 쿼리 파라미터에 데이터를 포함해서 전달함
	- 예) 검색, 필터, 페이징 등에서 많이 사용하는 방식

- **POST - HTML Form**
	- content-type: application/x-www-form-urlencoded
	- 메시지 바디에 쿼리 파라미터 형식으로 전달 username=hello&age=20
	- 보면 알겠지만, GET 방식에서 쿼리 파라미터를 사용하는 것과 동일함
	- 예) 회원가입, 상품 주문, HTML Form 사용

- **HTTP message body**에 데이터를 직접 담아서 요청
	- HTTP API에서 주로 사용함. JSON, XML, TEXT 등
	- 데이터 형식은 주로 JSON
	- POST, PUT, PATCH

**POST - HTML Form 예시**
![[Pasted image 20250501191335.png]]

## HTTP 요청 데이터 - GET 쿼리 파라미터
다음 데이터를 클라이언트에서 서버로 전송해보자.
- username=hello
- age=20

메시지 바디 없이, URL의 **쿼리 파라미터**를 사용해서 데이터를 전달해보자.
예) 검색, 필터, 페이징 등에서 많이 사용하는 방식

쿼리 파라미터는 URL에 다음과 같이 `?` 를 시작으로 보낼 수 있다. 추가 파라미터는 `&`로 구분하면 된다.
- `http://localhost:8080/request-param?username=hello&age=20`

서버에서는 `HttpServletRequest`가 제공하는 다음 메서드를 통해서 쿼리 파라미터를 편리하게 조회할 수 있다.

**쿼리 파라미터 조회 메서드**
```java
 // 단일 파라미터 조회
String username = request.getParameter("username");

// 파라미터 이름을 모두 조회
Enumeration<String> parameterNames = request.getParameterNames(); 

// 파라미터를 Map 으로 조회
Map<String, String[]> parameterMap = request.getParameterMap(); 

// 복수 파라미터 조회
String[] usernames = request.getParameterValues("username"); 
```

```java
package hello.servlet.basic.request;  
  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
import java.util.Enumeration;  
  
  
/**  
 * 1. 파라미터 전송 기능  
 * http://localhost:8080/request-param?username=hello&age=20  
 * */@WebServlet(name = "requestParamServlet", urlPatterns = "/request-param")  
public class RequestParamServlet extends HttpServlet {  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
        System.out.println("[전체 파라미터 조회] - start");  
  
        request.getParameterNames().asIterator()  
                .forEachRemaining(paramName -> System.out.println(paramName + " = " + request.getParameter(paramName)));  
  
        System.out.println("[전체 파라미터 조회] - end");  
  
        System.out.println();  
  
        System.out.println("[단일 파라미터 조회] - start");  
  
        String username = request.getParameter("username");  
        String age = request.getParameter("age");  
  
        System.out.println("username = " + username);  
        System.out.println("age = " + age);  
  
        System.out.println("[단일 파라미터 조회] - end");  
  
    }  
}
```

```output
[전체 파라미터 조회] - start
username = ryu
age = 10
oh = real
[전체 파라미터 조회] - end

[단일 파라미터 조회] - start
username = ryu
age = 10
[단일 파라미터 조회] - end
```

그런데, username에 2가지 값을 파라미터로 넘겨줄 수도 있다.
- `http://localhost:8080/request-param?username=ryu&age=10&username=ryu2`

이럴 때는 내부 우선 순위에서 먼저 잡히는 값이 출력될 것이다.

따라서 이름이 같은 복수 파라미터를 조회하는 방법은 다음과 같다.

```java
System.out.println("[이름이 같은 복수 파라미터 조회] - start");  
  
String[] usernames = request.getParameterValues("username");  
for (String name : usernames) {  
    System.out.println("username = " + name);  
}  
  
System.out.println("[이름이 같은 복수 파라미터 조회] - end");
```

- `http://localhost:8080/request-param?username=ryu&age=10&username=ryu2`

```java
[이름이 같은 복수 파라미터 조회] - start
username = ryu
username = ryu2
[이름이 같은 복수 파라미터 조회] - end
```


**복수 파라미터에서 단일 파라미터 조회**
`username=hello&username=kim` 과 같이 `파라미터 이름`은 `하나`인데, `값`이 `중복`이면 어떻게 될까?
`request.getparameter()`는 하나의 파라미터 이름에 대해서 단 하나의 값만 있을 때 사용해야 한다. 지금처럼 중복일 때는 `request.getparameterValues()`를 사용해야 한다.

참고로 이렇게 중복일 때 `request.getParameter()`를 사용하면 `request.getParameterValues()`의 첫 번째 값을 반환하게 된다.

대부분의 상황에서 단일 파라미터로 전송하기 때문에, 복수 파라미터로 보내는 경우가 특수한 경우이고, 이 특수한 경우에 대해서 잘 기억해서 `request.getParameterValues`를 사용해주면 됨. (의도한대로 동작할 수 있도록)

## HTTP 요청 데이터 - POST HTML Form
이번에는 HTML의 Form을 사용해서 클라이언트에서 서버로 데이터를 전송해보자.
주로 회원 가입, 상품 주문 등에서 사용하는 방식이다.

**특징**
- content-type: `application/x-www-form-urlencoded`
- 메시지 바디에 쿼리 파라미터 형식으로 데이터를 전달한다. `username=hello&age=20`

`src/main/webapp/basic/hello-form.html` 생성
```html
<!DOCTYPE html>  
<html>  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
<form action="/request-param" method="post">  
    username: <input type="text" name="username" />  
    age:      <input type="text" name="age" />  
    <button type="submit">전송</button>  
</form>  
</body>  
</html>
```

`http://localhost:8080/basic/hello-form.html` 경로로 접근
![[Pasted image 20250503003234.png]]

![[Pasted image 20250503003426.png]]

![[Pasted image 20250503003452.png]]

이전에 작성한 양식대로 잘 출력되는 것을 확인 가능

단순히 이 주소로 보냈을 뿐임
`<form action="/request-param" method="post">` 

POST의 HTML Form을 전송하면 웹 브라우저는 다음 형식으로 HTTP 메시지를 만든다.
- **요청 URL** : http://localhost:8080/request-param
- **content-type** : application/x-www-form-urlencoded
- **message body** : username = hello&age=20

`application/x-www-form-urlencoded` 형식은 앞서 GET에서 살펴본 쿼리 파라미터 형식과 같다.
따라서 **쿼리 파라미터 조회 메서드(`request.getParameter()`)를 그대로 사용**하면 된다.

클라이언트(웹 브라우저) 입장에서는 두 방식에 차이가 있지만, 서버 입장에서는 둘의 형식이 동일하므로 `request.getparameter()`로 편리하게 구분없이 조회할 수 있다.

정리하면, `request.getParameter()`는 GET URL 쿼리 파라미터 형식도 지원하고, POST HTML Form 형식도 둘 다 지원한다.

> 참고
> content-type은 HTTP 메시지 바디의 데이터 형식을 지정한다. **GET URL 쿼리 파라미터 형식**으로 클라이언트에서 서버로 데이터를 전달할 때는 HTTP 메시지 바디를 사용하지 않기 때문에 content-type이 없다.
> **POST HTML Form 형식**으로 데이터를 전달하면 HTTP 메시지 바디에 해당 데이터를 포함해서 보내기 때문에 바디에 포함된 데이터가 어떤 형식인지 content-type을 꼭 지정해야 한다.
> 
> 이렇게 폼으로 데이터를 전송하는 형식을 `application/x-www-form-urlencoded` 라고 한다.

#### Postman을 사용한 테스트
이런 간단한 테스트에 HTML Form을 만들 필요는 없다. 이때 필요한 것이 Postman
![[Pasted image 20250503004436.png]]

![[Pasted image 20250503004503.png]]


## HTTP 요청 데이터 API 메시지 바디 - 단순 텍스트
- **HTTP message body**에 데이터를 직접 담아서 요청
	- HTTP API에서 주로 사용, JSON, XML, TEXT
	- 데이터 형식은 주로 JSON 사용
	- POST, PUT, PATCH

- 먼저 가장 단순한 텍스트 메시지를 HTTP 메시지 바디에 담아서 전송하고 읽어보자
- HTTP 메시지 바디의 데이터를 InputStream을 사용해서 직접 읽을 수 있다.

**RequestBodyStringServlet**
```java
package hello.servlet.basic.request;  
  
import jakarta.servlet.ServletException;  
import jakarta.servlet.ServletInputStream;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import org.springframework.util.StreamUtils;  
  
import java.io.IOException;  
import java.nio.charset.StandardCharsets;  
  
@WebServlet(name = "requestBodyStringServlet", urlPatterns = "/request-body-string")  
public class RequestBodyStringServlet extends HttpServlet {  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        ServletInputStream inputStream = request.getInputStream(); // 메시지 바디의 내용을 바이트 코드로 얻을 수 있음  
        String messageBody = StreamUtils.copyToString(inputStream, StandardCharsets.UTF_8);// byte <-> 문자 변환 시에는 어떤 인코딩인지 꼭 명시해줘야 함, StreamUtils는 스프링이 제공함  
  
        System.out.println("messageBody = " + messageBody);  
  
        response.getWriter().write("OK");  
    }  
}
```

![[Pasted image 20250503011948.png]]

![[Pasted image 20250503012003.png]]

> **참고**
> inputStream은 byte 코드를 반환한다. byte 코드를 우리가 읽을 수 있는 문자(String)으로 보려면 문자표(Charset)를 지정해주어야 한다. 여기서는 UTF_8 Charset으로 지정해주었다.


**문자 전송**
- POST: http://localhost:8080/request-body-string
- content-type: text/plain
- message body: `hello`
- 결과: `message body = hello`


## HTTP 요청 데이터 - API 메시지 바디 - JSON
이번에는 HTTP API에서 주로 사용하는 JSON 형식으로 데이터를 전달해보자.

**JSON 형식 전송**
- POST http://localhost:8080/request-body-json
- content-type: "application/json"
- message body: `{"username": "hello", "age: 20}`
- 결과: `messageBody = {"username": "hello", "age": 20}`

**JSON 형식 파싱 추가**
JSON 형식으로 파싱할 수 있게 객체를 하나 생성하자
- JSON 형식으로 오는 데이터를 객체 형식으로 변환해서 사용하기 때문

`hello.servlet.basic.HelloData`
```java
package hello.servlet.basic;  
  
import lombok.Getter;  
import lombok.Setter;  
  
  
@Getter @Setter  
public class HelloData {  
  
    private String username;  
    private int age;  
  
}
```

`hello.servlet.basic.request.RequestBodyJsonServlet`
```java
package hello.servlet.basic.request;  
  
import jakarta.servlet.ServletException;  
import jakarta.servlet.ServletInputStream;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import org.springframework.util.StreamUtils;  
  
import java.io.IOException;  
import java.nio.charset.StandardCharsets;  
  
@WebServlet(name = "requestBodyJsonServlet", urlPatterns = "/request-body-json")  
public class RequestBodyJsonServlet extends HttpServlet {  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        ServletInputStream inputStream = request.getInputStream();  
        String messageBody = StreamUtils.copyToString(inputStream, StandardCharsets.UTF_8);  
  
        System.out.println("messageBody = " + messageBody);  
    }  
}
```

**Postman**
![[Pasted image 20250508163643.png]]

**결과**
`messageBody = {"username":"hello}", "age":20}`

정상 작동 하는 것을 알 수 있다.

이번에는 String이 아니라 객체 형식으로 클래스를 변환해서 사용해보자.
- JSON 라이브러리가 필요하다 (스프링부트 기본 내장 라이브러리 `jackson`)

```java
package hello.servlet.basic.request;  
  
import com.fasterxml.jackson.databind.ObjectMapper;  
import hello.servlet.basic.HelloData;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.ServletInputStream;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import org.springframework.util.StreamUtils;  
  
import java.io.IOException;  
import java.nio.charset.StandardCharsets;  
  
@WebServlet(name = "requestBodyJsonServlet", urlPatterns = "/request-body-json")  
public class RequestBodyJsonServlet extends HttpServlet {  
  
    private ObjectMapper objectMapper = new ObjectMapper();  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        ServletInputStream inputStream = request.getInputStream();  
        String messageBody = StreamUtils.copyToString(inputStream, StandardCharsets.UTF_8);  
  
        System.out.println("messageBody = " + messageBody);  
  
  
        HelloData helloData = objectMapper.readValue(messageBody, HelloData.class);  
  
        System.out.println("helloData.username = " + helloData.getUsername());  
        System.out.println("helloData.age = " + helloData.getAge());  
  
        response.getWriter().write("ok");  
    }  
}
```
- `objectMapper.readValue(...)` 를 사용해주면 된다.

```output
messageBody = {"username":"hello", "age":20}
helloData.username = hello}
helloData.age = 20
```

출력문을 참고해보면, `helloData.getUsername()`이 정상 동작을 하는 것을 알 수 있다.
비로소 JSON 형식의 데이터를 객체로 변환한 것!

>**참고**
>JSON 결과를 파싱해서 사용할 수 있는 자바 객체로 변환하려면 Jackson, Gson 같은 JSON 변환 라이브러리를 추가해서 사용해야 한다. 스프링 부트로 Spring MVC를 선택하면 기본적으로 Jackson 라이브러리(`ObjectMapper`)를 함께 제공한다.

>**참고**
>HTML form 데이터도 메시지 바디를 통해 전송되므로 직접 읽을 수 있다. 하지만 편리한 파라미터 조회 기능 (`request.getParameter(...)`)을 이미 제공하기 때문에 파라미터 조회 기능을 사용하면 된다.

>GET 쿼리 파라미터, HTML Form 데이터 (조회)
>`request.getParameter()`
>
>POST HTTP API 메시지 바디 - JSON (조회)
>`request.getInputStream()
>`
>POST HTTP API 메시지 바디 - JSON (객체 변환 시)
>`objectMapper.readValue()`


#### 🔑 **HTTP 요청 데이터 전송 방식 요약**

1️⃣ **GET (쿼리 파라미터 방식)**

- 데이터는 URL에 `?`로 시작해 `&`로 구분해서 전달.
- ex) `/request-param?username=hello&age=20`
- 메시지 바디 없음, content-type 없음.
- 조회 메서드:  
    `request.getParameter()`
    request.getParameterValues()`
    `request.getParameterNames()`

2️⃣ **POST (HTML Form 방식)**

- content-type: `application/x-www-form-urlencoded`
- 메시지 바디: `username=hello&age=20`
- GET과 동일하게 `request.getParameter()`로 조회 가능.
- 폼 전송 시 주로 사용 (회원가입 등).
    

3️⃣ **POST (HTTP 메시지 바디 직접 전달)**

- API에서 주로 사용.
- content-type: JSON (`application/json`), TEXT 등.
- 메시지 바디 직접 읽기:  
    `request.getInputStream()`
- JSON을 객체로 변환:  
    `ObjectMapper.readValue()` (Jackson)

---

### ⚠️ **주의할 점**

- **중복 파라미터**:  
    `username=hello&username=kim` 처럼 중복되면 `request.getParameter()`는 첫 번째 값만 반환. → **반드시** `request.getParameterValues()` 사용.

- **폼 데이터 vs JSON 데이터**:  
    HTML Form은 쿼리 파라미터 방식과 메시지 형식이 같아서 `getParameter()`로 편하게 조회.  
    JSON은 `getParameter()`로 조회 불가 → 반드시 InputStream으로 읽어야 함.

- **인코딩**:  
    InputStream을 문자열로 바꿀 때는 인코딩(UTF-8 등)을 꼭 지정해야 함.

>**참고**
>서블릿이 하는 일?

- HTTP 요청을 받아서:
    - 요청 데이터 읽고 (`HttpServletRequest`)
    - 원하는 로직 실행하고 (DB 조회, 계산 등)
    - 응답 만들어서 (`HttpServletResponse`)
    - 다시 클라이언트로 돌려보내는 것

즉, **웹 요청 -> 응답** 전체 과정을 담당하는 애라고 보면 됨


## HttpServletResponse - 기본 사용법

#### HttpServletResponse 역할

**HTTP 응답 메시지 생성**
- HTTP 응답 코드 지정 (200, 400, 500, 401, 404 ...)
- Content-Header 생성
- Content-Body 생성

**편의 기능 제공**
- Content-Type, 쿠키, Redirect

`hello.servlet.basic.response.ResponseHeaderServlet`
```java
package hello.servlet.basic.response;  
  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
import java.io.PrintWriter;  
  
@WebServlet(name = "responseHeaderServlet", urlPatterns = "/response-header")  
public class ResponseHeaderServlet extends HttpServlet {  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
        // [status-line] | 응답 코드 세팅  
        response.setStatus(HttpServletResponse.SC_OK); // 응답 코드를 숫자 대신 상수를 넣어주는 것이 좋음 (매직 넘버 방지)  
  
        // [response-header] | 컨텐츠 헤더 세팅  
        response.setHeader("Content-Type", "text/plain;charset=utf-8");  
        response.setHeader("Cache-Control", "no-cache, no-store, must-revalidate"); // 캐시 완전 무효화  
        response.setHeader("Pragma", "no-cache"); // 과거 버전 전용 캐시 무효화 (HTTP 강의 참고)  
        response.setHeader("my-header", "hello"); // 커스텀 헤더도 만들 수 있음  
  
        PrintWriter writer = response.getWriter();  
        writer.println("ok");  
    }  
}
```

![[Pasted image 20250508185446.png]]
- `Response Header` 부분을 참고해보면 설정한대로 잘 반영된 걸 알 수 있음

**만약 응답 코드를 다르게 설정한다면?**
```java
// [status-line] | 응답 코드 세팅  
response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
// 응답 코드를 숫자 대신 상수를 넣어주는 것이 좋음 (매직 넘버 방지)
```

![[Pasted image 20250508185642.png]]
- 잘 반영되는 것을 알 수 있음

**편의 메서드 추가**
```java
package hello.servlet.basic.response;  
  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.Cookie;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
import java.io.PrintWriter;  
  
@WebServlet(name = "responseHeaderServlet", urlPatterns = "/response-header")  
public class ResponseHeaderServlet extends HttpServlet {  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
        // [status-line] | 응답 코드 세팅  
        response.setStatus(HttpServletResponse.SC_OK); // 응답 코드를 숫자 대신 상수를 넣어주는 것이 좋음 (매직 넘버 방지)  
  
        // [response-header] | 컨텐츠 헤더 세팅  
        // response.setHeader("Content-Type", "text/plain;charset=utf-8");  
        response.setHeader("Cache-Control", "no-cache, no-store, must-revalidate"); // 캐시 완전 무효화  
        response.setHeader("Pragma", "no-cache"); // 과거 버전 전용 캐시 무효화 (HTTP 강의 참고)  
        response.setHeader("my-header", "hello"); // 커스텀 헤더도 만들 수 있음  
  
        // [Header 편의 메서드]  
        content(response);  
        cookie(response);  
        redirect(response);  
  
        PrintWriter writer = response.getWriter();  
        writer.println("ok");  
    }  
  
    private void content(HttpServletResponse response) {  
        // Content-Type: text/plain;charset=utf-8  
        // Content-Length: 2        // response.setHeader("Content-Type", "text/plain;charset=utf-8");        response.setContentType("text/plain"); // 기존 코드 대체 가능 (response.setHeader("..."))        response.setCharacterEncoding("utf-8"); // 기존 코드 대체 가능 (response.setHeader("..."))        // response.setContentLength(2); // 생략시에는 자동 생성됨  
    }  
  
    private void cookie(HttpServletResponse response) {  
        // Set-Cookie: myCookie=good; Max-Age=600;  
        // response.setHeader("Set-Cookie", "myCookie=good; Max-Age=600");        Cookie cookie = new Cookie("myCookie", "good");  
        cookie.setMaxAge(600);  
        response.addCookie(cookie); // response 에 쿠키 삽입 가능  
    }  
  
    private void redirect(HttpServletResponse response) throws IOException {  
        // Status Code  302  
        // Location: /basic/hello-form.html  
        // response.setStatus(HttpServletResponse.SC_FOUND); // 302        // response.setHeader("Location", "/basic/hello-form.html");        response.sendRedirect("/basic/hello-form.html");  
    }  
}
```
- `ContentType`, `Cookie`를 직접 지정하는 방법 말고 메서드를 이용해서도 가능함


![[Pasted image 20250508225947.png]]
- `Set-Cookie` 가 설정되었으니 다시 요청해보면

![[Pasted image 20250508225913.png]]
- 쿠키가 잘 저장된 것을 확인할 수 있음

>클라이언트 -(쿠키 없이 요청)-> 서버
>서버 -(Set-Cookie를 헤더에 담아서 응답)-> 클라이언트
>클라이언트 -(쿠키 담아서 재요청)-> 서버

![[Pasted image 20250508230715.png]]
- `redirect`도 가능함

![[Pasted image 20250508230854.png]]
- 첫 요청에서 302를 반환해주며 리다이렉트, 리다이렉트 된 페이지에서는 200이 반환됨

![[Pasted image 20250508230734.png]]

**메시지 바디 편의 메서드**

```java
@WebServlet(name = "responseHeaderServlet", urlPatterns = "/response-header")  
public class ResponseHeaderServlet extends HttpServlet {  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
        // [status-line] | 응답 코드 세팅  
        response.setStatus(HttpServletResponse.SC_OK); // 응답 코드를 숫자 대신 상수를 넣어주는 것이 좋음 (매직 넘버 방지)  
  
        // [response-header] | 컨텐츠 헤더 세팅  
        // response.setHeader("Content-Type", "text/plain;charset=utf-8");  
        response.setHeader("Cache-Control", "no-cache, no-store, must-revalidate"); // 캐시 완전 무효화  
        response.setHeader("Pragma", "no-cache"); // 과거 버전 전용 캐시 무효화 (HTTP 강의 참고)  
        response.setHeader("my-header", "hello"); // 커스텀 헤더도 만들 수 있음  
  
        // [Header 편의 메서드]  
        content(response);  
        cookie(response);  
        redirect(response);  
  
        PrintWriter writer = response.getWriter();  
        writer.println("ok");  
          
        // [message body]  
        PrintWriter writer1 = response.getWriter();  
        writer1.println("ok");  
    }
```
- \[message body] 부분을 참고해보면, `response.getWriter()` 또는 `response.getInputStream()` 을 통해서 원하는 내용을 메시지 바디에 넣을 수 있게됨


## HTTP 응답 데이터 - 단순 텍스트, HTML
**HTTP 응답 메시지는 주로 다음 내용을 담아서 전달한다.**

- 단순 텍스트 응답
	- 앞에서 이미 살펴봄 (`writer.println("ok");`)
- HTML 응답
- HTTP API - MessageBody JSON 응답 

**hello.servlet.web.response.ResponseHtmlServlet**
```java
package hello.servlet.basic.response;  
  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
import java.io.PrintWriter;  
  
@WebServlet(name = "responseHtmlServlet", urlPatterns = "/response-html")  
public class ResponseHtmlServlet extends HttpServlet {  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        // Content-Type: text/html;charset=utf-8  
        response.setContentType("text/html");  
        response.setCharacterEncoding("UTF-8");  
  
        PrintWriter writer = response.getWriter();  
  
        writer.println("<html>");  
        writer.println("<body>");  
        writer.println("<div>안녕하시렵니까</div>");  
        writer.println("</html>");  
        writer.println("</body>");  
  
    }  
}
```

![[Pasted image 20250508232237.png]]'

![[Pasted image 20250508232305.png]]

## HTTP 응답 데이터 - API JSON
응답 데이터를 JSON 형식으로 보내는 방법

**hello.servlet.web.response.ResponseJsonServlet**
![[Pasted image 20250509002545.png]]

![[Pasted image 20250509002557.png]]

- HTTP 응답으로 JSON을 반환할 때는 content-type을 `application/json`으로 지정해야 한다.
- Jackson 라이브러리가 제공하는 `objectMapper.writeValueAsString()`을 사용하면 객체를 JSON 문자로 변경할 수 있다.

> 참고
> `application/json`은 스펙상 utf-8 형식을 사용하도록 정의되어 있다.
> 그래서 스펙에서 charset=utf-8과 같은 추가 파라미터를 지원하지는 않는다.
> 따라서 `application/json`이라고만 사용해야지, `application/json;charset=utf-8` 이라고 전달하는 것은 의미 없는 파라미터를 추가한 것이 된다.
> response.getWriter()를 사용하면 추가 파라미터를 자동으로 추가해준다. 이때는 response.getOutputStream()으로 출력하면 그런 문제가 없다.

## 정리
### 서블릿이 HTTP 요청/응답 처리와 관련하여 주로 어떤 역할을 하는 걸까요?
1. HTTP 요청/응답 서버 구현
2. 웹 브라우저 화면 디자인
3. 데이터베이스 정보 저장
4. 자바 애플리케이션 독립 실행

해설
1. 서블릿은 서버에서 HTTP 요청 메시지를 파싱하고, 필요한 비즈니스 로직을 처리한 후, HTTP 응답 메시지를 만들어 클라이언트에 되돌려주는 핵심 역할을 합니다. 개발자가 편리하게 웹 서비스 요청/응답을 다루게 돕죠.

### 스프링 부트에서 별도의 웹 서버 설치 없이 서블릿을 실행할 수 있어 편리한 주된 기능은 무엇인가요?

1. 보안 기능 자동 적용
2. 내장형 톰캣 서버 제공
3. 자동 코드 생성 지원
4. 데이터베이스 연결 자동 설정

해설
2. 스프링 부트는 내장형 톰캣 서버를 기본으로 포함하고 있어, 복잡한 웹 서버 설정 과정 없이 서블릿 코드를 바로 실행하고 테스트하는 환경을 편리하게 제공합니다. 개발 생산성을 높여주죠.

### `HttpServletRequest` 객체를 사용하는 주된 목적은 무엇일까요?

1. HTTP 요청 메시지 편리하게 읽기
2. 웹 애플리케이션 보안 강화
3. 서버에서 데이터 임시 저장
4. HTTP 응답 메시지 생성

해설
1. 개발자가 HTTP 요청 메시지의 시작 라인, 헤더, 바디 데이터를 직접 파싱하는 번거로움 없이, `HttpServletRequest` 객체를 통해 표준화된 방법으로 정보를 쉽게 얻도록 돕습니다.


### 클라이언트가 서버로 데이터를 전송할 때, 일반적으로 HTTP 메시지 '바디'에 데이터를 포함시키지 않는 방식은 무엇인가요?

1. PUT 방식 (JSON API)
2. POST 방식 (JSON API)
3. GET 방식 (쿼리 파라미터)
4. POST 방식 (HTML Form)

해설
3. GET 방식의 쿼리 파라미터는 URL 자체에 데이터를 '키=값' 형태로 포함시켜 전송합니다. 반면, POST, PUT, PATCH 등의 방식은 주로 데이터를 HTTP 메시지 바디에 담아 보냅니다.

### `request.getParameter()` 메소드가 GET 방식 쿼리 파라미터와 POST 방식 HTML Form 데이터를 모두 읽을 수 있는 이유는 무엇일까요?

1. 서버가 요청 방식 자동 변환
2. 모든 데이터 처리하도록 설계
3. 두 방식 모두 암호화 사용
4. 데이터 형식이 '키=값'으로 유사

해설
4. GET 쿼리 파라미터와 POST HTML Form 데이터 모두 '키=값' 형태의 URL 인코딩 방식을 사용합니다. 따라서 서버 입장에서는 데이터 형식이 같으므로 동일한 `request.getParameter()` 메소드로 편리하게 접근할 수 있습니다.


### 서버 간 통신, 모바일 앱 통신 등에서 HTTP 메시지 바디에 직접 데이터를 담아 전송할 때 주로 사용되는 HTTP 메소드는 무엇일까요?

1. GET, HEAD
2. POST, PUT, PATCH
3. TRACE, CONNECT
4. DELETE, OPTIONS

해설
2. API 통신에서 HTTP 메시지 바디에 JSON 등의 데이터를 담아 보낼 때는 주로 리소스 생성(POST), 전체 업데이트(PUT), 부분 업데이트(PATCH) 등의 의미를 가지는 메소드를 사용합니다.


### 서버 측에서 수신한 JSON 형식 HTTP 메시지 바디 데이터를 편리하게 자바 객체로 변환하기 위해 필요한 것은 무엇일까요?

1. 데이터베이스 드라이버
2. 내장형 웹 서버
3. JSON 파싱 라이브러리
4. 별도의 웹 프레임워크

해설
3. HTTP 메시지 바디의 JSON 데이터는 단순 텍스트 형태이므로, 이를 자바 객체 필드에 자동으로 매핑해주는 Jackson과 같은 JSON 파싱 전용 라이브러리가 서버 애플리케이션에 필요합니다.


### 서블릿에서 클라이언트로 보내는 HTTP 응답 메시지의 상태 코드(예: 200 OK, 404 Not Found)를 설정하는 메소드는 무엇일까요?

1. `response.setContentType()`
2. `response.getWriter()`
3. `response.setHeader()`
4. `response.setStatus()`

해설
4. HTTP 응답의 상태 코드는 요청 처리 결과를 나타내며, `response.setStatus()` 메소드를 사용하여 200(성공), 400(잘못된 요청), 404(찾을 수 없음) 등의 코드를 설정할 수 있습니다.

### HTTP 응답으로 텍스트나 HTML 콘텐츠를 보낼 때, `UTF-8`과 같은 문자 인코딩을 올바르게 설정하는 것이 중요한 주된 이유는 무엇일까요?

1. 응답 메시지 크기 축소
2. 응답 속도 향상
3. 서버 부하 감소
4. 문자 깨짐 없이 올바르게 표시

해설
4. 응답 데이터의 문자 인코딩을 명확히 지정하지 않으면, 클라이언트 브라우저가 서버의 의도와 다르게 문자를 해석하여 '깨짐' 현상이 발생할 수 있습니다. 특히 다양한 언어 사용 시 중요합니다.

### HTTP 응답 메시지 바디에 JSON 형식 데이터를 담아 보낼 때, 응답 헤더에 설정해야 하는 Content-Type 값은 무엇일까요?

1. `text/plain`
2. `application/x-www-form-urlencoded`
3. `text/html`
4. `application/json`

해설
클라이언트에게 응답 메시지 바디에 담긴 데이터의 형식이 JSON임을 알려주기 위해 `Content-Type` 헤더를 `application/json`으로 설정해야 합니다. 이는 표준 명세에 정의되어 있습니다.
- `text/plain` -> HTTP message body에 직접 담을 때 (순수 텍스트 데이터)
- `application/x-www-form-urlencoded` -> HTML Form 데이터 (POST), 주로 요청 바디에 들어감.
- `text/html` -> HTTP message body에 직접 담을 때 (HTML 페이지)


# 섹션 4. 서블릿, JSP, MVC 패턴

## 회원 관리 웹 애플리케이션 요구사항
- 서블릿으로 개발 후 불편한 점 알아보고 JSP로 개발
- JSP로 개발 후 불편한 점 알아보고 MVC 패턴으로 개발
- 최종적으로 MVC 패턴으로 모든 문제를 해결해보자.

**회원 정보**
이름: `username`
나이: `age`

**기능 요구사항**
- 회원 저장
- 회원 목록 조회

**회원 도메인 모델**

`hello.servlet.domain.member.Member`
```java
package hello.servlet.domain.member;  
  
import lombok.Getter;  
import lombok.Setter;  
  
@Getter @Setter  
public class Member {  
  
    private Long id;  
    private String username;  
    private int age;  
  
    public Member() { }  
  
    public Member(String username, int age) {  
        this.username = username;  
        this.age = age;  
    }  
  
  
}
```

`hello.servlet.domain.member.MemberRepository`
```java
package hello.servlet.domain.member;  
  
import java.util.ArrayList;  
import java.util.HashMap;  
import java.util.List;  
import java.util.Map;  
  
/**  
 * 동시성 문제가 고려되어 있지 않음.  
 * 실무에서는 ConcurrentHashMap, AtomicLong의 사용을 고려해야 함.  
 */public class MemberRepository {  
  
    private static Map<Long, Member> store = new HashMap<>();  
    private static long sequence = 0L;  
  
    private static final MemberRepository instance = new MemberRepository();  
  
    public static MemberRepository getInstance() {  
        return instance;  
    }  
  
    private MemberRepository() {  
  
    }  
  
    public Member save(Member member) {  
        member.setId(++sequence);  
        store.put(member.getId(), member);  
        return member;  
    }  
  
    public Member findById(long id) {  
        return store.get(id);  
    }  
  
    public List<Member> findAll() {  
        return new ArrayList<>(store.values()); // 얕은 복사  
    }  
  
    public void clearStore() {  
        store.clear();  
    }  
}
```


`test.java.hello.servlet.domain.member.MemberRepositoryTest`
```java
package hello.servlet.domain.member;  
  
import org.assertj.core.api.Assertions;  
import org.junit.jupiter.api.AfterEach;  
import org.junit.jupiter.api.Test;  
  
import java.util.List;  
  
class MemberRepositoryTest {  
  
    MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @AfterEach  
    void afterEach() {  
        memberRepository.clearStore();  
    }  
  
    @Test  
    void save() {  
        // given  
        Member member = new Member("hello", 20);  
  
        // when  
        Member savedMember = memberRepository.save(member);  
  
        // then  
        Member findMember = memberRepository.findById(savedMember.getId());  
        Assertions.assertThat(findMember).isEqualTo(savedMember);  
    }  
  
    @Test  
    void findAll() {  
        // given  
        Member member1 = new Member("member1", 20);  
        Member member2 = new Member("member2", 30);  
  
        memberRepository.save(member1);  
        memberRepository.save(member2);  
  
        // when  
        List<Member> result = memberRepository.findAll();  
  
        // then  
        Assertions.assertThat(result).hasSize(2);  
        Assertions.assertThat(result.size()).isEqualTo(2);  
        Assertions.assertThat(result).contains(member1, member2);  
    }  
}
```



## 서블릿으로 회원 관리 웹 애플리케이션 만들기

이제 본격적으로 서블릿을 이용한 회원 관리 웹 애플리케이션을 만들어보자.

가장 먼저 서블릿으로 회원 등록 HTML 폼을 제공해보자.

`hello.servlet.web.servlet.MemberFormServlet`
```java
package hello.servlet.web.servlet;  
  
import hello.servlet.domain.member.MemberRepository;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
import java.io.PrintWriter;  
  
@WebServlet(name = "memberFormServlet", urlPatterns = "/servlet/members/new-form")  
public class MemberFormServlet extends HttpServlet {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
        response.setContentType("text/html");  
        response.setCharacterEncoding("UTF-8");  
  
        PrintWriter w = response.getWriter();  
        w.write("<!DOCTYPE html>\n" +  
                "<html>\n" +  
                "<head>\n" +  
                "    <meta charset=\"UTF-8\">\n" +  
                "    <title>Title</title>\n" +  
                "</head>\n" +  
                "<body>\n" +  
                "<form action=\"/servlet/members/save\" method=\"post\">\n" +  
                "    username: <input type=\"text\" name=\"username\" />\n" +  
                "    age:      <input type=\"text\" name=\"age\" />\n" +  
                "    <button type=\"submit\">전송</button>\n" +  
                "</form>\n" +  
                "</body>\n" +  
                "</html>\n");  
    } // 서블릿으로 작성하니까 html 코드를 넣기가 너무 힘들다.  
}
```
- 자바 언어로 html을 작성하기에는 좀 무리가 있긴 하지만 완성

`hello.servlet.web.servlet.MemberSaveServlet`
```java
package hello.servlet.web.servlet;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
import java.io.PrintWriter;  
  
@WebServlet(name = "memberSaveServlet", urlPatterns = "/servlet/members/save")  
public class MemberSaveServlet extends HttpServlet {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        System.out.println("MemberSaveServlet.service");  
        String username = request.getParameter("username");  
        int age = Integer.parseInt(request.getParameter("age"));  
  
        Member member = new Member(username, age);  
        memberRepository.save(member);  
  
        response.setContentType("text/html");  
        response.setCharacterEncoding("UTF-8");  
  
        PrintWriter w = response.getWriter();  
        w.write("<html>\n" +  
                "<head>\n" +  
                "    <meta charset=\"UTF-8\">\n" +  
                "</head>\n" +  
                "<body>\n" +  
                "성공\n" +  
                "<ul>\n" +  
                "    <li>id="+member.getId()+"</li>\n" +  
                "    <li>username="+member.getUsername()+"</li>\n" +  
                "    <li>age="+member.getAge()+"</li>\n" +  
                "</ul>\n" +  
                "<a href=\"/index.html\">메인</a>\n" +  
                "</body>\n" +  
                "</html>");  
    }  
}
```

1. 파라미터를 조회해서 Member 객체를 만든다.
2. Member 객체를 MemberRepository를 통해서 저장한다.
3. Member 객체를 사용해서 결과 화면에 HTML을 동적으로 만들어서 응답한다.

**회원 리스트 출력**

`hello.servlet.web.servlet.MemberListServlet`
```java
package hello.servlet.web.servlet;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
import java.io.PrintWriter;  
import java.util.List;  
  
@WebServlet(name = "memberListServlet", urlPatterns = "/servlet/members")  
public class MemberListServlet extends HttpServlet {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
        List<Member> members = memberRepository.findAll();  
  
        response.setContentType("text/html");  
        response.setCharacterEncoding("UTF-8");  
  
        PrintWriter w = response.getWriter();  
        w.write("<html>");  
        w.write("<head>");  
        w.write("    <meta charset=\"UTF-8\">");  
        w.write("    <title>Title</title>");  
        w.write("</head>");  
        w.write("<body>");  
        w.write("<a href=\"/index.html\">메인</a>");  
        w.write("<table>");  
        w.write("    <thead>");  
        w.write("    <th>id</th>");  
        w.write("    <th>username</th>");  
        w.write("    <th>age</th>");  
        w.write("    </thead>");  
        w.write("    <tbody>");  
        /* 정적인 HTML        w.write("    <tr>");        w.write("        <td>1</td>");        w.write("        <td>userA</td>");        w.write("        <td>10</td>");        w.write("    </tr>");        */        for (Member member : members) { // 동적인 HTML            w.write("    <tr>");  
            w.write("        <td>" + member.getId() + "</td>");  
            w.write("        <td>" + member.getUsername() + "</td>");  
            w.write("        <td>" + member.getAge() + "</td>");  
            w.write("    </tr>");  
        }  
        w.write("    </tbody>");  
        w.write("</table>");  
        w.write("</body>");  
        w.write("</html>");  
    }  
}
```

![[Pasted image 20250509141902.png]]

1. `memberRepository.findAll()`을 통해 모든 회원을 조회한다.
2. 회원 목록 HTML을 for 루프를 통해서 회원 수 만큼 동적으로 생성하고 응답한다. 

이쯤에서 되돌아보면, 서블릿의 단점은 아무래도 html 코드 작성의 어려움일 것이다.
따라서 필요한 것이 `템플릿 엔진` 이다.

기존의 방식(서블릿)은 자바 코드에다가 HTML을 삽입하는 것.
새로운 방식(템플릿 엔진)은 HTML 코드에다가 자바 코드를 삽입하는 것.

>참고
>템플릿 엔진에는 JSP, Thymeleaf, Freemarker, Velocity 등이 있다.


**템플릿 엔진으로**
지금까지 서블릿과 자바 코드만으로 HTML을 만들어보았다. 서블릿 덕분에 동적으로 원하는 HTML을 마음껏 만들 수 있다.
정적인 HTML 문서라면 화면이 계속 달라지는 회원의 저장 결과라던가, 회원 목록 같은 동적인 HTML을 만드는 일은 불가능 할 것이다.
그런데 코드에서 보듯이 이것은 매우 복잡하고 비효율적이다. 자바 코드로 HTML을 만들어 내는 것 보다 차라리 HTML 문서에 동적으로 변경해야 하는 부분만 자바 코드를 넣을 수 있게 만든다면 더 편라할 것이다.
이것이 바로 템플릿 엔진이 나온 이유이다. 템플릿 엔진을 사용하면 HTML 문서에서 필요한 곳만 코드를 적용해서 동적으로 변경할 수 있게 된다.

## JSP로 회원 관리 웹 애플리케이션 만들기

**회원 등록 폼 JSP**
`main/webapp/jsp/members/new-form.jsp`
```jsp
<%--  
  Created by IntelliJ IDEA.  User: Dongni  Date: 2025-05-09  Time: 오후 11:44  To change this template use File | Settings | File Templates.--%>  
<%@ page contentType="text/html;charset=UTF-8" language="java" %>  
<html>  
<head>  
    <title>Title</title>  
</head>  
<body>  
<form action="/jsp/members/save.jsp" method="post">  
    username: <input type="text" name="username" />  
    age:      <input type="text" name="age" />  
    <button type="submit">전송</button>  
</form>  
</body>  
</html>
```
- `<%@ page contentType="text/html;charset=UTF-8" language="java" %>` 
	- 첫 줄은 JSP 문서라는 뜻이다. 꼭 이렇게 시작한다.
- 회원 등록 폼 JSP를 보면 첫 줄을 제외하고는 완전히 HTML과 똑같다.
- JSP는 서버 내부에서 `서블릿`으로 변환되는데, 우리가 만들었던 MemberFormServlet과 거의 비슷한 모습으로 변환된다.

**회원 저장 JSP**
`main/webapp/jsp/members/save.jsp`
```jsp
<%--  
  Created by IntelliJ IDEA.  User: Dongni  Date: 2025-05-09  Time: 오후 11:48  To change this template use File | Settings | File Templates.--%>  
  
<%@ page contentType="text/html;charset=UTF-8" language="java" %>  
<%@ page import="hello.servlet.domain.member.Member" %>  
<%@ page import="hello.servlet.domain.member.MemberRepository" %>  
  
<%  
  // request, response 사용 가능 (jsp도 결국 서블릿으로 변환되기 때문에 private service 메서드가 실행되는 거라고 이해하면 됨.  
  MemberRepository memberRepository = MemberRepository.getInstance();  
  
  // 쿼리 파라미터 파싱  
  String username = request.getParameter("username");  
  int age = Integer.parseInt(request.getParameter("age"));  
  
  // 비즈니스 로직 실행  
  Member member = new Member(username, age);  
  memberRepository.save(member);%>  
  
<html>  
<head>  
    <title>Title</title>  
</head>  
<body>  
성공  
<ul>  
  <li>id=<%=member.getId()%></li>  
  <li>username=<%=member.getUsername()%></li>  
  <li>age=<%=member.getAge()%></li>  
</ul>  
<a href="/index.html">메인</a>  
</body>  
</html>
```
- JSP는 자바 코드를 그대로 다 사용할 수 있다.
- `<%@ page import="hello.servlet.domain.member.MemberRepository" %>`
	- 자바의 import 문과 같다.
- `<% ~~ %>`
	- 이 부분에는 자바 코드를 입력할 수 있다.
- `<%= ~~ %>`
	- 이 부분에는 자바 코드를 출력할 수 있다.

회원 저장 JSP를 보면, 회원 저장 서블릿 코드와 같다. 다른 점이 있다면, HTML을 중심으로 하고 자바 코드를 부분부분 입력해주었다는 점.

`<% ~ %>`를 사용해서 HTML 중간에 자바 코드를 출력하고 있다.


**회원 목록 JSP**
`main/webapp/jsp/members.jsp`
```jsp
<%@ page import="hello.servlet.domain.member.Member" %>  
<%@ page import="java.util.List" %>  
<%@ page import="hello.servlet.domain.member.MemberRepository" %><%--  
  Created by IntelliJ IDEA.  User: Dongni  Date: 2025-05-09  Time: 오후 11:57  To change this template use File | Settings | File Templates.--%>  
<%@ page contentType="text/html;charset=UTF-8" language="java" %>  
  
<%  
  MemberRepository memberRepository = MemberRepository.getInstance();  
  
  List<Member> members = memberRepository.findAll();%>  
<html>  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
</head>  
<body>  
<a href="/index.html">메인</a>  
<table>  
  <thead> <th>id</th>  
  <th>username</th>  
  <th>age</th>  
  </thead>  <tbody>  <%  
    for (Member member : members) {  
      out.write(" <tr>");  
      out.write(" <td>" + member.getId() + "</td>");  
      out.write(" <td>" + member.getUsername() + "</td>");  
      out.write(" <td>" + member.getAge() + "</td>");  
      out.write(" </tr>");  
    }  %>  
  </tbody>  
</table>  
</body>  
</html>
```
- 회원 리포지토리를 먼저 조회하고 결과 List를 사용해서 중간에 `<tr><td>` HTML 태그를 반복해서 출력하고 있다.

#### 서블릿과 JSP의 한계
서블릿으로 개발할 때는 뷰(View)화면을 위한 HTML을 만드는 작업이 자바 코드에 섞여서 지저분하고 복잡했다. JSP를 사용한 덕분에 뷰를 생성하는 HTML 작업을 깔끔하게 가져가고, 중간중간 동적으로 변경이 필요한 부분에만 자바 코드를 적용했다.

그런데 이렇게 해도 해결되지 않는 몇가지 고민이 남는다.

회원 저장 JSP를 보자.

코드의 상위 절반은 회원을 저장하기 위한 비즈니스 로직이고, 나머지 하위 절반만 결과를 HTML로 보여주기 위한 뷰 영역이다. 회원 목록의 경우에도 마찬가지다.

코드를 잘 보면, JAVA 코드, 데이터를 조회하는 리포지토리 등등 다양한 코드가 모두 JSP에 노출되어 있다. JSP가 너무 많은 역할을 한다. 이렇게 작은 프로젝트도 벌써 머리가 아파오는데, 수백 수천줄이 넘어가는 JSP를 떠올려보면 정말 지옥과 같을 것이다. (유지보수 지옥 썰)

#### MVC 패턴의 등장
비즈니스 로직은 서블릿 처럼 다른곳에서 처리하고, JSP는 목적에 맞게 HTML로 화면(View)을 그리는 일에 집중하도록 하자. 과거 개발자들도 모두 비슷한 고민이 있었고, 그래서 MVC 패턴이 등장했다.

우리도 직접 MVC 패턴을 적용해서 프로젝트를 리팩터링 해보자.


## MVC 패턴 - 개요
** 너무 많은 역할**
하나의 서블릿이나 JSP 만으로 비즈니스 로직과 뷰 렌더링까지 모두 처리하게 되면, 너무 많은 역할을 맡게 되고, 결과적으로 유지보수가 어려워진다.
비즈니스 로직을 호출하는 부분에 변경이 발생해도 해당 코드를 손대야 하고, UI를 변경할 일이 있어도 비즈니스 로직이 함께 있는 해당 파일을 수정해야 한다. HTML 코드 하나 수정해야 하는데, 수백 줄의 자바 코드가 함께 있는 상황을 상상해보자.. 또는 비즈니스 로직을 하나 수정해야 하는데 수백 수천 줄의 HTML 코드가 함께 있다고 상상해보자.....

**변경의 라이프 사이클**
사실 이게 정말 중요한데, 진짜 문제는 둘 사이에 변경의 라이프 사이클이 다르다는 점이다.
예를 들어서 UI를 일부 수정하는 일과 비즈니스 로직을 일부 수정하는 일은 각각 다르게 발생할 가능성이 매우 높고 대부분 서로에게 영향을 주지 않는다.
이렇게 변경의 라이프 사이클이 다른 부분을 하나의 코드로 관리하는 것은 유지보수하기 좋지 않다. (물론 UI가 많이 변하게되면 함께 변경될 가능성도 있다.)

**

## MVC 패턴 - 적용



## MVC 패턴 - 한계



## 정리