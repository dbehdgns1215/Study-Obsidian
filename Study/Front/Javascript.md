
# 변수 선언

**const, let**
- const
	- 값 변경이 불가능함.
- let
	- 값 변경이 가능함.

**변수에 담을 수 있는 값**
- 숫자
- 문자
	- `' '`
	- `" "`
- boolean
	- `true`
	- `false`
- 배열
- 객체


# 함수

`function` `함수명` `(매개변수...)` `{`
	`로직 ...`
	`return 변수` `-> 가능`
`}`

**함수 선언의 두가지 방식**
- 함수 선언문
  ```javascript
	function add(a, b) {
		return a + b;
	}
	```
- 특징
	- 코드 실행 전에 **호이스팅**됨
		- 선언 위치와 상관없이 사용 가능
	- 전역 또는 블록 스코프에서 정의됨

- 함수 표현식
  ```javascript
	const add = function(a, b) {
		return a + b;
	};
	```
- 변수에 함수 객체를 할당하는 형태
- **호이스팅 불가**
- 익명 함수(이름 없는 함수)를 주로 사용하지만, 이름을 붙인 표현식도 가능

- 화살표 함수
 ```javascript
 const add = (a, b) => a + b;
 ```
 - `this` 바인딩이 없음
 - 간결하고 콜백 함수 작성시에 자주 사용됨


일급 함수로서의 자바스크립트
- 함수가 변수처럼 어디든 할당될 수 있다는 특징

```javascript
function logText(message) {
	message();
}

logText(function() {
	console.log('hi');
});
```
- 결과로 `hi`가 출력됨
- 분명 매개변수를 넘겨줬을 뿐인데, 어떻게 함수로서 동작하는걸까?


