

1. 섹션 바로가기
2. [[#섹션 2 - 프로젝트 환경설정]]
3. [[#섹션 3 - 스프링 웹 개발 기초]]
4. [[#섹션 4 - 회원 관리 예제 - 백엔드 개발]]
5. [[#섹션 5 - 스프링 빈과 의존관계 설정]]


---

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

또한, 스프링의 기본 정책 중 하나.
@ResponseBody 어노테이션이 붙어있고, 반환하는 데이터가 **객체**인 경우에는 JSON 형식으로 HTTP 응답에 넘겨주는 것이 기본 정책이다.

![[Pasted image 20250120162717.png]]

HttpMessageConverter에 의해서 JSON 또는 String으로 변환되어서 HTTP 응답의 Body에 포함되게 되는 것


#### **API 정리
- `@ResponseBody`를 사용
- HTTP의 BODY에 문자 내용을 직접 반환
- `viewResolver` 대신에 `HttpMessageConverter`
- 기본 문자처리: StringHttpMessageConverter
- 기본 객체처리: MappingJackson2HttpMessageConverter
-  스프링에는 byte 처리 등등 기타 여러 HttpMessageConverter가 기본으로 등록되어 있음

> 참고: 클라이언트의 HTTP Accept 헤더와 서버의 컨트롤러 반환 타입 정보, 이 둘을 조합해서 `HttpMessageConverter`가 선택된다.

---

# 섹션 4 - 회원 관리 예제 - 백엔드 개발

## **비즈니스 요구사항 정리
- 데이터: 회원 ID, 이름
- 기능: 회원 등록, 조회
- 아직 데이터 저장소가 선정되지 않았음 (가상의 시나리오)

![[Pasted image 20250121095442.png]]
- 컨트롤러: 웹 MVC의 컨트롤러 역할
- 서비스: 핵심 비즈니스 로직 구현
- 리포지토리: 데이터베이스에 접근, 도메인 객체를 DB에 저장하고 관리
- 도메인: 비즈니스 도메인 객체
	- 예) 회원 주문, 쿠폰 등등 주로 데이터베이스에 저장하고 관리됨

![[Pasted image 20250121100509.png]]
- 아직 데이터 저장소가 선정되지 않아서, 우선 인터페이스로 구현 클래스를 변경할 수 있도록 설계
- 데이터 저장소는 RDB, NoSQL 등등 다양한 저장소를 고민중인 상황으로 가정
- 개발을 진행하기 위해서 초기 개발 단계에서는 구현체로 가벼운 메모리 기반의 데이터 저장소 사용



## **회원 도메인과 리포지토리 만들기


## **회원 리포지토리 테스트 케이스 작성

- 주로 assertj 에 들어있는 Assertions를 import해서 테스트 코드를 작성

>@AfterEach

Junit 5 에서 사용되는 어노테이션으로, 각각의 테스트 코드가 실행된 이후 실행되어야 하는 메서드들을 정의하는데 유용한 기능

> Assertions.assertThat()

AssertJ 라이브러리에서 제공하는 테스트 검증 메서드이며, 예상 결과와 실행 결과를 비교해서 테스트의 성공 여부를 판별함

- .isEqualTo(), .contains(), .isGreaterThan() 등의 검증 메서드들을 제공하기도 함

```java
Assertions.assertThat(member).isEqualTo(result);
```

## **회원 서비스 개발

- 주로 비즈니스 로직을 처리하는 역할을 함

>테스트 코드를 자동으로 빠르게 만드는 방법
>Ctrl + Shift + T

>각종 추출 관련 명령어
>Ctrl + T

>**변수 자동 추출
>**Ctrl + Alt + V

- Optional로 감싸는 이유는 Null을 방지하는 것 외에도 유용한 메서드들을 제공해주기 때문
## **회원 서비스 테스트

> @BeforeEach

Junit 5 에서 사용되는 어노테이션으로 각각의 테스트 코드가 실행되기 전 먼저 실행되어야 하는 메서드들을 정의하는데 유용한 기능

- 테스트 코드에서 객체 생성과 같은 작업들

> @Test

테스트 어노테이션이며, 각 테스트 명은 한글로 작성해도 됨.

> Given / When / Then

테스트 코드에서 가독성을 끌어올려주는 작성 방법 중 하나
어떤 것들이 주어지고, 주어진 것들이 특정 행위를 했을 때, 그때 발생하는 일
이렇게 크게 세가지의 부분으로 나누어짐

>Assertions.assertThrows()

JUnit 5 에서 제공하는 메서드로, 특정 코드 블럭이 예상된 예외를 잘 발생시키는지 테스트하는 데 사용됨

- 예외 타입 명시적으로 지정 가능
- 람다식 사용 가능
- 예외 객체를 반환하기 때문에 추가적인 검증 가능
```java
memberService.join(member1);  
IllegalArgumentException e = assertThrows(IllegalArgumentException.class, () -> memberService.join(member2));  
  
assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
```
- 위 코드에서 확인할 수 있듯, `IllegalArgumentException e` 에 예외 객체를 저장한 뒤에 추가적으로 getMessage()를 사용해서 예외 메시지도 검증할 수 있음

> 의존성 주입 (Dependency Injection) / DI

테스트 코드와 서비스 코드에서 모두 각각 new를 통해서 레파지토리 객체를 생성한 뒤 사용했었는데, 이렇게 비효율적으로 할 필요가 있을까?

- 테스트 코드에서 객체를 생성한 뒤, 실제 서비스 코드에 객체를 주입하는 방식으로 변경
- 근데 이렇게 해도 되는건가?

- 서비스 코드에서는 생성자를 통해서 레파지토리 변수를 초기화할 수 있게끔 함
- 테스트 코드에서는 우선 레파지토리 객체를 생성하고 서비스 객체의 생성자의 매개변수로 레파지토리 객체를 넘겨줌

`향후 자세히 설명 예정`

## 의존성 주입의 방향성

1. **MemberService 클래스**:
   - MemberService는 생성자를 통해 MemberRepository를 주입받습니다.
   ```java
   public MemberService(MemberRepository memberRepository) {
       this.memberRepository = memberRepository;
   }
   ```
   이는 의존성 주입의 좋은 예시입니다. MemberService는 구체적인 구현체가 아닌 인터페이스(MemberRepository)에 의존합니다.

2. **MemberServiceTest 클래스**:
   - 테스트 클래스에서 MemberService와 MemoryMemberRepository의 인스턴스를 생성하고 연결합니다.
   ```java
   @BeforeEach
   public void beforeEach() {
       memoryMemberRepository = new MemoryMemberRepository();
       memberService = new MemberService(memoryMemberRepository);
   }
   ```


---

# 섹션 5 - 스프링 빈과 의존관계 설정

## 컴포넌트 스캔과 자동 의존관계 설정

```java
package hello.hello_spring.Controller;  
  
import org.springframework.stereotype.Controller;  
  
@Controller  
public class MemberController {  
}
```
- 스프링이 실행될 때 `스프링 컨테이너`가 생성되는데, 거기에 `@Controller` 어노테이션이 있으면 해당 컨트롤러 객체를 생성해서 스프링 컨테이너에 넣어두고 관리하게 된다
- 이런 일련의 과정을 `스프링 컨테이너에서 스프링 빈이 관리된다`고 표현함


```java
@Controller  
public class MemberController {  
      
    private final MemberService memberService = new MemberService();  
}
```
- 또한 컨트롤러에서 서비스를 가져와서 사용해야하는데, 이때 `new` 키워드를 사용해서 직접 객체를 생성한 뒤 사용할 수도 있다
	- 단, 여기에는 하나의 문제가 있다
	- 여러 컨트롤러에서 해당 `MemberService`를 사용할 수 있는데, `MemberService`는 개별적으로 동작할 필요가 없고 하나만 생성해서 공용으로 사용하면 되기 때문이다
- 따라서 스프링을 사용할 때는 스프링 컨테이너에 등록을 하고 스프링이 관리하고, 우리는 그걸 받아서 사용하는 방식으로 코드를 구현해야 한다

```java
package hello.hello_spring.Controller;  
  
import hello.hello_spring.Service.MemberService;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Controller;  
  
@Controller  
public class MemberController {  
  
    private final MemberService memberService;  
  
    @Autowired  
    public MemberController(MemberService memberService) {  
        this.memberService = memberService;  
    }  
}
```
- 이처럼 생성자를 통해서 외부로부터 의존성을 주입받음과 동시에 `@Autowired` 키워드를 이용해서 코드 상에 보이는 `MemberService`를 스프링 컨테이너에서 꺼내와서 자동으로 연결시켜주는 기능을 제공해준다 

추가로, 서비스 코드를 스프링 컨테이너에 등록하는 방법은 다음과 같다

```java
@Service  
public class MemberService {
```
- `@Service` 어노테이션을 통해서 등록해주면 된다


마찬가지로, 리포지토리 코드를 스프링 컨테이너에 등록하는 방법은 다음과 같다

```java
@Repository  
public class MemoryMemberRepository implements MemberRepository {
```
- `@Repository` 어노테이션을 통해서 등록해주면 된다
- 단 이번 경우에서도 알 수 있다싶이 실제 구현체에 어노테이션을 붙여주어야 함


![![Spring/#*Table]]
## 정리

**"스프링 빈을 등록하는 2가지 방법"
- 컴포넌트 스캔과 자동 의존관계 설정
- 자바 코드로 직접 스프링 빈 등록하기

> 컴포넌트 스캔과 자동 의존관계 설정

- `@Component` : 어노테이션이 있으면 스프링 빈으로 자동 등록된다
	- `@Controller` : 컨트롤러가 스프링 빈으로 자동 등록된 이유도 컴포넌트 스캔 때문이다
	- `@Controller`, `@Service`, `@Repository` 해당 어노테이션과 관련된 파일을 살펴보면 `@Component`가 코드 내에 삽입되어 있는 것을 확인할 수 있다.
	- 따라서 해당 어노테이션들 만으로도 컴포넌트를 명시하지 않아도 자동으로 등록되는 것이고 방식의 이름도 `컴포넌트 스캔` 방식이 된 것임

- `@Component` 를 포함하는 다음 어노테이션들도 스프링 빈에 자동 등록된다
	- `@Controller`
	- `@Service`
	- `@Repository`

- 또한 스프링 빈에 등록된 객체들에 대한 의존성을 주입하고 싶을 때는 다음 키워드를 사용하면 된다
	- `@Autowired`

> 참고
> 스프링은 스프링 컨테이너에 스프링 빈을 등록할 때, 기본적으로는 **싱글톤**으로 등록하게 된다(유일하게 하나만 등록해서 공유하는 것). 따라서 같은 스프링 빈이면 모두 같은 인스턴스다. 설정으로 싱글톤이 아니게 설정할 수 있지만 특별한 경우를 제외하면 대부분 싱글톤을 사용한다


## 자바 코드로 직접 스프링 빈 등록하기

>자바 코드로 직접 스프링 빈 등록하기

- 설정 파일을 생성해서 직접 관계를 정의해주면 된다

```java
package hello.hello_spring;  
  
import hello.hello_spring.Repository.MemberRepository;  
import hello.hello_spring.Repository.MemoryMemberRepository;  
import hello.hello_spring.Service.MemberService;  
import org.springframework.context.annotation.Bean;  
import org.springframework.context.annotation.Configuration;  
  
@Configuration  
public class SpringConfig {  
  
    @Bean  
    public MemberService memberService() {  
        return new MemberService(memberRepository());  
    }  
  
    @Bean  
    public MemberRepository memberRepository() {  
        return new MemoryMemberRepository();  
    }  
}
```
- 이처럼 `@Configuration` 어노테이션을 사용해서 설정 파일임을 명시하고, `@Bean` 어노테이션을 사용해서 빈에 등록될 수 있도록 명시하면 된다
- `MemberService`의 객체를 생성하는 경우, `MemberRepository` 에 대한 의존성이 주입되어야 하는데 위와 같은 구조로 구현하면 된다



앞서 언급한 컴포넌트 스캔 방식과 자바 코드로 직접 등록하는 방식은 각각의 장단점이 존재함

- 여기서는 향후 메모리 리포지토리를 다른 리포지토리로 변경할 예정이므로, 컴포넌트 스캔 방식 대신에 자바 코드로 스프링 빈을 설정한 것.
- 나중에는 설정 파일만 변경해주면 완벽하게 대체 가능


> 참고: 자바 코드가 아닌 XML로 설정하는 방식도 있었지만, 최근에는 잘 사용되지 않음

> 참고: DI에는 **필드 주입, Setter 주입, 생성자 주입** 이렇게 3가지 방법이 있다. 의존 관계가 실행 중에 동적으로 변하는 경우는 거의 없으므로 생성자 주입을 권장한다
> **불변성 강조**

> 필드 주입
```
 @Autowired private final MemberService memberService;
```
- 단점으로는 한 번 생성되고 나면 아예 변경될 수 없다는 것
- 즉, 무슨 수를 써도 이걸 변경할 수 있는 방법이 존재하지 않는다

> Setter 주입
```
private MemberService memberService;  
  
@Autowired  
public void setMemberService(MemberService memberService) {  
    this.memberService = memberService;  
}
```
- 단점으로는  public으로 설정해주어야 하기 때문에, 임의로 누군가가 호출하게 됐을 때 객체가 변하게 됨

> 참고: 실무에서는 주로 정형화된 컨트롤러, 서비스, 리포지토리 같은 코드는 컴포넌트 스캔 방식을 이용한다. 그리고 정형화되지 않거나, 상황에 따라 구현 클래스를 변경해야 하면 설정 파일을 통해 스프링 빈을 등록한다

> 주의: `@Autowired`를 통한 DI는 `MemberController`, `MemberService`등과 같이 스프링이 관리하는 객체에서만 동작한다. 스프링 빈으로 등록하지 않고 내가 직접 생성한 객체에서는 동작하지 않는다

---

# 섹션 6 - 회원 관리 예제 - 웹 MVC 개발

## 회원 웹 기능 - 회원가입
- 웰컴 페이지 우선순위
	- @GetMapping("/") > static/index.html
	- 그 이유는 요청이 들어오면 컨트롤러부터 찾은 뒤, 찾지 못했을 때 정적 컨텐츠를 찾아서 띄워주는 것


## 회원 웹 기능 - 등록

**\<MemberController>
```java
@GetMapping("/members/new")  
public String createForm() {  
    return "members/createMemberForm";  
}  
  
@PostMapping("members/new")  
public String create(MemberForm form) {  
    Member member = new Member();  
    member.setName(form.getName());  
  
    memberService.join(member);  
  
    return "redirect:/";  
}
```
- `@GetMapping`은 회원가입 폼을 보여주고 
- `@PostMapping`은 폼 제출시 회원 정보를 처리하여 가입을 수행함
- `redirect:` 가 생략되면 단순히 뷰를 렌더링하기 때문에 주소창 URL이 변경되지 않음
	- 또한 PRG(POST - Redirect - GET) 패턴의 경우에는 리다이렉션이 필수적임
	- 그렇지 않으면 꼬여서 WhiteLabel Error 발생
- 따라서 Spring MVC에서 리다이렉션과 뷰 렌더링을 구분하려면 명시적으로 `redirect:`를 적어주어야 함



## 회원 웹 기능 - 조회

```java
@GetMapping("/members")  
public String list(Model model) {  
    List<Member> members = memberService.findMembers();  
    model.addAttribute("members", members);  
  
    return "members/memberList";  
}
```
- GET 요청 (/members)
- model에 유저의 정보를 넘겨준 뒤 `members/memberList` 를 렌더링 하게끔 명령

```html
<!DOCTYPE HTML>  
<html xmlns:th="http://www.thymeleaf.org">  
<body>  
<div class="container">  
    <div>
	    <table>
			<thead>            
			<tr>                
				<th>#</th>  
                <th>이름</th>  
            </tr>'            
            </thead>            
            <tbody>            
	            <tr th:each="member : ${members}"> 
                <td th:text="${member.id}"></td>  
                <td th:text="${member.name}"></td>  
            </tr>            
            </tbody>        
		</table>    
	</div>
</div> <!-- /container -->  
</body>  
</html>
```

- html 에서는 `Thymeleaf` 템플릿 엔진을 사용
- $ 표시가 의미하는 것은, model 안에서 해당 변수와 똑같은 이름의 값을 꺼내온다는 의미


----

