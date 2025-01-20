
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


## **빌드하고 실행하기

---

# **섹션 3 - 스프링 웹 개발 기초

## **정적 컨텐츠


## **MVC와 템플릿 엔진


## **API


---

# 섹션 4 - 회원 관리 예제 - 백엔드 개발

## **비즈니스 요구사항 정리


## **회원 도메인과 리포지토리 만들기


## **회원 리포지토리 테스트 케이스 작성


## **회원 서비스 개발


## **회원 서비스 테스트


---
