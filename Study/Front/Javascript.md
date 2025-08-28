
# 변수 선언

### `const` 와 `let`

- **`const`**
    - 재할당(값 변경)이 불가능함.
    - 단, **객체나 배열의 내부 값은 변경 가능**함.
```javascript
const arr = [1, 2, 3];
arr.push(4); // 가능
arr = [5, 6]; // 불가능 (재할당)
```
- **`let`**
    - 재할당이 가능함.
    	- 블록 스코프(block scope)를 가짐.
```javascript
if (true) {
	let x = 10;
	console.log(x); // 10
}
console.log(x); // ReferenceError
```

### `var` (추가 참고)
- ES6 이전에 사용되던 방식
- 함수 스코프(function scope)만 지원
- **호이스팅** 시 값이 `undefined` 로 초기화되어 예기치 못한 오류를 유발할 수 있음
- 요즘은 `let`/`const` 권장

---

# 자료형

- 숫자(Number)
- 문자열(String)
    - `'작은따옴표'`, `"큰따옴표"`, `백틱(템플릿 리터럴)`
    - 템플릿 리터럴은 문자열 내 변수/표현식 사용 가능
```javascript
const name = "철수";
console.log(`안녕, ${name}`); // 안녕, 철수
```

- 불리언(Boolean) → `true`, `false`
- 배열(Array)
- 객체(Object)
- null / undefined (값 없음)

---

# 함수

### 함수 선언문

```javascript
function add(a, b) {
  return a + b;
}
```
- **호이스팅**: 코드 실행 전에 메모리에 등록됨  
    → 정의 위치와 상관없이 먼저 호출 가능
- 전역 또는 블록 스코프에서 사용 가능

---

### 함수 표현식

```javascript
const add = function(a, b) {
  return a + b;
};
```
- 변수에 익명/기명 함수를 할당하는 형태
- **호이스팅 불가** (정확히는, 변수 자체는 호이스팅되지만 함수 값은 아직 할당되지 않음)
- 실행 시점에 평가됨

---

### 화살표 함수

```javascript
const add = (a, b) => a + b;
```
- `this`, `arguments`, `super`, `new.target` 을 바인딩하지 않음
- `return` 생략 가능 (단, 표현식 한 줄일 때만)
- 객체 리터럴 반환 시 `()` 로 감싸야 함
```javascript
const f = () => ({ a: 1 });
```

---

# 모든 경우의 수 정리

```javascript
// (1) 매개변수 1개, 한 줄
const f1 = x => x * 2;

// (2) 매개변수 1개, 여러 줄
const f2 = x => {
  console.log(x);
  return x * 2;
};

// (3) 매개변수 2개 이상
const f3 = (x, y) => x + y;

// (4) 매개변수 없음
const f4 = () => "hi";

// (5) 객체 리터럴 반환
const f5 = () => ({ a: 1, b: 2 });
```

---

# 일급 객체(First-class citizen)로서의 함수

자바스크립트에서 **함수도 값(value)** 이다.  
→ 즉, **변수에 할당, 다른 함수에 인자 전달, 다른 함수의 반환값으로 사용**할 수 있음.

```javascript
function logText(callback) {
  callback();  // 함수 실행
}

logText(function() {
  console.log('hi');
});
```
- `logText`는 **함수를 인자로 받음**
- 인자로 넘긴 익명 함수가 실행되어 `'hi'` 출력

📌 이게 가능한 이유:
- 자바스크립트에서는 함수도 **객체(Object)** 의 한 종류이기 때문  
    → `typeof functionName === "function"`  
    → 내부적으로는 **객체 + 실행 가능한 코드** 를 가진 특별한 값

---

# 고급 활용 예시

### (1) 콜백 함수

```javascript
function repeat(n, action) {
  for (let i = 0; i < n; i++) {
    action(i);
  }
}

repeat(3, console.log);
// 0, 1, 2 출력
```

### (2) 고차 함수 (Higher-Order Function)

- 함수를 반환하거나, 인자로 받는 함수

```javascript
function multiplier(factor) {
  return number => number * factor;
}

const double = multiplier(2);
console.log(double(5)); // 10
```

### (3) 배열 메서드에서 자주 사용

```javascript
const arr = [1, 2, 3, 4];
const doubled = arr.map(x => x * 2);
console.log(doubled); // [2, 4, 6, 8]
```

---

👉 정리
- `let`/`const`는 스코프와 재할당 가능 여부가 다름
- 함수는 **선언문/표현식/화살표 함수** 세 가지 방식
- 자바스크립트 함수는 **일급 객체**라서, 값처럼 다룰 수 있고 고차 함수 패턴을 만들어낼 수 있음



- 연산자
- 자료형
- 호이스팅
- BOM 객체
- DOM 접근 및 활용
- function 선언 함수
- arrow function 함수
- addEventListener
- form 태그 전송 방식 2가지 특징
- async/awiat, Promise.then() 비교 및 장점
- 코드 실행 결과가 많이 나올 듯
