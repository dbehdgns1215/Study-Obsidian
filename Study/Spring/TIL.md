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

---

