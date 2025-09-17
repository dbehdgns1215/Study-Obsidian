
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
- JSON, XML (API를 사용할 때 주로 사용)asdasdasd
- 거의 모든 형태의 데이터 전송 가능aaaaa
- 서버간의 데이터를 주고 받는 경우에도 대부분 HTTP 사용

#### 웹 서버(Web Server)
- HTTP 기반으로 동작
- 정적 리소스 제공, 기타 부가d 기능 제공
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

**기능 특화**
특히 JSP 같은 뷰 템플릿은 화면을 렌더링 하는데 최적화 되어 있기 때문에 이 부분의 업무만 담당하는 것이 가장 효과적이다.

**Model View Controller**
MVC 패턴은 지금까지 학습한 것 처럼 하나의 서블릿이나 JSP로 처리하던 것을 컨트롤러와 뷰라는 영역으로 서로 역할을 나눈 것을 말한다. 웹 애플리케이션은 보통 이 MVC 패턴을 사용한다.

**컨트롤러** : HTTP 요청을 받아서 파라미터를 검증하고, 비즈니스 로직을 실행한다. 그리고 뷰에 전달할 결과 데이터를 조회해서 모델에 담는다.
**모델** : 뷰에 출력할 데이터를 담아둔다. 뷰가 필요한 데이터를 모두 모델에 담아서 전달해주는 덕분에 뷰는 비즈니스 로직이나 데이터 접근을 몰라도 되고, 화면을 렌더링하는 일에 집중할 수 있다.
**뷰** : 모델에 담겨있는 데이터를 사용해서 화면을 그리는 일에 집중한다. 여기서는 HTML을 생성하는 부분을 말한다.

>참고
>컨트롤러에 비즈니스 로직을 둘 수도 있지만, 이렇게 되면 컨트롤러가 너무 많은 역할을 담당한다. 그래서 일반적으로 비즈니스 로직은 서비스라는 계층을 별도로 만들어서 처리한다. 그리고 컨트롤러는 비즈니스 로직이 있는 서비스를 호출하는 역할을 담당한다. 참고로 비즈니스 로직을 변경하면 비즈니스 로직을 호출하는 컨트롤러의 코드도 변경될 수 있다. 앞에서는 이해를 돕기 위해서 비즈니스 로직을 호출한다는 표현 보다는 비즈니스 로직이라 설명했다.

**MVC 패턴 등장 이전**
![[Pasted image 20250510162502.png]]

**MVC 패턴 1**
![[Pasted image 20250510162322.png]]

**MVC 패턴 2**
![[Pasted image 20250510162331.png]]

## MVC 패턴 - 적용
서블릿을 컨트롤러로 사용하고 JSP를 뷰로 사용해서 MVC 패턴을 적용해보자.
Model은 HttpServletRequest 객체를 사용한다. request는 내부에 데이터 저장소를 가지고 있는데, `request.setAttribute()`, `request.getAttribute()`를 사용하면 데이터를 보관하고 조회할 수 있다.

`hello.servlet.web.servletmvc.MvcMemberFormServlet`
```java
package hello.servlet.web.servletmvc;  
  
import jakarta.servlet.RequestDispatcher;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
  
  
@WebServlet(name = "mvcMemberFormServlet", urlPatterns = "/servlet-mvc/members/new-form")  
public class MvcMemberFormServlet extends HttpServlet {  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        String viewPath = "/WEB-INF/views/new-form.jsp";  
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);// 컨트롤러 -> 뷰 이동할 때 사용  
        dispatcher.forward(request, response); // 서블릿에서 JSP 호출  
    }  
}
```
- `dispatcher.forward()`: 다른 서블릿이나 JSP로 이동할 수 있는 기능이다. *서버 내부에서 다시 호출이 발생한다.* ()

>`/WEB-INF`
>이 경로 안에 JSP가 있으면 외부에서 직접 JSP를 호출할 수 없다. (경로를 url로 쳐서 호출하는 것)
>우리가 기대하는 것은 항상 컨트롤러를 통해서 JSP를 호출하는 것이다.

>**redirect vs forward**
>리다이렉트는 실제 클라이언트(웹 브라우저)에 응답이 나갔다가, 클라이언트가 redirect 경로로 다시 요청한다.
>따라서 클라이언트가 인지할 수 있고 URL 경로도 실제로 변경된다. 반면에 포워드는 서버 내부에서 일어나는 호출이기 때문에 클라이언트가 전혀 인지하지 못한다.


`main/webapp/WEB-INF/views/new-form.jsp`'
```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>  
<html>  
<head>  
  <meta charset="UTF-8">  
  <title>Title</title>  
</head>  
<body>  
<!-- 상대경로 사용, [현재 URL이 속한 계층 경로 + /save] --><form action="save" method="post">  
  username: <input type="text" name="username" />  
  age: <input type="text" name="age" />  
  <button type="submit">전송</button>  
</form>  
</body>  
</html>
```
- 여기서 form의 action을 보면 절대 경로가 아니라 상대 경로로 되어있는 것을 확인할 수 있다.
- 이렇게 상대 경로를 사용하면 폼 전송시 현재 URL이 속한 계층 경로 + save가 호출된다.
	- 현재 계층 경로: `servlet-mvc/members`
	- 결과: `/servlet-mvc/members.save`


#### 회원 저장

**회원 저장 - 컨트롤러**
`MvcMemberSaveServlet`
```java
package hello.servlet.web.servletmvc;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import jakarta.servlet.RequestDispatcher;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
  
@WebServlet(name ="nvcMemberSaveServlet", urlPatterns = "/servlet-mvc/members/save")  
public class MvcMemberSaveServlet extends HttpServlet {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        // 쿼리 파라미터 파싱  
        String username = request.getParameter("username");  
        int age = Integer.parseInt(request.getParameter("age"));  
  
        // 비즈니스 로직 실행  
        Member member = new Member(username, age);  
        memberRepository.save(member);  
  
        // Model에 데이터를 보관한다.  
        request.setAttribute("member", member);  
  
        String viewPath = "/WEB-INF/views/save-result.jsp";  
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);  
        dispatcher.forward(request, response);  
    }  
}
```
- `HttpServletRequest`를 Model로 사용한다.
- request가 제공하는 `setAttribute()`를 사용하면 request 객체에 데이터를 보관해서 뷰에 전달할 수 있다.
- 뷰는 `requset.getAttribute()`를 사용해서 데이터를 꺼내면 된다.



**회원 저장 - 뷰**
`main/webapp/WEB-INF/views/save-result.jsp`
```jsp
<%@ page import="hello.servlet.domain.member.Member" %><%--  
  Created by IntelliJ IDEA.  User: Dongni  Date: 2025-05-10  Time: 오후 7:05  To change this template use File | Settings | File Templates.--%>  
<%@ page contentType="text/html;charset=UTF-8" language="java" %>  
<html>  
<head>  
    <title>Title</title>  
</head>  
<body>  
성공  
<ul>  
    <%--<li>id=<%=((Member)request.getAttribute("member")).getId()%></li>  
    <li>username=<%=((Member)request.getAttribute("member")).getUsername()%></li>    <li>age=<%=((Member)request.getAttribute("member")).getAge()%></li>--%>    <li>id=${member.id}</li>  
    <li>username=${member.username}</li>  
    <li>age=${member.age}</li>  
</ul>  
<a href="/index.html">메인</a>  
</body>  
</html>
```
- `<%= request.getAttribute("member")%>`로 모델에 저장한 member 객체를 꺼낼 수 있지만, 너무 복잡해진다.
- JSP는 `${}` 문법을 제공하는데, 이 문법을 사용하면 request의 attribute에 담긴 데이터를 편리하게 조회할 수 있다.


#### 회원 목록 조회

**회원 목록 조회 - 컨트롤러**
`MvcMemberListServlet`
```java
package hello.servlet.web.servletmvc;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import jakarta.servlet.RequestDispatcher;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import java.io.IOException;  
import java.util.List;  
  
@WebServlet(name = "mvcMemberListServlet", urlPatterns = "/servlet-mvc/members")  
public class MvcMemberListServlet extends HttpServlet {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
        List<Member> members = memberRepository.findAll();  
  
        request.setAttribute("members", members);  
  
        String viewPath = "/WEB-INF/views/members.jsp";  
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);  
        dispatcher.forward(request, response);  
    }  
}
```
- `setAttribute()`가 핵심 (모델에 저장 후 Dispatcher를 통해서 뷰에게 전달)

**회원 목록 조회 - 뷰**
`main/webapp/WEB-INF/views/members.jsp`
```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>  
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>  
  
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
  </thead>  <tbody>  <c:forEach var="item" items="${members}"> <!-- members는 model에 담겨있는 그 members -->    <tr>  
      <td>${item.id}</td>  
      <td>${item.username}</td>  
      <td>${item.age}</td>  
    </tr>  </c:forEach>  
  </tbody>  
</table>  
</body>  
</html>
```

> JSP를 학습하는 것이 주 목적이 아님.
> 궁금하면 반나절이면 대부분의 기능 학습 가능

## MVC 패턴 - 한계
MVC 패턴을 적용한 덕분에 컨트롤러의 역할과 뷰를 렌더링하는 역할을 명확하게 구분할 수 있었다.
특히 뷰는 화면을 그리는 역할에 충실한 덕분에 코드가 깔끔하고 직관적이다. 단순히 모델에서 필요한 데이터를 꺼내고 화면을 만들기만 하면 된다.
그런데 컨트롤러는 딱 봐도 중복되는 코드가 많고 필요하지 않아 보이는 코드도 있었다..

#### **MVC 컨트롤러의 단점**

**포워드 중복**
View로 이동하는 코드가 항상 중복 호출되어야 한다.
물론 이 부분을 메서드로 공통화해도 되지만, 해당 메서드도 항상 직접 호출해야 한다.
```java 
RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);  
dispatcher.forward(request, response);
```

**ViewPath 중복**
```java
String viewPath = "/WEB-INF/views/aaaa.jsp"; 
```
- prefix: `/WEB-INF/views/`
- suffix: `.jsp`

그리고 만약 jsp가 아닌 thymeleaf 같은 다른 뷰로 변경하려면 전체 코드를 다 변경해야만 한다.

**사용하지 않는 코드**
다음 코드를 사용할 때도 있고 사용하지 않을 때도 있다. 특히 response는 이전 코드에서 사용되지도 않았다.
```java
HttpServletRequest request, HttpServletResponse response 
```
- 그리고 이런 `HttpServletRequest`, `HttpServletResponse`를 사용하는 코드는 테스트 케이스를 작성하기도 어렵다.

**공통 처리가 어렵다**
기능이 복잡해질 수록 컨트롤러에서 공통으로 처리해야 하는 부분이 점점 더 많이 증가할 것이다. 단순히 공통 기능을 메서드로 뽑으면 될 것 같지만, 결과적으로 해당 메서드를 항상 호출해야 하고 실수로 호출하지 않으면 문제가 될 것이다. 그리고 호출하는 것 자체도 중복이다.

**정리하면 공통 처리가 어렵다는 문제가 있다.**
이 문제를 해결하려면 컨트롤러 호출 전에 먼저 공통 기능을 처리해야 한다. 소위 **수문장**역할을 하는 기능이 필요하다는 것이다.

**프론트 컨트롤러(Front Controller) 패턴**을 도입하면 이런 문제를 깔끔하게 해결할 수 있다. (입구를 하나로!)

스프링 MVC의 핵심도 바로 이 프론트 컨트롤러에 있다.


## 정리

### 서블릿만으로 HTML 화면을 직접 만드는 것이 왜 어려울까요?

1. 서버 리소스 부족
2. 자바 코드 안에 HTML을 작성하는 것의 복잡성
3. 사용자 인증 처리의 어려움
4. 데이터베이스 연결 문제

해설
2. 서블릿만으로는 자바 코드 내에서 HTML 태그를 문자열처럼 작성해야 해서 유지보수가 어려워요. JSP가 이 문제를 해결하는 데 도움을 줬답니다.


### JSP만으로 웹 애플리케이션을 개발할 때 발생하는 주요 문제점은 무엇일까요?

1. 서버 응답 속도 저하
2. HTML 태그 사용 제한
3. CSS 스타일 적용 불가
4. 비즈니스 로직과 화면 표시 로직의 혼합

해설
4. JSP는 HTML과 자바 코드를 섞어 쓰게 되어 화면 로직과 비즈니스 로직이 혼재되어 복잡해지고 유지보수가 어려워져요. MVC 패턴이 이 문제를 해결하기 위해 등장했죠.


### MVC 패턴의 주된 목적은 무엇인가요?

1. 클라이언트 측 코드 실행
2. 데이터베이스 성능 최적화
3. 서버 보안 강화
4. 애플리케이션 로직을 역할에 따라 분리

해설
4. MVC는 Model, View, Controller 세 부분으로 나누어 각자의 역할에 집중하게 함으로써 코드의 분리와 유지보수성을 높여요. 서블릿과 JSP에서 발생한 혼합 문제를 해결해요.


### MVC 패턴에서 Model은 어떤 역할을 담당하나요?

1. 사용자 인터페이스 화면 표시
2. 데이터베이스와 직접 통신
3. View에 전달할 데이터를 담는 컨테이너
4. 클라이언트 요청 처리 및 비즈니스 로직 호출

해설
3. Model은 Controller가 비즈니스 로직 처리 후 View에게 전달할 데이터를 담아두는 공간이에요. View는 이 Model에서 필요한 데이터를 꺼내 화면을 그립니다.


### 기본 MVC 구현에서 발생하는 반복적인 코드 및 공통 처리의 어려움을 해결하기 위해 도입된 패턴은 무엇일까요?

1. Adapter 패턴
2. Observer 패턴
3. Factory Method 패턴
4. Front Controller 패턴
5. 기본 MVC에서는 반복되는 로직이나 공통 처리가 여러 Controller에 흩어지는 문제가 있었어요. Front Controller는 요청을 한 곳에서 받아 공통 처리를 위임해서 이 문제를 개선해요.



---

# 프론트 컨트롤러 패턴 소개

**프론트 컨트롤러 도입 전**
![[Pasted image 20250526000325.png]]
- 공통 로직과 특정 로직들이 함쳐져 있는 상태
- 아무데나 들어올 수 있어서 (입구가 없음) 공통 로직을 모두에게 넣어줘야 함

**프론트 컨트롤러 도입 후**
![[Pasted image 20250526000446.png]]
- 서블릿을 도입해서 공통 로직을 처리하면 됨
- 이후에는 각 컨트롤러가 필요한 로직은 각자 알아서 처리하게끔 만들면 됨
- 공통 로직을 모아서 처리하고 모두가 한 번씩 거쳐야하는 일종의 수문장, 문지기 역할임

**FrontController 패턴 특징**
- 프론트 컨트롤러 서블릿 하나로 클라이언트의 요청을 받음
- 프론트 컨트롤러가 요청에 맞는 컨트롤러를 찾아서 호출함
- 입구를 하나로!
- 공통 로직 처리 가능
- 프론트 컨트롤러를 제외한 나머지 컨트롤러는 서블릿을 사용하지 않아도 됨

**스프링 웹 MVC와 프론트 컨트롤러**
- 스프링 웹 MVC의 핵심도 바로 **FrontController**
- 스프링 웹 MVC의 **DispatcherServlet**이 FrontController 패턴으로 구현되어 있음


**뭐가 불편?
- 
**어떻게 해결?
- 
# 프론트 컨트롤러 도입 - v1
프론트 컨트롤러를 단계적으로 도입해보자.

이번 목표는 기존 코드를 최대한 유지하면서, 프론트 컨트롤러를 도입하는 것.
먼저 구조를 맞추어두고 점진적으로 리펙터링 해보자.

**V1 구조**
![[Pasted image 20250528001108.png]]

```java
package hello.servlet.web.frontcontroller.v1;  
  
import jakarta.servlet.ServletException;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
  
public interface ControllerV1 {  
  
    void process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException;  
      
}
```
- 서블릿과 비슷한 모양의 컨트롤러 인터페이스를 도입한다.
- 각 컨트롤러들은 이 인터페이스를 구현하면 된다.
- 프론트 컨트롤러는 이 인터페이스를 호출해서 구현과 관계없이 로직의 일관성을 가져갈 수 있다.

이제 이 인터페이스를 구현한 컨트롤러를 만들어보자. 지금 단계에서는 기존 로직을 최대한 유지하는 것이 핵심.

`FrontControllerServletV1`
```java
package hello.servlet.web.frontcontroller.v1;  
  
import hello.servlet.web.frontcontroller.v1.controller.MemberFormControllerV1;  
import hello.servlet.web.frontcontroller.v1.controller.MemberListControllerV1;  
import hello.servlet.web.frontcontroller.v1.controller.MemberSaveControllerV1;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
import java.util.HashMap;  
import java.util.Map;  
  
@WebServlet(name = "frontControllerServletV1", urlPatterns = "/front-controller/v1/*")  
public class FrontControllerServletV1 extends HttpServlet {  
  
    private Map<String, ControllerV1> controllerMap = new HashMap<>(); // 컨트롤러 매핑 정보  
  
    public FrontControllerServletV1() {  
        controllerMap.put("/front-controller/v1/members/new-form", new MemberFormControllerV1());  
        controllerMap.put("/front-controller/v1/members/save", new MemberSaveControllerV1());  
        controllerMap.put("/front-controller/v1/members", new MemberListControllerV1());  
    }  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response)  
            throws ServletException, IOException {  
        System.out.println("FrontControllerServletV1.service");  
  
        String requestURI = request.getRequestURI(); // http://localhost:8080/front-controller/v1/dhy -> 'front-controller/v1/dhy' 이 부분만 추출 가능  
  
        ControllerV1 controller = controllerMap.get(requestURI);  
        if (controller == null) {  
            response.setStatus(HttpServletResponse.SC_NOT_FOUND); // 404 Error  
            return;  
        }  
  
        controller.process(request, response);  
    }  
}
```

`MemberFormControllerV1`
```java
package hello.servlet.web.frontcontroller.v1.controller;  
  
import hello.servlet.web.frontcontroller.v1.ControllerV1;  
import jakarta.servlet.RequestDispatcher;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
  
public class MemberFormControllerV1 implements ControllerV1 {  
    @Override  
    public void process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        String viewPath = "/WEB-INF/views/new-form.jsp";  
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);// 컨트롤러 -> 뷰 이동할 때 사용  
        dispatcher.forward(request, response); // 서블릿에서 JSP 호출  
    }  
}
```

`MemberSaveControllerV1`
```java
package hello.servlet.web.frontcontroller.v1.controller;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import hello.servlet.web.frontcontroller.v1.ControllerV1;  
import jakarta.servlet.RequestDispatcher;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
  
public class MemberSaveControllerV1 implements ControllerV1 {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @Override  
    public void process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        // 쿼리 파라미터 파싱  
        String username = request.getParameter("username");  
        int age = Integer.parseInt(request.getParameter("age"));  
  
        // 비즈니스 로직 실행  
        Member member = new Member(username, age);  
        memberRepository.save(member);  
  
        // Model에 데이터를 보관한다.  
        request.setAttribute("member", member);  
  
        String viewPath = "/WEB-INF/views/save-result.jsp";  
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);  
        dispatcher.forward(request, response);  
    }  
}
```

`MemberListControllerV1`
```java
package hello.servlet.web.frontcontroller.v1.controller;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import hello.servlet.web.frontcontroller.v1.ControllerV1;  
import jakarta.servlet.RequestDispatcher;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
import java.util.List;  
  
public class MemberListControllerV1 implements ControllerV1 {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @Override  
    public void process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        List<Member> members = memberRepository.findAll();  
  
        request.setAttribute("members", members);  
  
        String viewPath = "/WEB-INF/views/members.jsp";  
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);  
        dispatcher.forward(request, response);  
    }  
}
```


**뭐가 불편?
- 중복되는 코드가 많음
- 기존에 비해 살짝은 복잡해진 코드
**어떻게 해결?
- 최적화 해보자. 분리하고 다듬고!
# View 분리 - v2
모든 컨트롤러에서 뷰로 이동하는 부분에 중복이 있고, 깔끔하지 않다.
```java
String viewPath = "/WEB-INF/views/members.jsp";  
RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);  
dispatcher.forward(request, response);
```
이 부분을 깔끔하게 분리하기 위해 별도로 뷰를 처리하는 객체를 만들자.

**V2 구조**
![[Pasted image 20250528223301.png]]
- 기존 방식처럼 특정 컨트롤러가 직접 JSP로 forward 해주는 것이 아니라, MyView라는 객체를 만들어서 반환해 주는 것.

`ControllerV2`
```java
package hello.servlet.web.frontcontroller.v2;  
  
import hello.servlet.web.frontcontroller.MyView;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
  
public interface ControllerV2 {  
  
    MyView process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException;  
  
}
```


`MemberFormControllerV2`
```java
package hello.servlet.web.frontcontroller.v2.controller;  
  
import hello.servlet.web.frontcontroller.MyView;  
import hello.servlet.web.frontcontroller.v2.ControllerV2;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
  
public class MemberFormControllerV2 implements ControllerV2 {  
  
    @Override  
    public MyView process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        return new MyView("/WEB-INF/views/new-form.jsp");  
    }  
}
```

`MemberSaveControllerV2`
```java
package hello.servlet.web.frontcontroller.v2.controller;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import hello.servlet.web.frontcontroller.MyView;  
import hello.servlet.web.frontcontroller.v2.ControllerV2;  
import jakarta.servlet.RequestDispatcher;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
  
public class MemberSaveControllerV2 implements ControllerV2 {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @Override  
    public MyView process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        // 쿼리 파라미터 파싱  
        String username = request.getParameter("username");  
        int age = Integer.parseInt(request.getParameter("age"));  
  
        // 비즈니스 로직 실행  
        Member member = new Member(username, age);  
        memberRepository.save(member);  
  
        // Model에 데이터를 보관한다.  
        request.setAttribute("member", member);  
  
        return new MyView("/WEB-INF/views/save-result.jsp");  
    }  
}
```

`MemberListControllerV2`
```java
package hello.servlet.web.frontcontroller.v2.controller;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import hello.servlet.web.frontcontroller.MyView;  
import hello.servlet.web.frontcontroller.v2.ControllerV2;  
import jakarta.servlet.RequestDispatcher;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
import java.util.List;  
  
public class MemberListControllerV2 implements ControllerV2 {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @Override  
    public MyView process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
  
        List<Member> members = memberRepository.findAll();  
        request.setAttribute("members", members);  
        return new MyView("/WEB-INF/views/members.jsp");  
    }  
}
```

`FrontControllerServletV2`
```java
package hello.servlet.web.frontcontroller.v2;  
  
import hello.servlet.web.frontcontroller.MyView;  
import hello.servlet.web.frontcontroller.v2.controller.MemberFormControllerV2;  
import hello.servlet.web.frontcontroller.v2.controller.MemberListControllerV2;  
import hello.servlet.web.frontcontroller.v2.controller.MemberSaveControllerV2;  
import jakarta.servlet.ServletException;  
import jakarta.servlet.annotation.WebServlet;  
import jakarta.servlet.http.HttpServlet;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
import java.util.HashMap;  
import java.util.Map;  
  
@WebServlet(name = "frontControllerServletV2", urlPatterns = "/front-controller/v2/*")  
public class FrontControllerServletV2 extends HttpServlet {  
  
    private Map<String, ControllerV2> controllerMap = new HashMap<>(); // 컨트롤러 매핑 정보  
  
    public FrontControllerServletV2() {  
        controllerMap.put("/front-controller/v2/members/new-form", new MemberFormControllerV2());  
        controllerMap.put("/front-controller/v2/members/save", new MemberSaveControllerV2());  
        controllerMap.put("/front-controller/v2/members", new MemberListControllerV2());  
    }  
  
    @Override  
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {  
        System.out.println("FrontControllerServletV2.service");  
  
        String requestURI = request.getRequestURI(); // http://localhost:8080/front-controller/v2/dhy -> 'front-controller/v1/dhy' 이 부분만 추출 가능  
  
        ControllerV2 controller = controllerMap.get(requestURI);  
        if (controller == null) {  
            response.setStatus(HttpServletResponse.SC_NOT_FOUND); // 404 Error  
            return;  
        }  
  
        MyView view = controller.process(request, response);  
  
        view.render(request, response);  
    }  
}
```
- 우선, 뷰를 호출하는 부분이 중복되었기 때문에 공통적인 로직을 처리해 줄 무언가가 필요했다.
- 그래서 만든 것이 `MyView` 클래스.
- `render` 함수를 통해서 뷰로 연결 해줌.
- 이 MyView 클래스를 이용해서 기존에 있던 기능들을 최적화 해줬음
	- ex)
```java
// 이전 코드
String viewPath = "/WEB-INF/views/members.jsp";  
RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);  
dispatcher.forward(request, response);

// 최적화 코드
request.setAttribute("members", members);  
return new MyView("/WEB-INF/views/members.jsp");
```



**뭐가 불편?
- V2의 코드를 자세히 봐보자.
- `public MyView process(HttpServletRequest request, HttpServletResponse response)`
- 사용하지도 않는 `request`와 `response`가 파라미터로 넘어오고 있다.
- 필요 없는데, 스펙상 넘겨 받아야 하기 때문에 존재하는 것.
- 또한 `request` 속 `model`의 개념을 적용하지도 않았음ㅈ.
**어떻게 해결?
- 
# Model 추가 - v3
**서블릿 종속성 제거**
컨트롤러 입장에서 HttpServletRequest, HttpServletResponse 가 꼭 필요할까?
요청 파라미터 정보는 자바의 Map으로 대신 넘기도록 하면 지금 구조에서는 컨트롤러가 서블릿 기술을 몰라도 동작할 수 있다.
그리고 request 객체를 Model로 사용하는 대신에 별도의 Model 객체를 만들어서 반환하면 된다.
우리가 구현하는 컨트롤러가 서블릿 기술을 전혀 사용하지 않도록 변경해보자.
이렇게 하면 구현 코드도 매우 단순해지고 테스트 코드 작성이 쉬워질 것이다.

**뷰 이름 중복 제거**
컨트롤러에서 지정하는 뷰 이름에 중복이 있는 것을 확인할 수 있다.
컨트롤러는 **뷰의 논리 이름**을 반환하고, 실제 **물리 위치의 이름**은 프론트 컨트롤러에서 처리하도록 단순화하자. (By viewResolver)
이렇게 해두면 향후 뷰의 폴더 위치가 함께 이동해도 프론트 컨트롤러만 고치면 된다.

- `/WEB-INF/views/new-form.jsp` -> **new-form**
- `/WEB-INF/views/save-result.jsp` -> **save-result**
- `/WEB-INF/views/members.jsp` -> **members**

**V3 구조**
![[Pasted image 20250531003933.png]]

**ModelView**
지금까지 컨트롤러에서 서블릿에 종속적인 HttpServletRequest를 사용했다. 그리고 Model도 `request.setAttribute()`를 통해 데이터를 저장하고 뷰에 전달했다.

서블릿의 종속성을 제거하기 위해서 Model을 직접 만들고 추가로 View 이름까지 전달하는 객체를 만들어보자.
(이번 버전에서는 컨트롤러에서 HttpServletRequest를 사용할 수 없다. 따라서 직접 `request.setAttribute()`를 호출할 수도 없기 때문에, Model이 별도로 필요하다.)

참고로 `ModelView`객체는 다른 버전에서도 사용하므로 패키지를 `frontcontroller`에 둔다.



**뭐가 불편?
- 
**어떻게 해결?
- 
# 단순하고 실용적인 컨트롤러 - v4
앞서 만든 V3 컨트롤러는 서블릿 종속성을 제거하고 뷰 경로의 중복을 제거하는 등의 설계로 잘 설계된 컨트롤러이다.
그런데 실제 컨트롤러 인터페이스를 구현하는 개발자 입장에서 보면 항상 ModelView 객체를 생성하고 반환해야 하는 부분이 번거롭게 느껴진다.
좋은 프레임워크는 아키텍처도 중요하지만 그와 더불어 실제 개발하는 개발자가 단순하고 편리하게 사용할 수 있어야 한다. 소위 실용성이 있어야 한다는 말.

이번에는 v3를 조금 변형해서 실제 구현하는 개발자들이 매우 편리하게 개발할 수 있는 v4 버전을 개발해보자.

**V4 구조**
![[Pasted image 20250601233536.png]]
- 기본적인 구조는 V3와 같다. 대신에 컨트롤러가 `ModelView`를 반환하지 않고, `ViewName`만 반환한다.

```java
package hello.servlet.web.frontcontroller.v4;

import java.util.Map;

public interface ControllerV4 {
	/**
	* @param paramMap
	* @param model
	* @return viewName
	*/
	String process(Map<String, String> paramMap, Map<String, Object> model);
}
```
- 이번 버전은 인터페이스에 ModelView가 없다. model 객체는 파라미터로 전달되기 때문에 그냥 사용하면 되고, 결과로 뷰의 이름만 반환해주면 된다.



**뭐가 불편?
- 
**어떻게 해결?
- 
# 유연한 컨트롤러1 - v5
만약 어떤 개발자는 `ControllerV3` 방식으로 개발하고 싶고 어떤 개발자는 `ControllerV4` 방식으로 개발하고 싶다면 어떻게 해야할까?

```java
public interface ControllerV3 {
	ModelView process(Map<String, String> paramMap);
}
```

```java
public interface ControllerV4 {
	String process(Map<String, String> paramMap, Map<String, Object> model);
}
```

**어댑터 패턴**
지금까지 우리가 개발한 프론트 컨트롤러는 한가지 방식의 컨트롤러 인터페이스만 사용할 수 있다.
`ControllerV3`, `ControllerV4`는 완전히 다른 인터페이스이다.
따라서 호환이 불가능하다. 마치, v3는 110v이고 v4는 220v 전기 콘센트 같은 것이다.
이럴 때 사용하는 것이 바로 `어댑터`이다.
어댑터 패턴을 사용해서 프론트 컨트롤러가 다양한 방식의 컨트롤러를 처리할 수 있도록 변경해보자.

**V5 구조**
![[Pasted image 20250602235127.png]]
- **핸들러 어댑터**: 중간에 어댑터 역할을 하는 어댑터가 추가되었는데 이름이 핸들러 어댑터이다. 여기서 어댑터 역할을 해주는 덕분에 다양한 종류의 컨트롤러를 호출할 수 있다.
- **핸들러**: 컨트롤러의 이름을 더 넓은 범위인 핸들러로 변경했다. 그 이유는 이제 어댑터가 있기 때문에 꼭 컨트롤러의 개념 뿐만 아니라 어떠한 것이든 해당하는 종류의 어댑터만 있으면 다 처리할 수 있기 때문이다.

`MyHandlerAdapter`
```java
package hello.servlet.web.frontcontroller.v5;

import hello.servlet.web.frontcontroller.ModelView;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public interface MyHandlerAdapter {

	boolean supports(Object handler);
	
	ModelView handle(HttpServletRequest request, HttpServletResponse response, Object handler) throws ServletException, IOException;
	
}
```
- `boolean supports(Object handler)`
	- `handler`는 컨트롤러를 말한다.
	- 어댑터가 해당 컨트롤러를 처리할 수 있는지 판단하는 메서드이다.
- `ModelView handle(HttpServletRequest request, HttpServletResponse response, Object handler)`
	- 어댑터는 실제 컨트롤러를 호출하고 그 결과로 ModelView를 반환해야 한다.
	- 실제 컨트롤러가 ModelView를 반환하지 못하면 어댑터가 ModelView를 직접 생성해서라도 반환해야 한다.
	- 이전에는 프론트 컨트롤러가 실제 컨트롤러를 호출했지만 이제는 이 어댑터를 통해서 실제 컨트롤러가 호출된다.



**뭐가 불편?
- 
**어떻게 해결?
- 
# 유연한 컨트롤러2 - v5
`FrontControllerServletV5`에 `ControllerV4` 기능도 추가해보자.

**실행 로직**
```java
@Override  
public ModelView handle(HttpServletRequest request, HttpServletResponse response, Object handler) throws ServletException, IOException {  
    ControllerV4 controller = (ControllerV4) handler;  
  
    Map<String, String> paramMap = createParamMap(request);  
    HashMap<String, Object> model = new HashMap<>();  
    String viewName = controller.process(paramMap, model);  
  
    // 어댑터의 역할 수행  
    ModelView mv = new ModelView(viewName);  
    mv.setModel(model);  
  
    return mv;  
}
```


**뭐가 불편?
- 
**어떻게 해결?
- 
# 정리
지금까지 v1 ~ v5로 점진적으로 프레임워크를 발전시켜 왔다.

- **v1: 프론트 컨트롤러를 도입**
	- 기존 구조를 최대한 유지하면서 프론트 컨트롤러를 도입
- **v2: View 분류**
	- 단순 반복 되는 뷰 로직 분리 (MyView.java)
- **v3: Model 추가**
	- 서블릿 종속성 제거
	- 뷰 이름 중복 제거 (ViewResolver)
- **v4: 단순하고 실용적인 컨트롤러**
	- v3와 거의 비슷
	- 구현 입장에서 ModelView를 직접 생성해서 반환하지 않도록 편리한 인터페이스 제공
- **v5: 유연한 컨트롤러**
	- 어댑터 패턴 도입
	- 어댑터를 추가해서 프레임워크를 유연하고 확장성 있게 설계

여기에 애노테이션을 사용해서 컨트롤러를 더 편리하게 발전시킬 수 있다.
만약 애노테이션을 사용해서 컨트롤러를 편리하게 사용할 수 있게 하려면 어떻게 해야활까?
바로 애노테이션을 지원하는 어댑터를 추가하면 된다!
다형성과 어댑터 덕분에 기존 구조를 유지하면서, 프레임워크의 기능을 확장할 수 있다.

**스프링 MVC**
여기서 더 발전시키면 좋겠지만, 스프링 MVC의 핵심 구조를 파악하는데 필요한 부분은 모두 만들어보았다.
사실 지금까지 작성한 코드는 스프링 MVC 프레임워크의 핵심 코드의 축약 버전이고, 구조도 거의 같다.

스프링 MVC에는 지금까지 우리가 학습한 내용과 거의 같은 구조를 가지고 있다.



### 프론트 컨트롤러 패턴에서 클라이언트의 모든 요청을 가장 먼저 받아 처리하는 역할을 하는 것은 무엇일까요?

1. 프론트 컨트롤러 서블릿
2. 뷰 템플릿
3. 특정 컨트롤러
4. 데이터베이스

해설
1. 프론트 컨트롤러 서블릿
클라이언트 요청은 중앙 집중식 게이트웨이 역할을 하는 프론트 컨트롤러로 먼저 전달됩니다. 여기서 요청에 맞는 적절한 컨트롤러를 찾아 위임합니다.


### V3 버전에서 컨트롤러가 HttpServletRequest에 직접 의존하지 않도록 설계가 변경된 가장 큰 이유(장점)는 무엇이었나요?

1. 공통 기능 구현 용이성 확보
2. 컨트롤러 테스트 용이성 및 단순화
3. 응답 데이터 전송 속도 향상
4. 뷰 처리 로직 단순화

해설
2. 컨트롤러 테스트 용이성 및 단순화
HttpServletRequest 의존성을 제거하면 컨트롤러의 로직만을 순수하게 테스트하기 쉬워지며, 코드 또한 단순해집니다. 이는 V3 설계의 핵심 목표 중 하나였습니다.


### V3에서 컨트롤러가 실제 물리적인 뷰 경로 대신 '논리적인' 뷰 이름만 반환하게 변경된 이유는 무엇이었을까요?

1. HTTP 응답 효율 증가
2. 컨트롤러 간 데이터 공유 용이성
3. 모델 데이터 바인딩 자동화
4. 프론트 컨트롤러에서 뷰 경로 일괄 관리

해설
4. 프론트 컨트롤러에서 뷰 경로 일괄 관리
뷰의 물리적인 경로 정보가 컨트롤러마다 중복되는 것을 방지하고, 프론트 컨트롤러(또는 ViewResolver)에서 뷰 경로 접두사/접미사를 일괄적으로 관리하기 위함입니다.



### 다양한 형태의 컨트롤러(예: V3, V4)를 하나의 프론트 컨트롤러에서 유연하게 처리하기 위해 V5에서 도입된 '핸들러 어댑터(Handler Adapter)'의 주된 역할은 무엇일까요?

1. 컨트롤러 매핑 정보 관리
2. 뷰 템플릿 엔진 선택
3. 컨트롤러 실행 및 결과를 FC에 맞게 변환
4. 클라이언트 요청 파라미터 검증

해설
3. 컨트롤러 실행 및 결과를 FC에 맞게 변환
핸들러 어댑터는 다양한 인터페이스를 가진 컨트롤러를 프론트 컨트롤러가 호출할 수 있도록 중간에서 연결하고, 컨트롤러 실행 후 결과를 프론트 컨트롤러가 처리할 수 있는 형태(ModelAndView 등)로 변환합니다.



### 우리가 V1부터 V5까지 단계적으로 발전시킨 프레임워크 구조와 유사하게, 스프링 MVC의 핵심 역할을 하는 DispatcherServlet은 어떤 디자인 패턴을 기반으로 구현되었을까요?

1. 프론트 컨트롤러 패턴
2. 팩토리 패턴
3. 옵저버 패턴
4. 싱글톤 패턴

해설
1. 프론트 컨트롤러 패턴
스프링 MVC의 DispatcherServlet은 모든 클라이언트 요청을 하나의 진입점에서 중앙 집중식으로 받아 처리하고 적절한 핸들러(컨트롤러)에게 위임하는 프론트 컨트롤러 패턴을 구현한 것입니다.



---

# 섹션 6. 스프링 MVC - 구조 이해

## 스프링 MVC 전체 구조

**직접 만든 MVC 구조**
![[Pasted image 20250608204848.png]]

**Spring MVC 구조**
![[Pasted image 20250608204907.png]]

**직접 만든 프레임워크 -> 스프링 MVC 비교**
- FrontController -> DispatcherServlet
- handlerMappingMap -> HandlerMapping
- MyHandlerAdapter -> HandlerAdapter
- ModelView -> ModelAndView
- viewResolver -> ViewResolver
- MyView -> View


**DispatcherServlet 구조 살펴보기**
`org.springframework.web.servlet.DispatcherServlet`

스프링 MVC도 프론트 컨트롤러 패턴으로 구현되어 있다.
스프링 MVC의 프론트 컨트롤러가 바로 디스패처 서블릿(DispatcherServlet)이다.
그리고 이 디스패처 서블릿이 바로 스프링 MVC의 핵심

**DispatcherServlet 서블릿 등록**
- `DispatcherServlet`도 부모 클래스에서 `HttpServlet`을 상속 받아서 사용하고 서블릿으로 동작한다.
	- DispatcherServlet -> FrameworkServlet -> HttpServletBean -> HttpServlet
- 스프링 부트는 `DispatcherServlet`을 서블릿으로 자동으로 등록하면서 **모든 경로(`urlPatterns="/")`** 에 대해서 매핑한다.
	- 참고: 더 자세한 경로가 우선 순위가 높다. 그래서 기존에 등록한 서블릿도 함께 동작한다.

**요청 흐름**
- 서블릿이 호출되면 `HttpServlet`이 제공하는 `service()`가 호출된다.
- 스프링 MVC는 `DispatcherServlet`의 부모인 `FrameworkServlet`에서 `service()`를 오버라이드 해두었다.
- `FrameworkServlet.service()`를 시작으로 여러 메서드가 호출되면서 `DispatcherServlet.doDispatch()`가 호출된다.

지금부터 `DispatcherServlet`의 핵심인 `doDispatch()` 코드를 분석해보자. 
최대한 간단히 설명하기 위해 예외 처리, 인터셉터 기능은 제외했다.

>참고:
>![[Pasted image 20250608215942.png]]


`DispatcherServlet.doDispatch()`
```java
protected void doDispatch(HttpServletRequest request, HttpServletResponse response) throws Exception {
    HttpServletRequest processedRequest = request;
    HandlerExecutionChain mappedHandler = null;
    ModelAndView mv = null;

    // 1. 핸들러 조회
    mappedHandler = getHandler(processedRequest);
    if (mappedHandler == null) {
        noHandlerFound(processedRequest, response);
        return;
    }

    // 2. 핸들러 어댑터 조회 - 핸들러를 처리할 수 있는 어댑터
    HandlerAdapter ha = getHandlerAdapter(mappedHandler.getHandler());

    // 3. 핸들러 어댑터 실행 -> 4. 핸들러 어댑터를 통해 핸들러 실행 -> 5. ModelAndView 반환
    mv = ha.handle(processedRequest, response, mappedHandler.getHandler());

    processDispatchResult(processedRequest, response, mappedHandler, mv, null);
}

// into--- 

private void processDispatchResult(
        HttpServletRequest request,
        HttpServletResponse response,
        HandlerExecutionChain mappedHandler,
        ModelAndView mv,
        Exception exception) throws Exception {

    // 뷰 렌더링 호출
    render(mv, request, response);
}

// into---

protected void render(
        ModelAndView mv,
        HttpServletRequest request,
        HttpServletResponse response) throws Exception {

    View view;
    String viewName = mv.getViewName();

    // 6. 뷰 리졸버를 통해서 뷰 찾기, 7. View 반환
    view = resolveViewName(viewName, mv.getModelInternal(), locale, request);

    // 8. 뷰 렌더링
    view.render(mv.getModelInternal(), request, response);
}

```

**Spring MVC 구조**
![[Pasted image 20250609001117.png]]

**동작 순서**
1. **핸들러 조회**: 핸들러 매핑을 통해서 요청 URL에 매핑된 핸들러(컨트롤러)를 조회한다.
2. **핸들러 어댑터 조회**: 핸들러를 실행할 수 있는 핸들러 어댑터를 조회한다.
3. **핸들러 어댑터 실행**: 핸들러 어댑터를 실행한다.
4. **핸들러 실행**: 핸들러 어댑터가 실제 핸들러를 실행한다.
5. **ModelAndView 반환**: 핸들러 어댑터는 핸들러가 반환하는 정보를 ModelAndView로 **변환**해서 반환한다.
6. **viewResolver 호출**: 뷰 리졸버를 찾고 실행한다.
	- JSP의 경우: `InternalResourceViewResolver`가 자동 등록되고 사용된다.
7. **View 반환**: 뷰 리졸버는 뷰의 논리 이름을 물리 이름으로 바꾸고 렌더링 역할을 담당하는 뷰 객체를 반환한다.
8. **뷰 렌더링**: 뷰를 통해서 뷰를 렌더링한다.

**인터페이스 살펴보기**
- 스프링 MVC의 큰 강점은 `DispatcherServlet` 코드의 변경 없이 원하는 기능을 변경하거나 확장할 수 있다는 점이다.
- 지금까지 설명한 대부분을 확장 가능할 수 있게 인터페이스로 제공한다.
- 이 인터페이스들만 구현해서 `DispatcherServlet`에 등록하면 나만의 컨트롤러를 만들 수도 있다.


**정리**
	스프링 MVC는 코드 분량도 매우 많고, 복잡해서 내부 구조를 다 파악하는 것은 쉽지 않다.
	사실 해당 기능을 직접 확장 하거나 나만의 컨트롤러를 만드는 일은 없으므로 걱정하지 않아도 된다.
	왜냐하면 스프링 MVC는 전세계 수 많은 개발 자들의 요구사항에 맞추어 기능을 계속 확장해왔고, 그래서 여러분이 웹 애플리케이션을 만들 때 필요로 하는 대부분의 기능이 이미 다 구현되어 있다.
	그래도 이렇게 핵심 동작방식을 알아두어야 향후 문제가 발생했을 때 어떤 부분에서 문제가 발생했는지 쉽게 파악하고, 문제를 해결할 수 있다. 그리고 확장 포인트가 필요할 때, 어떤 부분을 확장해야 할지 감을 잡을 수 있다.
	실제 다른 컴포 넌트를 제공하거나 기능을 확장하는 부분들은 강의를 진행하면서 조금씩 설명하겠다. 지금은 전체적인 구조가 이렇게 되어 있구나 하고 이해하면 된다. 우리가 지금까지 함께 개발한 MVC 프레임워크와 유사한 구조여서 이해하기 어렵지 않았을 것이다.                                                                                                                                                                                                       

## 핸들러 매핑과 핸들러 어댑터
핸들러 매핑과 핸들러 어댑터가 어떤 것들이 어떻게 사용되는지 알아보자.
지금은 전혀 사용하지 않지만, 과거에 주로 사용했던 스프링이 제공하는 간단한 컨트롤러로 핸들러 매핑과 어댑터를 이해해보자.

#### Controller 인터페이스
**과거 버전 스프링 컨트롤러**
```java
public interface Controller {

	ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception;
	
}
```
스프링도 처음에는 이렇게 딱딱한 형식의 컨트롤러를 제공했다.

>참고
>`Controller` 인터페이스는 `@Controller` 애노테이션과는 전혀 다른 것이다.


```java
package hello.servlet.web.springmvc.old;  
  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
  
import org.springframework.stereotype.Component;  
import org.springframework.web.servlet.ModelAndView;  
import org.springframework.web.servlet.mvc.Controller;  
  
@Component("/springmvc/old-controller")  
public class OldController implements Controller {  
    @Override  
    public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {  
        System.out.println("OldController.handleRequest");  
        return null;  
    }  
}
```

**실행**
- `http://localhost:8080/springmvc/old-controller`
- 콘솔에 `OldController.handleRequest`가 출력되면 성공

**이 컨트롤러는 어떻게 호출될 수 있었을까?**
![[Pasted image 20250609233338.png]]

이 컨트롤러가 호출되려면 다음 2가지 요소가 필요하다.

- **HandlerMapping(핸들러 매핑)**
	- 핸들러 매핑에서 이 컨트롤러를 찾을 수 있어야 한다.
	- 예) **스프링 빈의 이름으로 핸들러를 찾을 수 있는 핸들러 매핑**이 필요하다.
		- `BeanNameUrlHandlerMapping`
		- `private final Map<String, Object> handlerMappingMap = new HashMap<>();`
- **HandlerAdapter(핸들러 어댑터)
	- 핸들러 매핑을 통해서 찾은 핸들러를 실행할 수 있는 핸들러 어댑터가 필요하다.
	- 예) `Controller` **인터페이스(애노테이션 X)** 를 실행할 수 있는 핸들러 어댑터를 찾고 실행해야 한다.
		- `SimpleControllerHandlerAdapter`
		- `supports`, `handle`

스프링은 이미 필요한 핸들러 매핑과 핸들러 어댑터를 대부분 구현해두었다. 개발자가 직접 핸들러 매핑과 핸들러 어댑터를 만드는 일은 거의 없다.


**스프링 부트가 자동으로 등록하는 핸들러 매핑과 핸들러 어댑터**

#### HandlerMapping

| 우선순위 | 이름                           | 설명                                       |
| ---- | ---------------------------- | ---------------------------------------- |
| 1    | RequestMappingHandlerMapping | 애노테이션 기반의 컨트롤러인 `@RequestMapping`  에서 사용 |
| 2    | BeanNameUrlHandlerMapping    | 스프링 빈 이름으로 핸들러를 찾음                       |

#### HandlerAdapter

| 우선순위 | 이름                             | 설명                                       |
| ---- | ------------------------------ | ---------------------------------------- |
| 1    | RequestMappingHandlerAdapter   | 애노테이션 기반의 컨트롤러인 `@RequestMapping`  에서 사용 |
| 2    | HttpRequestHandlerAdapter      | HttpRequestHandler 타입 컨트롤러 처리            |
| 3    | SimpleControllerHandlerAdapter | Controller 인터페이스(애노테이션X, 과거 방식) 컨트롤러 처리  |

핸들러 매핑도, 핸들러 어댑터도 모두 순서대로 찾아보고, 만약에 없으면 다음 순서로 넘어간다.

**1. 핸들러 매핑으로 핸들러 조회**
1. `HandlerMapping`을 순서대로 실행해서 핸들러를 찾는다.
2. 이 경우 빈 이름으로 핸들러를 찾아야 하기 때문에, 이름 그대로 `빈 이름`으로 핸들러를 찾아주는 `BeanNameUrlHandlerMapping`가 실행에 성공하고 핸들러인 `OldController`를 반환한다. (예시) 

**2. 핸들러 어댑터 조회**
1. `HandlerAdapter`의 `supports()`를 순서대로 호출한다.
2. `SimpleControllerHandlerAdapter`가 `Controller` 인터페이스를 지원하므로 대상이 된다.

**3. 핸들러 어댑터 실행**
1. 디스패처 서블릿이 조회한 `SimpleControllerHandlerAdapter`를 실행하면서 핸들러 정보도 함께 넘겨준다.
2. `SimpleControllerHandlerAdapter`는 핸들러인 `OldController`를 내부에서 실행하고 그 결과를 반환한다.

**정리 - OldController 핸들러 매핑, 어댑터**
`OldController`를 실행하면서 사용된 객체는 다음과 같다.
`HandlerMapping = BeanNameUrlHandlerMapping`
`HandlerAdapter = SimpleControllerHandlerAdapter`

---

>참고

| 용어           | 정의 및 역할                                               | 예시/비고                             |
| ------------ | ----------------------------------------------------- | --------------------------------- |
| **서블릿 컨테이너** | 서블릿(자바 웹 컴포넌트)의 생성, 실행, 생명주기 관리 및 HTTP 요청/응답 처리 담당    | 톰캣, 제티 등. 웹 서버와 연동, HTTP 통신 지원    |
| **스프링 컨테이너** | 스프링 빈(객체)의 생성, 의존성 주입, 생명주기 관리 등 애플리케이션 로직의 객체 관리 담당  | ApplicationContext, BeanFactory 등 |
| **디스패처 서블릿** | 스프링이 제공하는 프론트 컨트롤러 서블릿. 모든 웹 요청을 받아 컨트롤러로 분배, 응답까지 조정 | DispatcherServlet 클래스. "/" 경로에 매핑 |
| **프론트 컨트롤러** | 모든 웹 요청을 하나의 진입점에서 받아 공통 로직 처리 후, 적절한 컨트롤러로 위임하는 패턴   | 스프링에서는 DispatcherServlet이 대표적 구현체 |


- **서블릿 컨테이너**
    
    - 자바 웹 표준 기술.
        
    - HTTP 요청을 받아 서블릿 객체(service(), doGet(), doPost() 등)를 실행하고 응답을 반환
        
    - 웹 서버와의 통신, 멀티스레드 관리 등도 담당.
        
- **스프링 컨테이너**
    
    - 스프링 프레임워크의 핵심.
        
    - @Component, @Service, @Controller 등으로 등록된 객체(빈)를 생성·관리·의존성 주입
        
    - 비즈니스 로직, 서비스 계층 등 애플리케이션의 내부 객체 관리.
        
- **디스패처 서블릿**
    
    - 스프링 MVC의 프론트 컨트롤러 서블릿.
        
    - 서블릿 컨테이너(톰캣 등)에 의해 실행되며, 모든 HTTP 요청을 받아 스프링 컨트롤러로 분배[
        
    - 요청 → 핸들러 매핑 → 컨트롤러 실행 → 뷰 처리 → 응답의 전체 흐름을 조정.
        
- **프론트 컨트롤러**
    
    - 모든 웹 요청을 하나의 진입점에서 받아 공통로직(인증, 로깅 등) 처리 후, 각 컨트롤러로 위임하는 디자인 패턴
        
    - 스프링 MVC에서는 DispatcherServlet이 프론트 컨트롤러 역할을 수행.
        
## 관계도

- **서블릿 컨테이너**가 HTTP 요청을 받아 **디스패처 서블릿(프론트 컨트롤러)**을 실행
    
- **디스패처 서블릿**이 스프링 내부의 **스프링 컨테이너**에서 관리하는 컨트롤러(빈)를 찾아 요청 처리
    
- **프론트 컨트롤러**는 디자인 패턴 용어이며, 스프링에서는 DispatcherServlet이 그 구현체
    


---

하나의 예시를 더 들어보자.

#### HttpRequestHandler
```
HandlerAdapter
1 = HttpRequestHandlerAdapter : HttpRequestHandler 처리
```

핸들러 매핑과 어댑터를 더 잘 이해하기 위해서 Controller 인터페이스가 아닌 다른 핸들러를 알아보자.
`HttpRequestHandler` 핸들러(컨트롤러)는 **서블릿과 가장 유사한 형태**의 핸들러이다.

**HttpRequestHandler**
```java
@Component("/springmvc/request-handler")  
public class MyHttpRequestHandler implements HttpRequestHandler {  
    @Override  
    public void handleRequest(HttpServletRequest request, HttpServletResponse response)  
            throws ServletException, IOException {  
        System.out.println("MyHttpRequestHandler.handleRequest");  
    }  
}
```

**실행**
- `http://localhost:8080/springmvc/request-handler`
- 웹 브라우저에 빈 화면이 나오고 콘솔에 `MyHttpRequestHandler.handleRequest`가 출력되면 성공이다.

**1. 핸들러 매핑으로 핸들러 조회**
1. `HandlerMapping`을 순서대로 실행해서 핸들러를 찾는다.
2. 이 경우 빈 이름으로 핸들러를 찾아야 하기 때문에, 이름 그대로 `빈 이름`으로 핸들러를 찾아주는 `BeanNameUrlHandlerMapping`가 실행에 성공하고 핸들러인 `MyHttpRequestHandler`를 반환한다.

**2. 핸들러 어댑터 조회**
1. `HandlerAdapter`의 `supports()`를 순서대로 호출한다.
2. `MyRequestHandlerAdapter`가 `HttpRequestHandler` 인터페이스를 지원하므로 대상이 된다.

**3. 핸들러 어댑터 실행**
1. 디스패처 서블릿이 조회한 `HttpRequestHandlerAdapter`를 실행하면서 핸들러 정보도 함께 넘겨준다.
2. `HttpRequestHandlerAdapter`는 핸들러인 `MyHttpRequestHandler`를 내부에서 실행하고 그 결과를 반환한다.

**정리 - MyHttpRequestHandler 핸들러 매핑, 어댑터**
`MyHttpRequestHandler`를 실행하면서 사용된 객체는 다음과 같다.
`HandlerMapping = BeanNameUrlHandlerMapping`
`HandlerAdapter = HttpRequestHandlerAdapter`


**`@RequestMapping`**
조금 뒤에서 설명하겠지만, 가장 우선 순위가 높은 핸들러 매핑과 핸들러 어댑터는 `RequestMappingHandlerMapping`, `RequestMappingHandlerAdapter`이다.
- `@RequestMapping`의 앞글자를 따서 만든 이름인데, 이것이 바로 지금 스프링에서 주로 사용하는 애노테이션 기반의 컨트롤러를 지원하는 매핑과 어댑터이다.
- 실무에서는 사실 99.9% 이 방식의 컨트롤러를 사용한다.

## 뷰 리졸버

스프링 부트는 `InternalResourceViewResolver`라는 뷰 리졸버를 자동으로 등록하는데, 이때 `application.properties`에 등록한 `spring.mvc.view.prefix`, `spring.mvc.view.suffix` 설정 정보를 사용해서 등록한다.

참고로 권장하지는 않지만 설정 없이 다음과 같이 전체 경로를 주어도 동작하기는 한다.
`return new ModelAndView("/WEB-INF/views/new-form.jsp);`

**뷰 리졸버 동작 방식**
![[Pasted image 20250611205205.png]]

**스프링 부트가 자동 등록하는 뷰 리졸버**
(실제로는 더 많지만, 중요한 부분 위주로 설명하기 위해 일부 생략)
```
1 = BeanNameViewResolver         : 빈 이름으로 뷰를 찾아서 반환한다. (예: 엑셀 파일 생성 기능에 사용) 
2 = InternalResourceViewResolver : JSP를 처리할 수 있는 뷰를 반환한다.
```


**1. 핸들러 어댑터 호출**
핸들러 어댑터를 통해 `new-form`이라는 논리 뷰 이름을 획득한다.

**2. ViewResolver 호출**
- `new-form`이라는 뷰 이름으로 viewResolver 리스트를 순서대로 호출한다.
- `BeanNameViewResolver`는 `new-form`이라는 이름의 스프링 빈으로 등록된 뷰를 찾아야 하는데 없다.
- `InternalResourceViewResolver`가 호출된다.

**3. InternalResourceViewResolver**
이 뷰 리졸버는 `InternalResourceView`를 반환한다.

**4. 뷰 - InternalResourceView**
`InternalResourceView`는 JSP 처럼 포워드 `forward()`를 호출해서 처리할 수 있는 경우에 사용한다.

**5. view.render()**
`view.render()`가 호출되고 `InternalResourceView`는 `forward()`를 사용해서 JSP를 실행한다.


>참고
>`InternalResourceViewResolver`는 만약 JSTL 라이브러리가 있으면 `InternalResource`를 상속받은 `JstlView`를 반환한다. `JstlView`는 JSTL 태그 사용 시 약간의 부가 기능이 추가된다.

>참고
>다른 뷰는 실제 뷰를 렌더링 하지만, JSP 경우의 `forward()`를 통해서 해당 JSP로 이동(실행)해야 렌더링이 된다. JSP를 제외한 나머지 뷰 템플릿들은 `forward()` 과정 없이 바로 렌더링 된다.

>참고
>Thymeleaf 뷰 템플릿을 사용하면 `ThymeleafViewResolver`를 등록해야 한다. 최근에는 라이브러리만 추가하면 스프링 부트가 이런 작업도 모두 자동화 해줬다.


## 스프링 MVC - 시작하기
스프링이 제공하는 컨트롤러는 애노테이션 기반으로 동작해서 매우 유연하고 실용적이다.
과거에는 자바 언어에 애노테이션이 없기도 했고 스프링도 처음부터 이런 유연한 컨트롤러를 제공한 것은 아니다.

**@RequestMapping**
스프링은 애노테이션을 활용한 매우 유연하고 실용적인 컨트롤러를 만들었는데 이것이 바로 `@RequestMapping` 애노태에션을 사용하는 컨트롤러이다.
여담이지만, 과거에는 스프링 프레임워크가 MVC 부분이 약해서 스프링을 사용하더라도 MVC 웹 기술은 스트럿츠 같은 다른 프레임워크를 사용했었다. 그런데, `@RequestMapping` 기반의 애노테이션 컨트롤러가 등장하면서 MVC 부분도 스프링의 완승으로 끝이 났다.

`@RequestMapping`
- `RequestMappingHandlerMapping`
- `RequestMappingHandlerAdapter`

앞서 보았듯이 가장 우선순위가 높은 핸들러 매핑과 핸들러 어댑터는 `RequestMappingHandlerMapping`, `RequestMappingHandlerAdapter`이다.
`@RequestMapping`의 앞글자를 따서 만든 이름인데 이것이 바로 지금 스프링에서 주로 사용하는 애노테이션 기반의 컨트롤러를 지원하는 핸들러 매핑과 어댑터이다. **실무에서는 99.9% 이 방식의 컨트롤러를 사용**한다.

그럼 이제 본격적으로 애노테이션 기반의 컨트롤러를 사용해보자.
지금까지 만들었던 프레임워크에서 사용했던 컨트롤러를 `@RequestMapping` 기반의 스프링 MVC 컨트롤러로 변경해보자.

`SpringMemberFormControllerV1 - 회원 등록 폼`
```java
package hello.servlet.web.springmvc.v1;  
  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.servlet.ModelAndView;  
  
@Controller  
public class SpringMemberFormControllerV1 {  
  
    @RequestMapping("/springmvc/v1/members/new-form")  
    public ModelAndView process() {  
        return new ModelAndView("new-form");  
    }  
  
}
```
- `@Controller`
	- 스프링이 자동으로 스프링 빈으로 등록한다. (내부에 `@Component` 애노테이션이 있어서 컴포넌트 스캔의 대상이 됨)
	- 스프링 MVC에서 애노테이션 기반 컨트롤러로 인식한다. (`RequestMappingHandlerMapping`이 해당 클래스를 스캔할 수 있도록 함)
- `@RequestMapping`
	- 요청 정보를 매핑한다.
	- 해당 URL이 호출되면 이 메서드가 호출된다.
	- 애노테이션을 기반으로 동작하기 때문에 메서드의 이름은 임의로 지어도 된다.
- `ModelAndView`
	- 모델과 뷰 정보를 담아서 반환하면 된다.

`RequestMappingHandlerMapping`은 스프링 빈 중에서 `@RequestMapping` 또는 `@Controller`가 클래스 레벨에 붙어 있는 경우에 매핑 정보로 인식한다.

따라서 다음 코드도 동일하게 동작한다.

```java
package hello.servlet.web.springmvc.v1;  
  
import org.springframework.stereotype.Component;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.servlet.ModelAndView;  
  
// @Controller  
@Component  // 클래스 레벨
@RequestMapping  
public class SpringMemberFormControllerV1 {  

	// 메서드 레벨
    @RequestMapping("/springmvc/v1/members/new-form")  
    public ModelAndView process() {  
        return new ModelAndView("new-form");  
    }  
  
}
```

그 이유는?
``
`RequestMappingHandlerMapping.isHandler()`
```java
@Override
protected boolean isHandler(Class<?> beanType) {
	return (AnnotatedElementUtils.hasAnnotation(beanType, Controller.class) ||
			AnnotatedElementUtils.hasAnnotation(beanType, RequestMapping.class));
}
```

`ServletApplication`
```java
package hello.servlet;  
  
import hello.servlet.web.springmvc.v1.SpringMemberFormControllerV1;  
import org.springframework.boot.SpringApplication;  
import org.springframework.boot.autoconfigure.SpringBootApplication;  
import org.springframework.boot.web.servlet.ServletComponentScan;  
import org.springframework.context.annotation.Bean;  
import org.springframework.web.servlet.ViewResolver;  
import org.springframework.web.servlet.view.InternalResourceViewResolver;  
  
@ServletComponentScan // 자동으로 패키지 내의 서블릿을 찾은 뒤 실행할 수 있게끔 만들어줌  
@SpringBootApplication  
public class ServletApplication {  
  
    public static void main(String[] args) {  
       SpringApplication.run(ServletApplication.class, args);  
    }  
  
    // 스프링 부트가 자동으로 처리해줌  
//  @Bean  
//  InternalResourceViewResolver internalResourceViewResolver() {  
//     return new InternalResourceViewResolver("/WEB-INF/views/", ".jsp");  
//  }  

	// @Component 대신, 스프링 빈으로 직접 등록해도 됨 (SpringMemberFormControllerV1)
    @Bean  
    SpringMemberFormControllerV1 springMemberFormControllerV1() {  
       return new SpringMemberFormControllerV1();  
    }  
}
```
- 스프링 빈을 직접 등록 해줘도 당연히 가능함

**결국?**
- `@Controller` 를 사용하면 됨.
	- 컴포넌트 스캔의 대상으로 자동 등록됨 (내부에 `@Component`를 상속 받고 있음)
	- `RequestMappingHandlerMapping`에서 `@Controller`가 붙은 클래스를 **핸들러로** 인식함

스프링에서는 **애노테이션 위에 다른 애노테이션을 붙이는 방식**으로 기능을 확장함.
- **메타 애노테이션(Meta-Annotation)**
	- 즉, `@Controller` 위에 `@Component`가 붙어 있으면 `@Controller`는 **자동으로 `@Component`의 기능도 갖는다**는 뜻.

> 참고
> 메타 애노테이션
``` java
@Target(ElementType.TYPE) // 클래스, 인터페이스, enum에 붙일 수 있음
@Retention(RetentionPolicy.RUNTIME) // 런타임까지 유지됨
@Documented
@Component // 이 어노테이션이 붙으면 스프링이 컴포넌트로 인식
public @interface Service {
}
```
- 이처럼, `애노테이션`에 붙일 수 있는 `애노테이션`을 **메타 애노테이션**이라 함.
	- `@Service` : 애노테이션
		- `@Component` : 메타 애노테이션
		- `@Documented` : 메타 애노테이션
		- `@Retention` : 메타 애노테이션
		- `@Target` : 메타 애노테이션
		- ...


---
**V1 버전**

`SpringMemberFormControllerV1`
```java
package hello.servlet.web.springmvc.v1;  
  
import org.springframework.stereotype.Component;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.servlet.ModelAndView;  
  
@Controller  
public class SpringMemberFormControllerV1 {  
  
    @RequestMapping("/springmvc/v1/members/new-form")  
    public ModelAndView process() {  
        return new ModelAndView("new-form");  
    }  
  
}
```

`SpringMemberSaveControllerV1`
```java
package hello.servlet.web.springmvc.v1;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.util.Map;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.servlet.ModelAndView;  
  
@Controller  
public class SpringMemberSaveControllerV1 {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @RequestMapping("/springmvc/v1/members/save")  
    public ModelAndView process(HttpServletRequest request, HttpServletResponse response) throws Exception {  
        String username = request.getParameter("username");  
        int age = Integer.parseInt(request.getParameter("age"));  
  
        Member member = new Member(username, age);  
        memberRepository.save(member);  
  
        ModelAndView mv = new ModelAndView("save-result");  
        // mv.getModel().put("member", member);  
        mv.addObject("member", member);  
        return mv;  
    }  
}
```

`SpringMemberListControllerV1`
```java
package hello.servlet.web.springmvc.v1;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import java.util.List;  
import java.util.Map;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.servlet.ModelAndView;  
  
@Controller  
public class SpringMemberListControllerV1 {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @RequestMapping("/springmvc/v1/members")  
    public ModelAndView process() {  
        List<Member> members = memberRepository.findAll();  
  
        ModelAndView mv = new ModelAndView("members");  
        // mv.getModel().put("members", members);  
        mv.addObject("members", members);  
        return mv;  
    }  
}
```

## 스프링 MVC - 컨트롤러 통합
`@RequestMapping`을 잘 보면 클래스 단위가 아니라 메서드 단위에 적용된 것을 확인할 수 있다.
따라서 컨트롤러 클래스를 유연하게 하나로 통합할 수 있다.

```java
package hello.servlet.web.springmvc.v2;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.util.List;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.servlet.ModelAndView;  
  
@Controller  
public class SpringMemberControllerV2 {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @RequestMapping("/springmvc/v2/members/new-form")  
    public ModelAndView newForm() {  
        return new ModelAndView("new-form");  
    }  
  
    @RequestMapping("/springmvc/v2/members/save")  
    public ModelAndView save(HttpServletRequest request, HttpServletResponse response) throws Exception {  
        String username = request.getParameter("username");  
        int age = Integer.parseInt(request.getParameter("age"));  
  
        Member member = new Member(username, age);  
        memberRepository.save(member);  
  
        ModelAndView mv = new ModelAndView("save-result");  
        // mv.getModel().put("member", member);  
        mv.addObject("member", member);  
        return mv;  
    }  
  
    @RequestMapping("/springmvc/v2/members")  
    public ModelAndView members() {  
        List<Member> members = memberRepository.findAll();  
  
        ModelAndView mv = new ModelAndView("members");  
        // mv.getModel().put("members", members);  
        mv.addObject("members", members);  
        return mv;  
    }  
}
```
- 작동도 잘 되지만, 중복이 조금 있다.
	- `/springmvc/v2/members/`

```java

@Controller  
@RequestMapping("/springmvc/v2/members")  
public class SpringMemberControllerV2 {  

    @RequestMapping("/new-form")  
    public ModelAndView newForm() {}  
  
    @RequestMapping("/save")  
    public ModelAndView save() {}  
  
    @RequestMapping
    public ModelAndView members() {}  
  
}
```
- 핵심 코드만 요약.
- 클래스 레벨에 `@RequestMapping`을 걸어주고 중복되는 부분을 설정해주면 됨.

**완성은 했지만...**
뭔가 `ModelAndView`를 계속 만들어서 반환해야 하기에 뭔가 불편함.
- 이전에 V3 -> V4 로 업그레이드 하는 과정을 기억해보자.
	- 논리적인 뷰 이름을 반환해주고 그걸 뷰 리졸버를 통해서 물리적인 주소로 변환했던 것

**조합**
컨트롤러 클래스를 통합하는 것을 넘어서 조합도 가능하다.
다음 코드는 `/springmvc/v2/members` 라는 부분에 중복이 있다.

- `@RequestMapping("/springmvc/v2/members/new-form")`
- `@RequestMapping("/springmvc/v2/members/save")`
- `@RequestMapping("/springmvc/v2/members")`

물론 이렇게 사용해도 되지만, 컨트롤러를 통합한 예제 코드를 보면 중복을 어떻게 제거했는지 확인할 수 있다.
클래스 레벨에서 다음과 같이 `@RequestMapping`을 두면 메서드 레벨과 조합이 된다.

```java
@Controller
@RequestMapping("/springmvc/v2/members")
public class SpringMemberControllerV2 {}
```

**조합 결과**
- `클래스 레벨 @RequestMapping("/springmvc/v2/members")`
	- `메서드 레벨`
	- `@RequestMapping("/new-form")` -> `/springmvc/v2/members/new-form`
	- `메서드 레벨`
	- `@RequestMapping` -> `/springmvc/v2/members`
	- `메서드 레벨`
	- `@RequestMapping("/save")` -> `/springmvc/v2/members/save"`

## 스프링 MVC - 실용적인 방식

MVC 프레임워크 만들기에서 v3는 ModelView를 개발자가 직접 생성해서 반환했기 때문에 불편했던 기억이 있을 것이다.
물론 v4를 만들면서 실용적으로 개선한 기억도 있을 것이다.

스프링 MVC는 개발자가 편리하게 개발할 수 있도록 수 많은 편의 기능을 제공한다.
**실무에서는 지금부터 설명하는 방식을 주로 사용한다.**

**SpringMemberControllerV3**
```java
package hello.servlet.web.springmvc.v3;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import java.util.List;  
import org.springframework.stereotype.Controller;  
import org.springframework.ui.Model;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RequestParam;  
  
@Controller  
@RequestMapping("/springmvc/v3/members")  
public class SpringMemberControllerV3 {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @RequestMapping("/new-form")  
    public String newForm() {  
        return "new-form"; 
        }  
  
    @RequestMapping("/save")  
    public String save(  
            @RequestParam("username") String username,  
            @RequestParam("age") int age,  
            Model model) {  
  
        Member member = new Member(username, age);  
        memberRepository.save(member);  
  
        model.addAttribute("member", member);  
        return "save-result";  
    }  
  
    @RequestMapping  
    public String members(Model model) {  
        List<Member> members = memberRepository.findAll();  
  
        model.addAttribute("members", members);  
  
        return "members";  
    }  
}
```

```text
- 스프링의 애노테이션 기반 컨트롤러는 ModelAndView를 반환해도 되고 문자를 반환해도 됨.
	- (별도 세팅 없이 스프링 부트를 통해.)

- HandlerAdapter가 판단함.
- @RequestMapping 메서드의 반환 값 타입에 따라서 다르게 작동  
	- ModelAndView -> 그 안의 뷰 이름, 모델을 사용  
	- String -> 뷰 이름으로 간주  
	- @ResponseBody -> 응답 본문으로 간주 (ex: JSON)
```

- 하나의 문제가 더 있다.
- 지금까지는 HTTP Method를 구분하지 않았다. (GET, POST, PUT, DELETE)
- 딱 봐도 좋은 개발 방법은 아님.

![[Pasted image 20250622231646.png]]

![[Pasted image 20250622231700.png]]


아래와 같이 해결 가능
```java
package hello.servlet.web.springmvc.v3;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import java.util.List;  
import org.springframework.stereotype.Controller;  
import org.springframework.ui.Model;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RequestMethod;  
import org.springframework.web.bind.annotation.RequestParam;  
  
@Controller  
@RequestMapping("/springmvc/v3/members")  
public class SpringMemberControllerV3 {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @RequestMapping(value = "/new-form", method = RequestMethod.GET)  
    public String newForm() {  
        return "new-form";
        }  
  
    @RequestMapping(value = "/save", method = RequestMethod.POST)  
    public String save(  
            @RequestParam("username") String username,  
            @RequestParam("age") int age,  
            Model model) {  
  
        Member member = new Member(username, age);  
        memberRepository.save(member);  
  
        model.addAttribute("member", member);  
        return "save-result";  
    }  
  
    @RequestMapping(method = RequestMethod.GET)  
    public String members(Model model) {  
        List<Member> members = memberRepository.findAll();  
  
        model.addAttribute("members", members);  
  
        return "members";  
    }  
}
```

이마저도 단축한다면?
```java
package hello.servlet.web.springmvc.v3;  
  
import hello.servlet.domain.member.Member;  
import hello.servlet.domain.member.MemberRepository;  
import java.util.List;  
import org.springframework.stereotype.Controller;  
import org.springframework.ui.Model;  
import org.springframework.web.bind.annotation.GetMapping;  
import org.springframework.web.bind.annotation.PostMapping;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RequestMethod;  
import org.springframework.web.bind.annotation.RequestParam;  
  
@Controller  
@RequestMapping("/springmvc/v3/members")  
public class SpringMemberControllerV3 {  
  
    private MemberRepository memberRepository = MemberRepository.getInstance();  
  
    @GetMapping("/new-form")  
    public String newForm() {  
        return "new-form"; // 스프링의 애노테이션 기반 컨트롤러는 ModelAndView를 반환해도 되고 문자를 반환해도 됨. (별도 세팅 없이 스프링 부트를 통해.)  
        // HandlerAdapter가 판단함.  
        // @RequestMapping 메서드의 반환 값 타입에 따라서 다르게 작동  
        // ModelAndView -> 그 안의 뷰 이름, 모델을 사용  
        // String -> 뷰 이름으로 간주  
        // @ResponseBody -> 응답 본문으로 간주 (ex: JSON)    }  
  
    @PostMapping("/save")  
    public String save(  
            @RequestParam("username") String username,  
            @RequestParam("age") int age,  
            Model model) {  
  
        Member member = new Member(username, age);  
        memberRepository.save(member);  
  
        model.addAttribute("member", member);  
        return "save-result";  
    }  
  
    @GetMapping  
    public String members(Model model) {  
        List<Member> members = memberRepository.findAll();  
  
        model.addAttribute("members", members);  
  
        return "members";  
    }  
}
```
- `@GetMapping`, `@PostMapping`

### **핵심 정리**

**Model 파라미터**
- `save()`, `members()` 를 보면 Model을 파라미터로 받는 것을 확인할 수 있다.
- 스프링 MVC도 이런 편의 기능을 제공한다.

**ViewName 직접 반환**
- 뷰의 논리 이름을 반환할 수 있다.

**@RequestParam 사용**
스프링은 HTTP 요청 파라미터를 `@RequestParam`으로 받을 수 있다.
- `@RequestParam("username")`은 `request.getParameter("username")`과 거의 같은 코드라 생각하면 된다.
- 물론 GET 쿼리 파라미터, POST Form 방식을 모두 지원한다.

**@RequestMapping -> @GetMapping, @PostMapping**
- `@RequestMapping`은 URL만 매칭하는 것이 아니라, HTTP Method도 함께 구분할 수 있다.
- 예를 들어서 URL이 `/new-form`이고, HTTP Method가 GET인 경우를 모두 만족하는 매핑을 하려면 다음과 같이 처리하면 된다.

```java
@RequestMapping(value = "/new-form", method = RequestMethod.GET)
```

이것을 `@GetMapping`, `@PostMapping`으로 더 편리하게 사용할 수 있다.
참고로 GET, POST, PUT, DELETE, PATCH 모두 애노테이션이 준비되어 있다.

`@GetMapping` 코드를 열어서 `@RequestMapping` 애노테이션을 내부에 가지고 있는 모습도 확인해보자!

```java
@Target(ElementType.METHOD)  
@Retention(RetentionPolicy.RUNTIME)  
@Documented  
@RequestMapping(method = RequestMethod.GET)    // 🔥 메타 애노테이션!
public @interface GetMapping {  
  
    /**  
     * Alias for {@link RequestMapping#name}.  
     */    @AliasFor(annotation = RequestMapping.class)  
    String name() default "";  
  
    /**  
     * Alias for {@link RequestMapping#value}.  
     */    @AliasFor(annotation = RequestMapping.class)  
    String[] value() default {};

// 후략
```
- `@GetMapping` 내에 `@RequestMapping`이 메타 애노테이션으로 들어가있는 것을 확인 가능.
	- `@RequestMapping(method = RequestMethod.GET)`

> 참고
> 메타 애노테이션

|애노테이션|설명|
|---|---|
|`@Target`|이 애노테이션이 어디에 붙을 수 있는지 지정 (클래스, 메서드 등)|
|`@Retention`|런타임까지 유지할지 여부 등|
|`@Documented`|JavaDoc에 포함 여부|
|`@Inherited`|상속 가능 여부|
|✅ `@RequestMapping`|커스텀 애노테이션 구성 요소로 사용될 수 있음 → 이게 핵심|

---

## 정리

### 스프링 MVC에서 HTTP 요청을 가장 먼저 받아 처리하는 핵심 컴포넌트는 무엇일까요?

1. HandlerMapping
2. HandlerAdapter
3. DispatcherServlet
4. ViewResolver

해설
3. DispatcherServlet
스프링 MVC에서 모든 HTTP 요청은 이 컴포넌트를 통해 들어옵니다. 여러 요청을 하나의 진입점에서 처리하는 전면 컨트롤러 패턴을 구현해요.


### DispatcherServlet 이후, 요청 처리를 위해 일반적으로 Handler를 찾고 실행한 뒤 View를 찾는 과정에서 핵심적인 순서는 무엇인가요?

1. HandlerMapping → ViewResolver → HandlerAdapter
2. HandlerAdapter → HandlerMapping → ViewResolver
3. HandlerMapping → HandlerAdapter → ViewResolver
4. ViewResolver → HandlerMapping → HandlerAdapter

해설
3. HandlerMapping → HandlerAdapter → ViewResolver
DispatcherServlet은 요청을 받으면 HandlerMapping으로 Handler를 찾고, HandlerAdapter로 실행해요. 실행 결과로 ViewResolver가 실제 View를 찾죠.


### Spring MVC에서 요청 URL을 처리할 Handler(Controller)를 '찾는' 역할과 찾아낸 Handler를 '실행하는' 역할을 분리하여 담당하는 두 컴포넌트는 각각 무엇일까요?

1. HandlerMapping, HandlerAdapter
2. DispatcherServlet, ViewResolver
3. View, Model
4. ViewResolver, HandlerMapping

해설
1. HandlerMapping, HandlerAdapter
요청 URL에 맞는 Handler를 찾는 것은 HandlerMapping이, 이 Handler의 타입에 상관없이 실행하는 것은 HandlerAdapter의 역할입니다. 이 둘이 함께 동작해요.


### Handler 실행 후 반환된 논리적인 View 이름을 실제 View(예: JSP 파일)로 변환하여 찾아내는 역할을 하는 컴포넌트는 무엇일까요?

1. DispatcherServlet
2. HandlerMapping
3. ViewResolver
4. HandlerAdapter

해설
3. ViewResolver
Controller가 반환한 View 이름(논리적 이름)을 가지고 실제 View 템플릿 객체(예: JSP)를 찾아주는 역할을 ViewResolver가 담당합니다.


### 현대적인 Spring MVC 개발에서 @Controller, @GetMapping, @PostMapping과 같은 애노테이션은 주로 어떤 역할을 가능하게 할까요?

1. 의존성 주입 설정
2. View 렌더링 로직 구현
3. HTTP 요청과 Handler/Method 매핑 및 처리 방식 정의
4. 데이터베이스 직접 접근

해설
3. HTTP 요청과 Handler/Method 매핑 및 처리 방식 정의
이 애노테이션들은 특정 URL 패턴의 HTTP 요청(GET/POST 등)을 어떤 Controller 클래스의 어떤 Method가 처리할지 편리하게 연결(매핑)하고 그 방식을 정의해요.

---

# 섹션 7. 스프링 MVC - 기본 기능


## 프로젝트 생성
생략

## 로깅 간단히 알아보기
앞으로 로그를 사용할 것이기 때문에, 이번 시간에는 로그에 대해서 간단히 알아보자.

운영 시스템에서는 `System.out.println()`과 같은 시스템 콘솔을 사용해서 필요한 정보를 출력하지 않고 별도의 로깅 라이브러리를 사용해서 로그를 출력한다.
참고로 로그 관련 라이브러리도 많고, 깊게 들어가면 끝이 없기 때문에 여기서는 최소한의 사용 방법만 알아본다.

**로깅 라이브러리**
스프링 부트 라이브러리를 사용하면 스프링 부트 로깅 라이브러리(`spring-boot-starter-logging)`가 함께 포함된다.
스프링 부트 로깅 라이브러리는 기본으로 다음 로깅 라이브러리를 사용한다.

- SLF4J - http://www.slf4j.org // 인터페이스
- Logback - http://logback.qos.ch // 구현체

로그 라이브러리는 Logback, Log4J, Log4J2 등등 수많은 라이브러리가 있는데 그것을 통합해서 인터페이스로 제공하는 것이 바로 SLF4J 라이브러리이다.

쉽게 이야기해서 SLF4J는 인터페이스이고 그 구현체로 Logback 같은 로그 라이브러리를 선택하면 된다.
실무에서는 스프링 부트가 기본으로 제공하는 Logback을 대부분 사용한다.

**로그 선언**
- `private Logger log = LoggerFactory.getLogger(getClass());`
- `private static final Logger log = LoggerFactory.getLogger(Xxx.class)`
- `@Slf4j` : 롬복 사용 가능

**로그 호출**
- `log.info("hello")`
- `System.out.println("hello")`
시스템 콘솔로 직접 출력하는 것 보다 로그를 사용하면 다음과 같은 장점이 있다.
실무에서는 항상 로그를 사용해야 한다!


>참고
>REST Controller
>기본적으로 스프링은 `@Controller` 와 같은 컨트롤러들은 문자를 반환하고 그걸 `뷰 이름`으로 간주하게 된다.
>하지만 `REST Controller`는 문자를 반환하면 해당 String을 그냥 바로 그대로 반환하게 된다.


```java
package hello.springmvc.basic;  
  
import org.slf4j.Logger;  
import org.slf4j.LoggerFactory;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
@RestController  
public class LogTestController {  
    private final Logger log = LoggerFactory.getLogger(this.getClass()); // slf4j를 사용해야함  
  
    @RequestMapping("/log-test")  
    public String logTest() {  
        String name = "Spring";  
  
        System.out.println("name = " + name); // 로그 안썼을 때  
        log.info("info log = {} ", name); // 로그 썼을 때  
  
        return "ok";  
    }  
}
```

![[Pasted image 20250623233306.png]]
- 같은 내용을 출력하지만, `log.info()`로 출력했을 때 더 많은 정보를 얻을 수 있음

```java
package hello.springmvc.basic;  
  
import org.slf4j.Logger;  
import org.slf4j.LoggerFactory;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
@RestController  
public class LogTestController {  
    private final Logger log = LoggerFactory.getLogger(this.getClass()); // slf4j를 사용해야함  
  
    @RequestMapping("/log-test")  
    public String logTest() {  
        String name = "Spring";  
  
        System.out.println("name = " + name); // 로그 안썼을 때  
  
        // 로그 썼을 때 (로그에도 레벨이 있음. 각 단계별로 어디서 쓰이는 로그인지 명확히 구별됨.)  
        log.trace("trace log {}", name);  
        log.debug("debug log {}", name);  
        log.info("info log {}", name);  
        log.warn("warn log = {} ", name);  
        log.error("error log = {} ", name);  
  
        return "ok";  
    }  
}
```

```Console
name = Spring
2025-06-23T23:36:06.476+09:00  INFO 16252 --- [springmvc] [nio-8080-exec-2] h.springmvc.basic.LogTestController      : info log Spring
2025-06-23T23:36:06.477+09:00  WARN 16252 --- [springmvc] [nio-8080-exec-2] h.springmvc.basic.LogTestController      : warn log = Spring 
2025-06-23T23:36:06.477+09:00 ERROR 16252 --- [springmvc] [nio-8080-exec-2] h.springmvc.basic.LogTestController      : error log = Spring 
```
- `trace`와 `debug`는 로그가 안찍혔네?

`application.properties`
```properties
spring.application.name=springmvc  
#hello.springmvc 패키지와 그 하위 로그 레벨 설정  
logging.level.hello.springmvc=trace
```
- 이렇게 설정해주면

```Console
name = Spring
2025-06-23T23:38:21.198+09:00 TRACE 39608 --- [springmvc] [nio-8080-exec-1] h.springmvc.basic.LogTestController      : trace log Spring
2025-06-23T23:38:21.198+09:00 DEBUG 39608 --- [springmvc] [nio-8080-exec-1] h.springmvc.basic.LogTestController      : debug log Spring
2025-06-23T23:38:21.198+09:00  INFO 39608 --- [springmvc] [nio-8080-exec-1] h.springmvc.basic.LogTestController      : info log Spring
2025-06-23T23:38:21.198+09:00  WARN 39608 --- [springmvc] [nio-8080-exec-1] h.springmvc.basic.LogTestController      : warn log = Spring 
2025-06-23T23:38:21.198+09:00 ERROR 39608 --- [springmvc] [nio-8080-exec-1] h.springmvc.basic.LogTestController      : error log = Spring 
```
- 만약 `trace`가 아니고 `debug`면 `debug` 하위 레벨들만 출력됨 (trace가 제외되는 거임.)

그렇다면
`개발 서버`는 `debug`로, 나의 `로컬 PC` 에서는 `trace`로, `운영 서버`에서는 `info` 레벨로 세팅한다면?
```properties
spring.application.name=springmvc  

#전체 로그 레벨 설정 (기본 info)
logging.level.root=info  
  
#hello.springmvc 패키지와 그 하위 로그 레벨 설정  
logging.level.hello.springmvc=info
```

>참고
1. **TRACE** (가장 상세, 가장 낮은 레벨)
2. **DEBUG**
3. **INFO** (미설정시 기본 값)
4. **WARN**
5. **ERROR** (가장 심각, 가장 높은 레벨)
- 개발 서버는 debug 레벨로
- 운영 서버는 info 레벨로

반면, `System.out.println()`으로 출력하게 되는 경우 모든 경우에 출력이 되기 때문에 로그 폭탄을 맞을 수 있음..



**매핑 정보**
- `@RestController`
	- `@Controller` 는 반환 값이 `String` 이면 뷰 이름으로 인식한다.
		- 그래서 **뷰를 찾고 뷰가 랜더링**되게 됨.
	- `@RestController`는 반환 값으로 뷰를 찾는 것이 아니라, **HTTP 메시지 바디에 바로 입력**한다.
		- 따라서 실행 결과로 ok 메시지를 받을 수 있다.
	- 이는 `@ResopnseBody`와 관련이 있는데, 후술할 예정.


```java
package hello.springmvc.basic;  
  
import lombok.extern.slf4j.Slf4j;  
import org.slf4j.Logger;  
import org.slf4j.LoggerFactory;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
@Slf4j  
@RestController  
public class LogTestController {  
    // private final Logger log = LoggerFactory.getLogger(this.getClass()); // slf4j를 사용해야함  
  
    @RequestMapping("/log-test")  
    public String logTest() {  
        String name = "Spring";  
  
        System.out.println("name = " + name); // 로그 안썼을 때  
  
        // 로그 썼을 때 (로그에도 레벨이 있음. 각 단계별로 어디서 쓰이는 로그인지 명확히 구별됨.)  
        log.trace("trace log {}", name);  // 매우 상세한 내부 동작 로그
        log.debug("debug log {}", name);  // 디버깅 시 필요한 정보
        log.info("info log {}", name);  // 일반적인 정보
        log.warn("warn log = {} ", name);  // 경고 상황
        log.error("error log = {} ", name);  // 에러 발생 시
  
        return "ok";  
    }  
}
```
- 롬복의 `@Slf4j`

**올바른 로그 사용법**
- `log.debug("data="+data)`
	- 로그 출력 레벨을 info로 설정해도 해당 코드에 있는 "data="+data가 실제 실행이 되어버린다. 결과적으로 문자 더하기 연산이 발생한다.
- `log.debug("data={}, data`
	- 로그 출력 레벨을 info로 설정하면 아무 일도 발생하지 않는다. 따라서 앞과 같은 의미없는 연산이 발생하지 않는다.

**로그 사용시 장점**
- 쓰레드 정보, 클래스 이름 같은 부가 정보를 함께 볼 수 있고, 출력 모양을 조정할 수 있다.
- 로그 레벨에 따라 개발 서버에서는 모든 로그를 출력하고, 운영 서버에서는 출력하지 않는 등 로그를 상황에 맞게 조절할 수 있다.
- 시스템 아웃 콘솔에만 출력하는 것이 아니라, 파일이나 네트워크 등 로그를 별도의 위치에 남길 수 있다. 특히 파일로 남길 때는 일별, 특정 용량에 따라 로그를 분할하는 것도 가능하다.
- 성능도 일반 System.out 보다 좋다. (내부 버퍼링, 멀티 쓰레드 등등...) 그래서 실무에서는 꼭 로그를 사용해야 한다.

>참고
- SLF4J - `http://www.slf4j.org`
- Logback - `http://logback.qos.ch`
- 스프링 부트 제공 로그 기능
	- `https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-logging`

## 요청 매핑
```java
package hello.springmvc.basic.requestmapping;  
  
import org.slf4j.Logger;  
import org.slf4j.LoggerFactory;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
@RestController  
public class MappingController {  
  
    private Logger log = LoggerFactory.getLogger(this.getClass());  
  
    /*  
    기본 요청  
    둘 다 허용 /hello-basic, /hello-basic/    HTTP 메서드 모두 허용 GET, HEAD, POST, PUT, PATCH, DELETE     */    @RequestMapping("/hello-basic")  
    public String helloBasic() {  
        log.info("hello-basic");  
        return "ok";  
    }  
}
```

**매핑 정보(한번 더)**
- `@RestController`
	- `@Controller`는 반환 값이 `String`이면 뷰 이름으로 인식된다. 그래서 뷰를 찾고 뷰가 랜더링 된다.
	- `@RestController`는 반환 값으로 뷰를 찾는 것이 아니라, HTTP 메시지 바디에 바로 입력한다. 따라서 실행 결과로 ok 메시지를 받을 수 있다. `@ResponseBody`와 관련이 있는데, 뒤에서 더 자세히 설명한다.
- `@RequestMapping("/hello-basic")`
	- `/hello-basic` URL 호출이 오면 이 메서드가 실행되도록 매핑한다.
	- 대부분의 속성을 `배열[]`로 제공하므로 다중 설정이 가능하다.
		- `{"/hello-basic", "/hello-go"}`

**Postman으로 테스트 해보자.**

**둘다 허용**
다음 두가지 요청은 다른 URL 이지만, 스프링은 다음 URL 요청들을 같은 요청으로 매핑한다.
- 매핑: `/hello-basic`
- URL 요청: `/hello-basic`, `/hello-basic/`

**HTTP 메서드**
`@RequestMapping`에 `method` 속성으로 HTTP 메서드를 지정하지 않으면 HTTP 메서드와 무관하게 호출된다.
모두 허용 GET, HEAD, POST, PUT, PATCH, DELETE

```java
package hello.springmvc.basic.requestmapping;  
  
import org.slf4j.Logger;  
import org.slf4j.LoggerFactory;  
import org.springframework.web.bind.annotation.GetMapping;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RequestMethod;  
import org.springframework.web.bind.annotation.RestController;  
  
@RestController  
public class MappingController {  
  
    private Logger log = LoggerFactory.getLogger(this.getClass());  
  
    /*  
    기본 요청  
    둘 다 허용 /hello-basic, /hello-basic/    HTTP 메서드 모두 허용 GET, HEAD, POST, PUT, PATCH, DELETE     */    @RequestMapping(value = "/hello-basic")  
    public String helloBasic() {  
        log.info("hello-basic");  
        return "ok";  
    }  
  
    /*  
    method 특정 HTTP 메서드 요청만 허용  
    GET, HEAD, POST, PUT, PATCH, DELETE    */    @RequestMapping(value = "/hello-basic-v1", method = RequestMethod.GET)  
    public String helloBasicV1() {  
        log.info("hello-basic");  
        return "ok";  
    }  
  
    /*  
    편리한 축약 애노테이션  
    @GetMapping    @PostMapping    @PutMapping    @DeleteMapping    @PatchMapping    */    @GetMapping(value = "/hello-basic-v2")  
    public String helloBasicV2() {  
        log.info("hello-basic");  
        return "ok";  
    }  
}
```


**경로 변수 사용**
```java
/*  
PathVariable(경로 변수) 사용  
변수명이 같으면 생략 가능  
@PathVariable("userId") String userId -> @PathVariable userId  
/mapping/userA  
 */@GetMapping("/mapping/{userId}")  
public String mappingPath(@PathVariable("userId") String data) {  
    log.info("mappingPath userId={}", data);  
    return "ok";  
}
```

최근 HTTP API는 다음과 같이 리소스 경로에 식별자를 넣는 스타일을 선호한다.
- `/mapping/userA`
- `/users/1`
- `@RequestMapping`은 URL 경로를 템플릿화 할 수 있는데, `@PathVariable`을 사용하면 매칭되는 부분을 편리하게 조회할 수 있다.
- `@PathVariable`의 이름과 파라미터 이름이 같으면 생략할 수 있다.
```java
@GetMapping("/mapping/{userId}")  
public String mappingPath(@PathVariable String userId) {  
    log.info("mappingPath userId={}", userId);  
    return "ok";  
}
```
- `?username=userA`와 같은 쿼리 파라미터 방식과는 다름

## 요청 매핑 - API 예시

```java
package hello.springmvc.basic.requestmapping;  
  
import org.springframework.web.bind.annotation.DeleteMapping;  
import org.springframework.web.bind.annotation.GetMapping;  
import org.springframework.web.bind.annotation.PatchMapping;  
import org.springframework.web.bind.annotation.PathVariable;  
import org.springframework.web.bind.annotation.PostMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
@RestController  
public class MappingClassController {  
  
    /**  
     * 회원 목록 조회 : GET      '/users  
     * 회원 등록     : POST     '/users  
     * 회원 조회     : GET      '/users/{userId}'  
     * 회원 수정     : PATCH    '/users/{userId}'  
     * 회원 삭제     : DELETE   '/users/{userId}'  
     */  
    @GetMapping("mapping/users")  
    public String user() {  
        return "get users";  
    }  
  
    @PostMapping("/mapping/users")  
    public String addUser() {  
        return "post user";  
    }  
  
    @GetMapping("/mapping/users/{userId}")  
    public String findUser(@PathVariable String userId) {  
        return "get userId=" + userId;  
    }  
  
    @PatchMapping("/mapping/users/{userId}")  
    public String updateUser(@PathVariable String userId) {  
        return "update userId=" + userId;  
    }  
  
    @DeleteMapping("/mapping/users/{userId}")  
    public String deleteUser(@PathVariable String userId) {  
        return "delete userId=" + userId;  
    }  
}
```

## HTTP 요청 - 기본, 헤더 조회
애노테이션 기반의 스프링 컨트롤러는 다양한 파라미터를 지원한다.
이번 시간에는 HTTP 헤더 정보를 조회하는 방법을 알아보자.

`RequestHeaderController`
```java
package hello.springmvc.basic.request;  
  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.util.Locale;  
import lombok.extern.slf4j.Slf4j;  
import org.springframework.http.HttpMethod;  
import org.springframework.util.MultiValueMap;  
import org.springframework.web.bind.annotation.CookieValue;  
import org.springframework.web.bind.annotation.RequestHeader;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
@Slf4j  
@RestController  
public class RequestHeaderController {  
  
    @RequestMapping("/headers")  
    public String headers(HttpServletRequest request,  
                          HttpServletResponse response,  
                          HttpMethod httpMethod,  
                          Locale locale,  
                          @RequestHeader MultiValueMap<String, String> headerMap,  
                          @RequestHeader("host") String host,  
                          @CookieValue(value = "myCookie", required = false) String myCookie) {  
  
        log.info("request={}", request);  
        log.info("response={}", response);  
        log.info("httpMethod={}", httpMethod);  
        log.info("locale={}", locale);  
        log.info("headerMap={}", headerMap);  
        log.info("header host={}", host);  
        log.info("myCookie={}", myCookie);  
  
        return "ok";  
    }  
}
```
- `HttpMethod`: HTTP 메서드 타입
- `Locale`: 언어
- `@RequestHeader MultiValueMap<...>`: 헤더 정보 전부
- `@RequestHeader("host")`: host 헤더 정보만
- `@CookieValue(value = "...")`: 쿠키 정보

**결과**
![[Pasted image 20250719230625.png]]
>참고
>`MultiValueMap
- Map과 유사한데, 하나의 키에 여러 값을 받을 수 있다.
- HTTP header, HTTP 쿼리 파라미터와 같이 하나의 키에 여러 값을 받을 때 사용한다.
	- `keyA = value1 & keyA = value2`
```java
MultiValueMap<String, Strinmg> map = new LinkedMultiValueMap();
map.add("keyA", "value1");
map.add("keyA", "value2");

// [value1, value2]
List<String> values = map.get("keyA");
```

> 참고
> `Slf4j`
다음 코드를 자동으로 생성해서 로그를 선언해줌. 개발자는 편리하게 `log`라고 사용하면 됨.
```java
private static final org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(RequestHeaderController.class);
```

## HTTP 요청 파라미터 - 쿼리 파라미터, HTML Form
서블릿에서 학습했던 HTTP 요청 데이터를 조회하는 방법을 다시 떠올려보자.
그리고 서블릿으로 학습했던 내용을 스프링이 얼마나 깔끔하고 효율적으로 바꾸어주는지 알아보자.

**HTTP 요청 메시지를 통해 클라이언트 -> 서버로 데이터를 전달하는 방법을 알아보자.**

**클라이언트에서 서버로 요청 데이터를 전달할 때는 주로 다음 3가지 방법을 사용한다.**

- **GET - 쿼리 파라미터**
	- `/url?username=hello&age=20`
	- 메시지 바디 없이, URL의 쿼리 파라미터에 데이터를 포함해서 전달
		- 예) 검색, 필터, 페이징 등에서 많이 사용되는 방식
- **POST - HTML Form**
	- `content-type: application/x-www-form-urlencoded`
	- 메시지 바디에 쿼리 파라미터 형식으로 전달 `username=hello&age=20`
		- 예) 회원가입, 상품 주문, HTML Form 사용
- **HTTP message body**에 데이터를 직접 담아서 요청
	- HTTP API에서 주로 사용 (JSO, XML, TEXT)
	- 데이터 형식은 주로 JSON
	- POST, PUT, PATCH

하나씩 알아보자.

### 요청 파라미터 - 쿼리 파라미터, HTML Form
`HttpServletRequest`의 `request.getParameter()`를 사용하면 다음 두가지 요청 파라미터를 조회할 수 있다.

**GET, 쿼리 파라미터 전송**
예시
`http://localhost:8080/request-param?username=hello&age=20`

**POST, HTML Form 전송**
예시
```java
POST /request-param ...
content-type: application/x-www-form-urlencoded

username=hello&age=20
```

GET 쿼리 파라미터 전송 방식이든, POST HTML Form 전송 방식이든 둘 다 형식이 같으므로 구분없이 조회할 수 있다.
이것을 간단히 **요청 파라미터(request parameter) 조회**라 한다.

지금부터 스프링으로 요청 파라미터를 조회하는 방법을 단계적으로 알아보자.

**RequestParamController**
```java
package hello.springmvc.basic.request;  
  
import jakarta.servlet.http.HttpServletRequest;  
import jakarta.servlet.http.HttpServletResponse;  
import java.io.IOException;  
import lombok.extern.slf4j.Slf4j;  
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.RequestMapping;  
  
@Slf4j  
@Controller  
public class RequestParamController {  
  
    // HttpServletRequest가 제공하는 getParameter 사용  
    @RequestMapping("/request-param-v1")  
    public void requestParamV1(HttpServletRequest request, HttpServletResponse response) throws IOException {  
        String username = request.getParameter("username");  
        int age = Integer.parseInt(request.getParameter("age"));  
        log.info("username={}, age={}", username, age);  
  
        response.getWriter().write("ok");  
    }  
}
```

## HTTP 요청 파라미터 - @RequestParam
스프링이 제공하는 `@RequestParam` 을 사용하면 요청 파라미터를 매우 편리하게 사용할 수 있다.

`requestParamV2`
```java
@ResponseBody // REST Controller 쓸거 아니면 응답 메시지 Body에 담아서 보내기  
@RequestMapping("/request-param-v2")  
public String requestParamV2(  
        @RequestParam("username") String memberName,  
        @RequestParam("age") int memberAge) {  
  
    log.info("username={}, age={}", memberName, memberAge);  
    return "ok";  
}
```
- `@RequestParam`: 파라미터 이름으로 바인딩
- `@ResponseBody`: View 조회를 무시하고, HTTP message body에 직접 해당 내용 입력

**@ReuquestParam**의 `name(value)` 속성이 파라미터 이름으로 사용
- @RequestParam("**username**") String **memberName**
- -> request.getParameter("**username**") 와 동일

```java
@ResponseBody  
@RequestMapping("/request-param-v3") // HTTP Request 속 넘어오는 변수명과 파라미터 변수명이 동일하면 생략 가능  
public String requestParamV3(  
        @RequestParam String username,  
        @RequestParam int age) {  
  
    log.info("username={}, age={}", username, age);  
    return "ok";  
}  
  
@ResponseBody  
@RequestMapping("/request-param-v4") // 근데 사실 V3을 만족한다면 V4로 변환도 가능  
public String requestParamV4(String username, int age) {  
    log.info("username={}, age={}", username, age);  
    return "ok";  
}
```
- HTTP 파라미터 이름이 변수 이름과 같으면 `@RequestParam(name="xx")` 생략 가능.
	- 스프링 MVC 파라미터 바인딩
- V4처럼, `String`, `int`, `Integer` 등의 단순 타입이면 `@RequestParam`도 생략 가능
	- 근데 이건 너무 과하지 않나..
	- `@RequestParam`을 명시하면서 목적을 가시적으로 보여줄 수 있는게 더 좋다고 생각.

```java
@ResponseBody  
@RequestMapping("/request-param-required") // 근데 사실 V3을 만족한다면 V4로 변환도 가능  
public String requestParamRequired(  
        @RequestParam(required = true) String username,  
        @RequestParam(required = true) int age) {  
    log.info("username={}, age={}", username, age);  
    return "ok";  
}
```
- `required` 옵션을 통해서 필수적으로 HTTP 파라미터 이름이 넘어와야 함.
	- 만약, age 가 `required = false` 인 상태로, username="aa" 만 HTTP 요청을 보냈다면?
		- **500 Error** 발생
		- HTTP 스펙대로 보냈지만, age처럼 받지 못한 값들은 null을 넣어준다.
		- 근데 int에는 null을 대입할 수 없어서 500 에러 발생..
			- 이를 해결하기 위해선 `int age`를 `Integer age`로 수정해주면 됨
			- 또는 `defaultValue`를 사용하면 됨
- `required`의 기본 값은 `true`
	- `username`이 `true`인데 요청에 포함 안시켰다면 **400 에러** 발생
		- `null` 과 `""` 는 언뜻 보면 동일해 보이지만 그렇지 않고 명백히 다름.

**DefaultValue**
```java
@ResponseBody  
@RequestMapping("/request-param-default") // 근데 사실 V3을 만족한다면 V4로 변환도 가능  
public String requestParamDefault(  
        @RequestParam(required = true, defaultValue = "guest") String username,  
        @RequestParam(required = false, defaultValue = "-1") int age) {  
    log.info("username={}, age={}", username, age);  
    return "ok";  
}
```

**파라미터를 Map으로 조회하기 - requestParamMap**
```java
@ResponseBody  
@RequestMapping("/request-param-map") // 근데 사실 V3을 만족한다면 V4로 변환도 가능  
public String requestParamMap(@RequestParam Map<String, Object> paramMap) {  
    log.info("username={}, age={}", paramMap.get("username"), paramMap.get("age"));  
    return "ok";  
}
```
- MultiValueMap 으로도 조회 가능
	- `@RequestParam Map`
		- `Map(key=value)`
	- `@RequestParam MultiValueMap`
		- `MultiValueMap(key=[value1, value2, ...] ex) (key=userIds, value=[id1, id2])`

## HTTP 요청 파라미터 - @ModelAttribute
실제 개발을 하면 요청 파라미터를 받앙서 필요한 객체를 만들고 그 객체에 값을 넣어주어야 한다. 보통 다음과 같이 코드를 작성할 것이다.
```java
@RequestParam String username;
@RequestParam int age;

HelloData data = new HelloData();
data.setUsername(username);
data.setAge(age);
```

스프링은 이 과정을 완전히 자동화해주는 `@ModelAttribute`기능을 제공한다.

먼저 요청 파라미터를 바인딩 받을 객체를 만들자.

`helloData`
```java
package hello.springmvc.basic;  
  
import lombok.Data;  
  
@Data  
public class HelloData {  
    private String username;  
    private Integer age;  
}
```
- 롬복 `@Data`
	- `@Getter`, `@Setter`, `@ToString`, `@EqualsAndHashCode`, `@RequiredArgsConstructor`를 자동으로 적용해준다.

`@ModelAttribute 적용 - modelAttributeV1`
```java
@ResponseBody  
@RequestMapping("/model-attribute-v1")  
public String modelAttributeV1(@ModelAttribute HelloData helloData) {  
    log.info("username={}, age={}", helloData.getUsername(), helloData.getAge());  
    log.info("hellodata={}", helloData);  
  
    return "ok";  
}
```
- 마치 마법처럼 HelloData 객체가 생성되고, 요청 파라미터의 값도 모두 들어가 있다.

스프링 MVC는 `@ModelAttribute`가 있으면 다음을 실행한다.
- `HelloData` 객체를 생성한다.
- 요청 파라미터의 이름으로 `HelloData`객체의 프로퍼티를 찾는다. 그리고 해당 프로퍼티의 setter를 호출해서 파라미터의 값을 입력(바인딩) 한다.
- 예) 파라미터의 이름이 `username`이면, `setUsername()` 메서드를 찾아서 호출하면서 값을 입력한다.

> `@RequestParam`은 수동 바인딩이고 `@ModelAttribute`는 자동 바인딩이다.

**프로퍼티**
객체에 `getUsername()`, `setUsername()` 메서드가 있으면 이 객체는 `username`이라는 프로퍼티를 가지고 있다.
`username`프로퍼티의 값을 변경하면 `setUsername()`이 호출되고, 조회하게 되면 `getUsername()`이 자동으로 호출된다.
```java
class HelloData {
	getUsername();
	setUsername();
}
```

**바인딩 오류**
`age = abc` 처럼 숫자가 들어가야 할 곳에 문자를 넣으면 `BindException`이 발생한다. 이런 바인딩 오류를 처리하는 방법은 검증 부분에서 다룬다.

`@ModelAttribute 생략 - modelAttributeV2`
```java
@ResponseBody  
@RequestMapping("/model-attribute-v2")  
public String modelAttributeV2(HelloData helloData) {  
    log.info("username={}, age={}", helloData.getUsername(), helloData.getAge());  
    log.info("hellodata={}", helloData);  
  
    return "ok";  
}
```
- `@ModelAttribute`는 생략할 수 있다.
- 그런데 `@RequestParam`도 생략할 수 있으니 혼란이 발생할 수 있다.

스프링은 해당 생략시 다음과 같은 규칙을 적용한다.
- `String`, `int`, `Integer` 같은 단순 타입 = `@RequestParam`
- 나머지 = `@ModelAttribute` (argument resolver로 지정해둔 타입 외)


## HTTP 요청 메시지 - 단순 텍스트
서블릿에서 학습한 내용을 떠올려보자.

- **HTTP message body**에 데이터를 직접 담아서 요청
	- HTTP API에서 주로 사용. JSON, XML, TEXT
	- 데이터 형식은 주로 JSON 사용
	- POST, PUT, PATCH

요청 파라미터와 다르게, HTTP 메시지 바디를 통해서 데이터가 직접 넘어오는 경우는 `@RequestParam`, `@ModelAttribute`를 사용할 수 없다.
- 물론 HTML Form 형식으로 전달되는 경우는 요청 파라미터로 인정된다.

먼저 가장 단순한 텍스트 메시지를 HTTP 메시지 바디에 담아서 전송하고 읽어보자.
HTTP 메시지 바디의 데이터는 `InputStream`을 사용해서 직접 읽을 수 있다.

**RequestBodyStringController**
```java
@Slf4j  
@Controller  
public class RequestBodyStringController {  
  
    @PostMapping("/request-body-string-v1")  
    public void requestBodyString(HttpServletRequest request, HttpServletResponse response) throws IOException {  
        ServletInputStream inputStream = request.getInputStream();  
        String messageBody = StreamUtils.copyToString(inputStream, StandardCharsets.UTF_8);  
  
        log.info("messageBody = {}", messageBody);  
  
        response.getWriter().write("ok");  
    }  
  
    @PostMapping("/request-body-string-v2")  
    public void requestBodyStringV2(InputStream inputStream, Writer responseWriter) throws IOException {  
        String messageBody = StreamUtils.copyToString(inputStream, StandardCharsets.UTF_8);  
        log.info("messageBody = {}", messageBody);  
        responseWriter.write("ok");  
    }  
}
```
- 스프링 MVC는 `InputStream`, `OutputStream`, `Writer`들을 모두 파라미터로 제공한다.

```java
@PostMapping("/request-body-string-v3")  
public HttpEntity<String> requestBodyStringV3(HttpEntity<String> httpEntity) throws IOException {  
  
    String messageBody = httpEntity.getBody();  
    log.info("messageBody = {}", messageBody);  
  
    return new HttpEntity<>("ok");  
}
```
**스프링 MVC**는 다음 파라미터를 지원한다.
- `HttpEntity`: HTTP header, body 정보를 편리하게 조회
	- 메시지 바디 정보를 직접 조회
	- 요청 파라미터를 조회하는 기능과는 관계 없음 `@RequestParam` -> X, `2ModelAttribute` -> X
- `HttpEntity`는 응답에도 사용 가능
	- 메시지 바디 정보를 직접 반환
	- 헤더 정보 포함 가능
	- view 조회 X

`HttpEntity`를 상속받은 다음 객체들도 같은 기능을 제공한다.
- `RequestEntity`
	- HttpMethod, url 정보가 추가와 요청에 사용 됨
- `ResponseEntity`
	- Http 상태 코드 설정 가능, 응답에서 아용
	- `return new ResponseEntity<String>("Hello World", responseHeaders, HttpStatus.CREATED)` 

>**참고**
>스프링 MVC 내부에서 HTTP 메시지 바디를 읽어서 문자나 객체로 변환해서 전달해주는데, 이때 HTTP 메시지 컨버터(`HttpMessageConverter`)라는 기능을 사용한다.


```java
@ResponseBody  
@PostMapping("/request-body-string-v4")  
public String requestBodyStringV4(@RequestBody String messageBody) {  
    log.info("messageBody = {}", messageBody);  
    return "ok";  
}
```
- 최종본

`@RequestBody`를 사용하면 HTTP 메시지 바디 정보를 편리하게 조회할 수 있다. 참고로 헤더 정보가 필요하다면 `HttpEntity`를 사용하거나 `@RequestHeader`를 사용하면 된다.
이렇게 메시지 바디를 직접 조회하는 기능은 요청 파라미터를 조회하는 `@RequestParam`, `@ModelAttribute`와는 전화 관계 없음

**요청 파라미터 vs HTTP 메시지 바디**
- 요청 파라미터를 조회하는 기능: `@RequestParam`, `@ModelAttribute`
- HTTP 메시지 바디를 직접 조회하는 기능: `@RequestBody`

**@ResponseBody**
- `@ResponseBody`를 사용하면 응답 결과를 HTTP 메시지 바디에 직접 담아서 전달할 수 있다.
- 물론 이 경우에도 view를 사용하지 않음.



## HTTP 요청 메시지 - JSON



## 응답 - 정적 리소스, 뷰 템플릿



## HTTP 응답 - HTTP API, 메시지 바디에 직접 입력



## HTTP 메시지 컨버터



## 요청 매핑 헨들러 어뎁터 구조



## 정리



---
