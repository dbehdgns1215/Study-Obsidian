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


### Cascading 1: 상속
- 작은 폭포, 계단: "상위에서 하위로 단계적으로 적용된다."는 의미.
	- 부모 요소에 지정한 스타일이 자식 요소에도 적용
	- 필요시 자식은 관련 속성을 재정의 할 수 있음.
		- 동일한 속성을 설정한다면 가장 마지막 설정이 적용됨
- 단, 모든 속성이 상속되는 것은 아니다.
![[Pasted image 20250805092448.png]]
- 상속되지 않는 속성을 상속받기 위해서는 값에 `inherit` 키워드를 사용하면 됨

### Cascading 2: 중요도 - 명시도 - 로드 순서
- style sheet는 중요도에 따라 3가지 단계의 origin으로 구성 - `user agent`, `user`, `author`
	- `user agent`
		- 웹 브라우저가 미리 설정해 놓은 스타일로 가장 낮은 우선 순위를 가짐
		- "이 브라우저의 기준은 이렇습니다!"
	- `user`
		- 사용자가 자신의 브라우저 설정이나 사용자 스타일 시트에 적용한 스타일
		- "나는 이렇게 보고 싶어" - 거의 사용되지 않음
	- `author`: 웹 페이지를 작성한 개발자가 정의한 스타일
		- "우리 사이트는 이렇게 보였으면 좋겠어"
- 우선 순위 적용 순서는 얼마나 중요한가?
![[Pasted image 20250805092937.png]]
- `User normal Style Sheet`, `User important Style Sheet`는 잘 사용되지 않음.
- inherited style sheet에서는 `!important` 무시함.
	- 즉, 상속 받은 CSS 에서는 그것이 중요하지 않음.
```css
p {
	color: red !important
}
```

### Cascading 3
- 만약 중요도가 같다면 다음으로는 명시도를 확인
	- 명시도는 선택자를 이용해서 우선 순위를 정하기 위한 값
		- 얼마나 한정 지을 수 있는가?
	- X - Y - Z 의 3가지 숫자로 명시도를 매기며 마치 금 - 은 - 동과 유사
	- X: ID 선택자의 개수
	- Y: class 선택자, 속성 선택자, 가상 클래스 선택자의 개수
	- Z: 타입 선택자, 가상 요소 선택자의 개수
- 만약 명시도마저 똑같다면 로드된 우선 순위에 의해 결정됨.
![[Pasted image 20250805093222.png]]


### CSS 선택자
- HTML 문서에서 CSS 규칙을 적용할 대상을 선택하기 위한 표현식
- CSS 뿐만 아니라 자바스크립트, Emmet 등 다양한 분야서 활용

**기본 선택자**
![[Pasted image 20250805093736.png]]

**복합 선택자**
![[Pasted image 20250805094345.png]]

**속성 선택자**
![[Pasted image 20250805094801.png]]

**가상 클래스 선택자**
- 실제 class 형태로 존재하진 않지만 상황에 따라 적용되는 class를 지정하기 위한 것으로 class 이름 앞에 `:` 가 추가됨
	- 개발자가 태그에 calss를 지정할 필요는 없음
- 사용자 동작에 반응하는 가상 클래스, 구조적 가상 클래스, 상태 기반 클래스 등이 있음.

**사용자 동작에 반응하는 가상 클래스**
![[Pasted image 20250805095422.png]]

**구조적 가상 클래스 (위치/순서 기반의 가상 클래스)**
![[Pasted image 20250805095411.png]]

**상태 기반 가상 클래스 선택자**
![[Pasted image 20250805095716.png]]

**가상 엘리먼트 선택자**
- 보이지 않는 가상의 요소를 선택하기 위한 선택자로 엘리먼트 이름 앞에 `::` 추가
![[Pasted image 20250805095844.png]]

**실습**
```css
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>아이언맨 팬 페이지</title>
    <style>
      /* TODO: 01. 모든 요소를 선택하세요 */
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      /* TODO: 02. body 태그를 선택하세요 */
      body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        padding: 20px;
      }

      /* TODO: 03. main-title이라는 id를 가진 요소를 선택하세요 */
      #main-title {
        color: #e62429;
        text-align: center;
        margin-bottom: 30px;
      }

      /* TODO: 04. movie-title이라는 클래스를 가진 요소를 선택하세요 */
      .movie-title {
        color: #4a4a4a;
        font-size: 1.5em;
        margin: 15px 0;
      }

      /* TODO: 05. movie-info 클래스를 가진 요소의 직계 자식 p태그를 선택하세요 */
      .movie-info > p {
        margin-bottom: 10px;
        color: #666;
      }

      /* TODO: 06. movie-section 클래스를 가진 요소 아래의 모든 span 태그를 선택하세요 */
      .movie-section span {
        color: #e62429;
        font-weight: bold;
      }

      /* TODO: 07. movie-title 클래스를 가진 요소에 마우스를 올렸을 때를 선택하세요 */
      .movie-title:hover {
        color: #e62429;
        cursor: pointer;
      }

      /* TODO: 08. highlight와 important 클래스를 모두 가진 요소를 선택하세요 */
      .highlight.important {
        background-color: #ffe6e6;
        padding: 10px;
      }

      /* TODO: 09. h2 바로 다음에 오는 p 태그를 선택하세요 */
      h2 + p {
        font-style: italic;
      }

      /* TODO: 010. alt 속성에 'Iron Man'이라는 텍스트를 포함하는 img 태그를 선택하세요 */
      img[alt*="Iron Man"] {
        border: 3px solid #e62429;
        border-radius: 10px;
      }

      /* TODO: 11. .movie-info 안의 첫 번째 p 태그를 선택하세요 */
      .movie-info p:first-child {
        font-weight: bold;
        border-bottom: 1px solid #e62429;
      }

      /* TODO: 12. 체크된 상태의 라디오 버튼을 선택하세요 */
      input[type="radio"]:checked + label {
        color: #e62429;
        font-weight: bold;
      }
    </style>
  </head>
```

### box model
- 텍스트, 이미지 등의 모든 콘텐츠를 사각의 박스 형태로 관리하는 모델
- HTML의 모든 요소는 사각형의 박스 모델이고 block 요소는 위에서 아래로, inline 요소는 왼쪽에서 오른쪽으로 배치됨
- box는 content, padding, border, margin으로 구성됨
![[Pasted image 20250805103050.png]]


#### content 영역
![[Pasted image 20250805103113.png]]
#### display 속성
- block 요소는 width와 height를 갖지만, inline 요소에서는 무시됨
	- 즉, span에게 width, height를 줘봤자 무의미함.

#### padding 영역
- content와 border 사이의 여백
![[Pasted image 20250805103656.png]]

#### block 요소와 inline 요소의 padding 차이
![[Pasted image 20250805103805.png]]
- 위 내용은 border나 margin도 마찬가지로 적용됨

![[Pasted image 20250805103829.png]]

#### border 영역
- padding을 밖에서 감싸고 있는 테두리
![[Pasted image 20250805104032.png]]
- `border-top-left-radius: 20px;`
#### box-sizing
- width와 height를 측정할 때의 기준 설정
![[Pasted image 20250805104316.png]]
- `inner1` 의 box-size는 240px
- `inner2` 의 box-size는 200px
	- box-sizing이 `content-box`냐 또는 `border-box`냐에 따른 차이

#### margin 영역
- border 외부에서 다른 요소와의 거리
![[Pasted image 20250805105354.png]]
#### block 요소와 inline 요소의 margin
- inline 요소는 padding과 마찬가지로 좌우 margin만 가질 수 있으며 상하 마진은 의미 없음
- block 요소끼리의 상하 마진은 병합(더 큰 마진 값 하나만 적용)되며 수평 margin은 각자의 margin을 유지.
	- 단, 요소의 일반적인 문서의 흐름을 벗어나는 경우 margin 병합은 발생하지 않음
![[Pasted image 20250805105528.png]]

#### box를 활용한 기본 레이아웃 구성
- 가운데 정렬
	- div의 width를 고정한 채 상하 margin을 0으로 두고 좌우 margin을 auto로 구성
- header, footer 고정
	- header + footer + main의 height가 viewport를 채우도록 함
		- 100vh
	- header와 footer의 height를 고정
	- 나머지 공간을 main이 모두 가져갈 수 있도록 처리
![[Pasted image 20250805105648.png]]

![[Pasted image 20250805105656.png]]


# Day 12

## display 속성
- 웹페이지의 레이아웃을 결정하는 중요한 속성

![[Pasted image 20250806090631.png]]

### block과 imline, inline-block
![[Pasted image 20250806090737.png]]

## block 요소의 가로 방향 배치
![[Pasted image 20250806092713.png]]

## float
![[Pasted image 20250806092725.png]]

## clear
![[Pasted image 20250806092944.png]]


## flexible box model
![[Pasted image 20250806093641.png]]

**flex container에게 적용되는 속성**
![[Pasted image 20250806093809.png]]
![[Pasted image 20250806094036.png]]


## flex item에게 적용되는 속성
![[Pasted image 20250806095215.png]]

## none
![[Pasted image 20250806095952.png]]

## position
![[Pasted image 20250806101706.png]]

### position 속성

### static
![[Pasted image 20250806101727.png]]

### relative
![[Pasted image 20250806101754.png]]

### absolute
![[Pasted image 20250806102120.png]]

### fixed
![[Pasted image 20250806102837.png]]

### etc
![[Pasted image 20250806103319.png]]
- `sticky`
	- 타이틀 같은 것들을 상단에 고정 시켜놓고 싶을 때.
	- 일부 스크롤이 가능하나 임계치를 넘어가면 고정됨



## 반응형 웹
![[Pasted image 20250806103941.png]]
- 반응형 웹을 구현할 때 써야하는 기술은 바로 `미디어 쿼리`

### 미디어 쿼리
![[Pasted image 20250806104041.png]]

![[Pasted image 20250806104722.png]]

**조건 활용**
![[Pasted image 20250806104759.png]]


# Day 13

## JavaScript
![[Pasted image 20250807090511.png]]
- 호스트 실행 환경: 브라우저

### Html 파일 내에 `<script>` 태그를 이용한 영역 표시
![[Pasted image 20250807091040.png]]

### 외부 파일 링크
![[Pasted image 20250807091234.png]]

### inline 방식
![[Pasted image 20250807091413.png]]

## 변수와 자료형

**기본 특징**
![[Pasted image 20250807092212.png]]

**변수의 선언 지시어**
![[Pasted image 20250807092349.png]]

**변수의 선언과 값의 할당**
![[Pasted image 20250807092739.png]]

**변수 선언 지시어 및 스코프**
![[Pasted image 20250807092847.png]]

**변수 선언 지시어 별 scope 확인**
![[Pasted image 20250807093600.png]]

### 자료형
![[Pasted image 20250807093716.png]]

#### 기본형
![[Pasted image 20250807093741.png]]

#### 숫자 타입
![[Pasted image 20250807094352.png]]
![[Pasted image 20250807094404.png]]

#### 문자열 (string)
![[Pasted image 20250807094424.png]]

#### 템플릿 문자열
![[Pasted image 20250807094639.png]]

#### boolean
![[Pasted image 20250807095039.png]]
- 위에 언급된 5가지 경우(falsy) 외에는 모두 `true`

#### undefined와 null
![[Pasted image 20250807095251.png]]

#### 참조형
![[Pasted image 20250807095525.png]]

#### JavaScript의 객체
![[Pasted image 20250807095545.png]]

#### 배열
![[Pasted image 20250807095714.png]]

#### 배열 객체
![[Pasted image 20250807095952.png]]

#### 사용자 정의 Object의 생성
![[Pasted image 20250807100030.png]]

#### 객체의 속성 관리
![[Pasted image 20250807100203.png]]


### 연산자

#### 산술연산
![[Pasted image 20250807102120.png]]

![[Pasted image 20250807102136.png]]

#### 비교 연산
![[Pasted image 20250807102218.png]]

#### 비교 연산의 형 변환
![[Pasted image 20250807102620.png]]

#### short-circuit 논리 연산자
![[Pasted image 20250807102642.png]]


### 조건문
![[Pasted image 20250807102900.png]]

### 다양한 형태의 for 문장 제공
![[Pasted image 20250807102947.png]]

### 예외 처리 구문
![[Pasted image 20250807103318.png]]

## function

### 다시 한 번 JavaScript는
![[Pasted image 20250807103441.png]]

#### function 기본 형태
![[Pasted image 20250807103835.png]]
- `myFunc(1, 2, 3, 4, 5)`는 어떻게 처리할 수 있을까? 버리진 않을텐데?

#### 다양한 정의 방법
![[Pasted image 20250807104022.png]]
![[Pasted image 20250807104039.png]]

#### 함수 호이스팅
![[Pasted image 20250807104501.png]]
![[Pasted image 20250807104807.png]]

#### 생성자로서의 function (잘 안씀)
![[Pasted image 20250807105452.png]]

#### 대신 class 활용 권장
![[Pasted image 20250807105517.png]]


#### first class citizen
![[Pasted image 20250807105535.png]]

#### 인자로 활용된 function
![[Pasted image 20250807105608.png]]


# Day 14

## 이벤트 처리 기본
### event와 event listener
![[Pasted image 20250808090455.png]]

### event listener 등록 방식
![[Pasted image 20250808090755.png]]
![[Pasted image 20250808091205.png]]

#### event source 가져오는 방법의 비교
![[Pasted image 20250808092032.png]]


## DOM
![[Pasted image 20250808092214.png]]

### Node의 기본 속성
![[Pasted image 20250808092354.png]]

### Element의 조회

#### document를 통한 조회
![[Pasted image 20250808092546.png]]
#### 조회된 element와의 관계를 이용한 탐색
![[Pasted image 20250808092922.png]]

#### Node의 생성
![[Pasted image 20250808094355.png]]


#### Node의 생성
![[Pasted image 20250808094550.png]]
