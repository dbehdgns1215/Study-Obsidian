# Day 10
- 웹 프로그램
	- 네트워크 너머의 서버에서 존재하며 HTTP를 통해서 서비스되는 프로그램

![[Pasted image 20250804090534.png]]

- HTML
	- 페이지 구조와 내용
	- 이미지 링크 ...
	- 저수준 상호작용
- CSS
	- 페이지 디자인
	- 컬러, 폰트 ...
	- 위치 배치 ...
- JavaScript
	- 이벤트 처리
	- 고수준 상호작용
	- 프로그래밍 처리

## Markup Language
![[Pasted image 20250804090930.png]]

- HTML, DOM Tree
![[Pasted image 20250804091118.png]]

## HTML 5의 주요 특징
![[Pasted image 20250804091158.png]]

## HTML
![[Pasted image 20250804092258.png]]
- 위와 같이 영역별로 역할을 분리 해놓은 게 웹 표준

### Tag
![[Pasted image 20250804092434.png]]

**용도에 따른 Tag의 종류**
![[Pasted image 20250804092459.png]]

**Block 요소와 Inline 요소**
![[Pasted image 20250804092557.png]]

### Tag의 Attribute(속성)
![[Pasted image 20250804093154.png]]

#### Global 속성
![[Pasted image 20250804093310.png]]

#### 문서의 구조
![[Pasted image 20250804093447.png]]

- 주석은 `<!--주석 내용-->`
	- 참고로 사용자에게 그대로 전달되니 조심해야 함.

#### 특수문자와 공백
![[Pasted image 20250804093702.png]]

#### emmet
![[Pasted image 20250804093858.png]]

### 기본 태그
#### heading
![[Pasted image 20250804094750.png]]
- `h$*6{Heading $}`

#### list
![[Pasted image 20250804095007.png]]
- `<!--TODO: 01. 야구의 포지션을 내야수, 외야수, 기타로 그룹핑해서 표현해보자.-->`
- `<!-- 단 그룹은 순서가 없고 포지션은 우측이 우선순위가 높다.-->`
	- ![[Pasted image 20250804095317.png]]

#### table
![[Pasted image 20250804100512.png]]

![[Pasted image 20250804100605.png]]
- `<!--TODO: 01. thead, tbody, tfoot를 지우고 스타일이 적용되지 않는 이유를 생각해보자.-->`
	- 자동으로 생성됨.
		- DOM을 잘 파악해야함.
		- 크롬같은 브라우저는 DOM으로 인식하기 때문

#### table 병합
![[Pasted image 20250804101140.png]]
- 1 row
	- 2개
- 2 row
	- 3개
- 3 row
	- 2개

#### img
![[Pasted image 20250804101629.png]]
```html
    <!-- TODO: 01. resource/wedding.jpg와 rocks.jpg를 절대/상대 경로로 출력해보자. -->
    img[src=/resource/wedding.jpg]
    <img src="/resource/wedding.jpg" alt="" />
    img[src=../../resource/rocks.jpg]
    <img src="../../resource/rocks.jpg" alt="" />
    <!--END-->
```
- `lazy`, `eager`
	- 현재 보여지는 페이지에 대해서 이미지 로딩 -> `lazy`
	- 사이트 접근 시 모든 이미지 로딩 -> `eager`
		- 웹툰 사이트를 생각해보면 됨

![[Pasted image 20250804102031.png]]
- 기본적으로 눈에 보이는 400 ~ 403이 lazy 로딩됨과 동시에 499번 이미지도 eager 로딩된 것을 볼 수 있음

#### a
![[Pasted image 20250804102220.png]]

![[Pasted image 20250804102357.png]]
```html
    <h1>basic link</h1>
    <!--TODO: 01. a 태그를 이용하여 구글로 이동하는 링크를 작성해보자.-->
    <!--구글(새창) | 싸피(현재창)-->
    a[href=http://www.google.com target=_blank]{구글로}
    <a href="http://www.google.com" target="_blank">구글로</a>
    a[href=http://www.ssafy.com]{싸피}
    <a href="http://www.ssafy.com">싸피로</a>
    <!--END-->
```

```html
    <!--TODO: 02. '글보기'와 '이미지맵' 링크를 만들어보자-->
    <!-- 글보기 | 이미지맵 -->
    a[href=#text]{글보기}
    <a href="#text">글보기</a>
    a[href=#map]{이미지 맵}
    <a href="#map">이미지 맵</a>
    <!--END-->
```


#### form
![[Pasted image 20250804102915.png]]

![[Pasted image 20250804102945.png]]

![[Pasted image 20250804103147.png]]

#### input
![[Pasted image 20250804103354.png]]
- name, value -> 서버로 전달되는 값들

#### label
![[Pasted image 20250804103722.png]]


#### Snipet
![[Pasted image 20250804103917.png]]

#### form
![[Pasted image 20250804104234.png]]
```html
    <!--TODO: 01. 서버로 username과 comment를 전달하기 위한 form을 만들어보자.-->
    <!--form>filedset>legend-->
    <form action="#">
      <fieldset>
        <legend>form test</legend>
        <label for="username">username: </label>
        <input type="text" id="username" name="username" value="hong" />
        <label for="">comment</label>
        <textarea name="comment" id="comment">
comment
        </textarea>
      </fieldset>
      <button>get</button>
      <button>post</button>
    </form>
    <!--END-->
```
![[Pasted image 20250804104930.png]]

![[Pasted image 20250804104713.png]]
- 회원가입
	- POST
- 검색
	- GET
- 로그인
	- POST (?)
- 글 보기
	- GET

```html
      <button formmethod="get">get</button>
      <button formmethod="post">post</button>
```
**GET**
![[Pasted image 20250804105204.png]]
**POST**
![[Pasted image 20250804105218.png]]

#### input의 type
![[Pasted image 20250804105402.png]]
- 빨간색 부분은, HTML 5에 추가된 기능
	- 스마트 폰을 타겟으로 추가된 기능임.

![[Pasted image 20250804105618.png]]

#### input의 기타 속성
![[Pasted image 20250804105726.png]]

#### checkbox와 radio 타입
![[Pasted image 20250804105803.png]]
- input과 label이 연결되어 있지 않으면 체크 불가능

#### button
![[Pasted image 20250804110021.png]]
- `type`이 중요함.

#### select
![[Pasted image 20250804110154.png]]

### Semantic 태그
![[Pasted image 20250804113054.png]]
- 아무 것도 없으면
	- 태그
- \#
	- id
- .
	- 클래스

![[Pasted image 20250804114442.png]]


# Day 11

## Cascading Style Sheets
- 문서 내에서 내용과 상관없이 스타일을 처리하는 기술
- 수시로 변경되는 웹 화면의 디자인 요소를 HTML에서 분리
- 장점
	- 문서와 디자인의 분리로 소스의 관리와 수정이 용이함 = 유지 보수성 향상
	- PC, Mobile 등 다양한 기기별 디자인 적용이 용이함
	- 웹 문서 제작 기간 단축 및 일관성 유지가 용이함

**기본 문법**
- CSS는 선택자와 선언부로 구성
![[Pasted image 20250805091141.png]]

- 선택자: 정의한 스타일을 적용할 대상
- 선언부: 선택자에 적용할 스타일로 {} 안에 작성하며 여러 개일 경우 ; 으로 구분
	- 속성: 지정할 속성 (color, font-size, ...)
	- 값: 지정할 값 (`blue;`, `12px;`, ...)
- 주석: multiline 형태 (\/\*주석 내용\*\/)의 주석 사용

### 스타일 적용 방법

#### 인라인 스타일
- 개별 태그들에 `style=property: value;` 형태로 지정
- 별도로 선택자를 사용하지는 않으며 재사용도 불가능함.
- 일반적으로 다른 스타일에 비해 강력한 우선 순위를 가짐

#### 내부 스타일
- 일반적으로 `<head>`의 `<style>`에 집중해서 작성
- 해당 html 내에서는 선택자 기준으로 재사용 가능
- 페이지에 특화된 내용 작성

#### 외부 스타일 시트 활용
- 외부에 있는 별도의 스타일 시트 파일(.css)를 만들고 `<link>` 태그로 연결
	- 모든 페이지에서 재사용 가능
- `@import`
- link와 달리 style tag 안에 설정하며 다른 CSS 파일 내부에서도사용 가능
- `<style> 태그의 맨 상단에 위치해야 함.`
- `@import url("file path");` 또는 `@import "file path";` 형태로 사용


