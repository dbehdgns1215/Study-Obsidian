# @RequestBody, @RequestParam, @ResponseBody

- **@RequestBody** → 바디(JSON 등) 통째로 객체로 매핑
- **@RequestParam** → URL 쿼리 파라미터 or ?뒤에 오는 값
- **@ResponseBody** → 리턴값을 그대로 JSON 등으로 응답(요즘은 생략 가능)

---

## @RequestBody — “요청 바디(JSON)” 가져오기

클라이언트가 아래처럼 **JSON 바디**를 보내면:

```json
{
  "name": "동훈",
  "age": 26
}
```

컨트롤러에서 받는 법:

```java
@PostMapping("/user")
public User saveUser(@RequestBody User user) {
    return user;
}
```

✔ JSON → User 객체로 자동 변환  
✔ 주로 POST, PUT 같은 **바디 있는 요청**에서 사용

---

## @RequestParam — “URL 쿼리 파라미터” 받는 것

예:  
`GET /search?keyword=apple&page=2`

```java
@GetMapping("/search")
public String search(@RequestParam String keyword,
                     @RequestParam(defaultValue="1") int page) {
    return keyword + " / " + page;
}
```

✔ URL에 붙는 값 받아옴  
✔ ? 뒤에 오는 값, form-data도 됨  
✔ 기본 타입(String, int 등) 받기 좋아

---

## @ResponseBody — “리턴값을 JSON으로 응답”

```java
@GetMapping("/hello")
@ResponseBody
public String hello() {
    return "hi";
}
```

✔ 리턴값을 뷰(View)로 보내지 말고 **그대로 응답 본문에 쓰라는 의미**

📌 **주의:**  
`@RestController` 쓰면 **자동으로 @ResponseBody 포함됨**  
그래서 요즘은 거의 안 씀.

```java
@RestController
public class UserController {
    @GetMapping("/hi")
    public String hi() {
        return "hello";
    }
}
```


## 📌 Jackson(JSON 파싱) 기준에서의 핵심

### 요청(@RequestBody) 받을 때 → **setter가 있어야 함**
- 역직렬화
- JSON → 객체로 만들 때 값 넣어야 하니까
### 응답(@ResponseBody) 보낼 때 → **getter만 있어도 됨**
- 직렬화
- 객체 → JSON 변환은 getter만 보고 함

---


# `Jackson` 은 어떻게 동작하는가?

`Spring`**3.0** 이후로 **컨트롤러**의 리턴 방식이 `@RequestBody` 형식이라면,  `Spring`은 `MessageConverter` **API** 를 통해, **컨트롤러**가 리턴하는 객체를 후킹 할 수 있습니다.

`Jackson`은 `JSON`데이터를 출력하기 위한  `MappingJacksonHttpMessageConverter`를 제공합니다. 만약 우리가 스프링 **MessageConverter**를 위의 `MappingJacksonHttpMessageConverter`으로 등록한다면, **컨트롤러**가 리턴하는 객체를 다시 뜯어(**_자바 리플렉션 사용_**), `Jackson`의 **ObjectMapper** **API**로 `JSON 객체`를 만들고 난 후, 출력하여 `JSON`데이터를 완성합니다.

더욱 편리해진 점은, `Spring` **3.1** 이후로 만약 클래스패스에 `Jackson` 라이브러리가 존재한다면, ( 쉽게 말해**_Jackson을 설치했느냐 안했느냐_** ) 자동적으로 **MessageConverter**가 등록된다는 점입니다.

덕분에 우리는 아래와 같이 매우 편리하게 사용할 수 있습니다.
```java
@RequestMapping("/json")  
@ResponseBody()  
public Object printJSON() {  
    Person person = new Person("Mommoo", "Developer");  
    return person;  
}
```

> 출처
> https://mommoo.tistory.com/83



---


# ResponseEntity

➡ **HTTP 응답 전체를 네가 직접 구성해서 반환하는 객체**
HTTP 응답은 3가지 요소로 이루어짐:
1. **Status Code** (예: 200, 400, 404, 500)
2. **Headers**
3. **Body(JSON)**

일반적으로는 `return UserDto` 이런 식으로 바디만 반환했는데,  
ResponseEntity는 이걸
-  상태코드  
- 헤더  
 - 바디

## 왜 쓰냐?

예를 들어 아래 상황들:
- 성공이면 `201 Created` 보내고 싶음
- 실패하면 `400 Bad Request` 보내고 싶음
- Location 같은 헤더 추가하고 싶음
- JSON 말고 파일 반환하고 싶음
- 비즈니스 로직에 따라 응답 코드를 명확하게 나누고 싶음

이때 `return dto;` 만으로는 부족하니까 쓰는 거임.

---
## 기본 예시 (가장 흔함)

```java
@GetMapping("/hello")
public ResponseEntity<String> hello() {
    return ResponseEntity.ok("안녕");
}
```

응답:
```
HTTP/1.1 200 OK
Content-Type: text/plain
Body: 안녕
```

---
## JSON 반환도 이렇게

```java
@GetMapping("/user")
public ResponseEntity<Map<String, Object>> getUser() {
    Map<String, Object> result = new HashMap<>();
    result.put("name", "동훈");
    result.put("age", 26);
    
    return ResponseEntity.ok(result);
}
```
- Map을 넣었으니 자동으로 JSON 직렬화됨  (by Jackson)
- 상태코드는 200

---
## 상태코드 바꾸기

예: 회원가입 성공 → 201 Created

```java
@PostMapping("/user")
public ResponseEntity<User> createUser(@RequestBody User user) {
    return ResponseEntity.status(201).body(user);
}
```

---
## 상태코드 + 헤더 + 바디 모두 커스텀

```java
return ResponseEntity
        .status(HttpStatus.CREATED)
        .header("X-User-Id", "123")
        .body(new UserResponse("홍길동"));
```

---

## 자주 쓰는 정적 메서드

| 코드                    | 사용      |
| --------------------- | ------- |
| `ok(body)`            | 200 응답  |
| `badRequest().body()` | 400 응답  |
| `notFound().build()`  | 404 응답  |
| `noContent().build()` | 204 응답  |
| `status(code).body()` | 임의 상태코드 |

예:

```java
return ResponseEntity.badRequest().body("입력값이 잘못됨");
```

---

## 결국 ResponseEntity는?

**"스프링이 응답을 만들 때 상태코드/헤더/바디를 다 네가 직접 구성하게 하는 박스"**


```java
@PostMapping("/signin")
public ResponseEntity<?> signin(@RequestBody SigninRequest request) {
    // ↑ 반환 타입              ↑ 요청 받기
    //   (보낼 때)                 (받을 때)
}
```

### SigninRequest는 어떻게 받는가?

### Vue에서 보내는 JSON
```javascript
axios.post('/api/user/signin', {
  email: 'test@test.com',
  password: '1234'
})
```

### 실제 HTTP 요청
````http
POST /api/user/signin HTTP/1.1
Content-Type: application/json

{"email":"test@test.com","password":"1234"}
```

### Spring Boot의 Jackson이 변환
```
JSON 문자열                          SigninRequest 클래스
┌──────────────────────────┐        ┌───────────────────────────┐
│ {                        │        │ public class              │
│   "email": "test@...",   │   →    │   SigninRequest {         │
│   "password": "1234"     │        │   private String email;   │
│ }                        │        │   private String password;|
└──────────────────────────┘        │ }                         │
                                    └───────────────────────────┘

                                     SigninRequest 객체
                                     ┌─────────────────────────┐
                                     │ email = "test@test.com" │
                                     │ password = "1234"       │
                                     └─────────────────────────┘
````

---

# 언제 재빌드 하면 되나?

## 재빌드(이미지/아티팩트 새로 만드는 것) **필요한 경우**

- **Java 코드 변경 (.java)**  
    → `mvn package`(또는 Gradle 빌드)로 .jar/.class 만든 뒤 이미지를 새로 빌드해야 변경 반영.  
    _단, 개발용으로 소스 폴더를 컨테이너에 바인드 마운트하고 `mvn spring-boot:run` 또는 devtools로 실행하면 이미지 재빌드 없이도 반영 가능._
- **리소스 파일 변경(프로덕션에 패키징된 .xml, .properties)**  
    → 이 파일들이 JAR 안에 패키징돼 있다면 **재빌드 + 이미지 재생성** 필요.  
    _대신 로컬 파일을 컨테이너에 마운트하면 컨테이너 재시작만으로 반영 가능._
- **의존성 추가/변경 (pom.xml / build.gradle)**  
    → 빌드 결과물이 바뀌니 **무조건 재빌드 필요**(jar 재생성 + 이미지 재빌드).
- **Dockerfile 변경 / 베이스 이미지 변경**  
    → 이미지 구성 자체가 바뀌므로 **이미지 재빌드 필요**.
- **프런트엔드(프로덕션) 빌드 변경 (vite 빌드 설정 등)**  
    → `npm run build` 하여 정적파일을 만들고 그걸 이미지에 포함한다면 **재빌드 필요**.

---

## 재빌드 불필요한 경우 (재시작 / 재생성만으로 OK)

- **환경변수 변경 (.env 파일)**  
    → 이미지 재빌드 불필요. 컨테이너 재시작(또는 재생성)이면 반영됨.  
    `docker-compose up -d`(변경된 env로 재생성 필요 시 `docker-compose up -d --force-recreate`) 또는 `docker-compose restart <service>`.
- **docker-compose.yml에서 포트/볼륨 매핑 변경**  
    → 이미지 재빌드 불필요. 단, compose 변경은 컨테이너 재생성 필요.  
    `docker-compose up -d` 하거나 `docker-compose up -d --force-recreate` 하면 된다.
- **컨테이너 실행 옵션(포트, 볼륨, env) 변경**  
    → 재생성/재시작만으로 해결.
- **단순 설정값(로그 레벨 등)을 컨테이너 시작 커맨드로 주입**  
    → 재빌드 X, restart 또는 재생성.

---
아래는 참고사항?
## 도커 위에서 Spring / Vite / MySQL 개발할 때 실무 팁

1. **개발용은 ‘마운트 & 런’**
    - 백엔드: 소스(`src`)와 `target/classes`를 컨테이너에 바인드해서 `mvn spring-boot:run` 실행. 코드 바꾸면 자동 재시작(또는 devtools로 빠른 재시작). → 이미지 재빌드 불필요.
    - 프론트엔드(vite): `npm run dev`를 컨테이너나 호스트에서 실행하고 소스 마운트. Vite의 HMR(Hot Module Replacement)로 변경 즉시 반영. → 이미지 재빌드 불필요.
2. **프로덕션 이미지는 정적파일을 포함해서 빌드**
    - 프론트도 `npm run build` 해서 정적 자원을 이미지에 복사하면, 정적파일 변경시 이미지 재빌드 필요.
3. **MySQL은 데이터가 볼륨에 있으니 스키마 변경은 마이그레이션 필요**
    - DB 스키마 변경은 이미지 빌드와 별개로 마이그레이션(Run migration, Flyway 등) 필요. 재빌드는 필요없음.
4. **빠른 개발 워크플로(예)**
    - `docker-compose up --build` : 이미지가 바뀔 때(의존성 변경, Dockerfile 변경) 사용
    - `docker-compose up -d` : 이미지 재빌드 없이 컨테이너(설정) 재생성 / 시작
    - `docker-compose restart service` : 단순 재시작(설정 변경은 반영 안 될 수 있음)
    - `docker-compose up -d --force-recreate` : 설정(compose.yml, env 마운트 등) 변경 반영 위해 컨테이너 재생성

---
### **Backend(스프링)** → **Java 코드, 의존성, Dockerfile 변경 = 재빌드 필요**

### **frontend(Vue)** → **Vite dev 모드가 아니면, 코드 변경 시 매번 재빌드 필요**

### **mysql** → **코드(쿼리) 수정이 아니라면 재빌드 없음**


