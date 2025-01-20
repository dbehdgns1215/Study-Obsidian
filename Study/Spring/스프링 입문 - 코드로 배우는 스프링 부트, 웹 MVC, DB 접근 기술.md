
# **섹션 2 - 프로젝트 환경설정

## **프로젝트 생성


## **라이브러리 살펴보기
> Gradle은 의존 관계가 있는 라이브러리를 함께 다운로드 한다

**스프링 부트 라이브러리
- spring-boot-starter-web
	- spring-boot-starter-tomcat: 톰캣(웹서버)
	- spring-webmvc: 스프링 웹 MVC
- spring-boot-starter-thymeleaf: 타임리프 템플릿 엔진(View)
- spring-boot-starter(공통): 스프링 부트 + 스프링 코어 + 로깅
	- spring-boot
		- spring-core
	- spring-boot-starter-loggin
		- logback, slf4j

**테스트 라이브러리
- spring-boot-starter-test
	- junit: 테스트 프레임워크
	- mockito: 목 라이브러리
	- assertj: 테스트 코드를 좀 더 편하게 작성하게 도와주는 라이브러리
	- spring-test: 스프링 통합 테스트 지원

## **View 환경설정
웰컴 페이지
- 스프링 부트에 내장된 기능으로, statics 폴더 하위에 `index.html` 파일을 넣어주면 자동으로 웰컴페이지로 사용할 수 있게끔 해줌

![[Pasted image 20250120143344.png]]
웹 브라우저 -> 내장 톰캣 서버 -> 스프링 컨테이너 (컨트롤러) -> 스프링 컨테이너(뷰 리졸버) -> 웹 브라우저



## **빌드하고 실행하기
IDE에서 실행하는 것이 아닌 직접 빌드 후 실행

> 윈도우 기준
1. `cd C:\study\hello-spring\hello-spring`

`C:\study\hello-spring\hello-spring>`

`2025-01-20  오전 11:48             2,966 gradlew.bat`



> 빌드 명령어

2. `C:\study\hello-spring\hello-spring>gradlew.bat build`

```
`Welcome to Gradle 8.11.1!`

Here are the highlights of this release:
 - Parallel load and store for Configuration Cache
 - Java compilation errors at the end of the build output
 - Consolidated report for warnings and deprecations

For more details see https://docs.gradle.org/8.11.1/release-notes.html

Starting a Gradle Daemon, 1 incompatible Daemon could not be reused, use --status for details
Java HotSpot(TM) 64-Bit Server VM warning: Sharing is only supported for boot loader classes because bootstrap classpath has been appended

BUILD SUCCESSFUL in 23s
7 actionable tasks: 6 executed, 1 up-to-date
C:\study\hello-spring\hello-spring>
```


3. `cd build/libs`

```
C:\study\hello-spring\hello-spring\build\libs 디렉터리

2025-01-20  오후 02:43    <DIR>          .
2025-01-20  오후 02:43    <DIR>          ..
2025-01-20  오후 02:43             2,435 hello-spring-0.0.1-SNAPSHOT-plain.jar
2025-01-20  오후 02:43        22,220,720 hello-spring-0.0.1-SNAPSHOT.jar
               2개 파일          22,223,155 바이트
               2개 디렉터리  18,477,236,224 바이트 남음
```

4. C:\study\hello-spring\hello-spring\build\libs>java -jar hello-spring-0.0.1-SNAPSHOT.jar
```
C:\study\hello-spring\hello-spring\build\libs>java -jar hello-spring-0.0.1-SNAPSHOT.jar
```

```
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/

 :: Spring Boot ::                (v3.4.1)

...
```


---

# **섹션 3 - 스프링 웹 개발 기초

## **정적 컨텐츠
- 스프링 부트 정적 컨텐츠 기능
- 파일을 그대로 웹 브라우저에 전달해주는 방식

![[Pasted image 20250120155453.png]]
- 기본적으로 스프링 컨테이너는 컨트롤러에서 해당 요청이 정의되어 있는지를 확인함
- 만약 정의되어 있지 않다면, static 디렉토리 하위에서 요청과 매칭되는 이름을 가진 html 파일을 찾아서 반환해줌



## **MVC와 템플릿 엔진
- 템플릿 엔진이 렌더링을해서 변환된 html을 웹 브라우저로 전달해주는 방식

![[Pasted image 20250120155515.png]]
- @Controller - 컨트롤러 어노테이션
- @GetMapping - GET 메서드 어노테이션
- @RequestParam - HTTP 요청의 파라미터를 컨트롤러 메서드의 파라미터로 바인딩해주는 어노테이션


## **API
- ㄴ


![[Pasted image 20250120160313.png]]
- @ResponseBody - HTML 응답 메시지의 body 부분에 **직접** 데이터를 반환하겠다는 어노테이션
- MVC나 템플릿 엔진과는 다르게 문자 그대로가 반환된다
	- @ResponseBody
	- public String helloString(@RequestParan("name") String name)
		- return "hello " + name;
- 실제로 실행시켜보면 매개변수로 입력한 문자 그 자체만 출력되는 것을 알 수 있음
	- html 태그같은 것도 없고 그냥 단순히 매개변수로 입력한 문자 그대로..
- ![[Pasted image 20250120161010.png]]
- ![[Pasted image 20250120161029.png]]

- 해당 기능은 페이지를 띄우거나 문자를 띄우거나 하는 것에는 비효율적이지만, 데이터를 넘겨줄 때는 효율적이기 때문에 API 방식이 주로 사용된다

![[Pasted image 20250120161801.png]]
- Getter, Setter가 있는 클래스의 인스턴스를 반환해주게 되면 무슨 일이 생길까?

![[Pasted image 20250120161845.png]]

- JSON 방식으로 데이터를 내려주는 것을 확인할 수 있다



> **짤막 상식

Java Bean 규약 - 프로퍼티 접근 방식, Getter & Setter, JavaBean 표준 방식

필드는 private 지시자를 통해서 접근할 수 없게 만들고, public 지시자를 사용하는 Getter와 Setter 메서드를 추가로 정의해서 외부에서도 접근할 수 있게끔 만듦


---

# 섹션 4 - 회원 관리 예제 - 백엔드 개발

## **비즈니스 요구사항 정리


## **회원 도메인과 리포지토리 만들기


## **회원 리포지토리 테스트 케이스 작성


## **회원 서비스 개발


## **회원 서비스 테스트


---
