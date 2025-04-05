## 🍕 시나리오: 피자 주문 서비스

우리는 `PizzaOrderService`를 만들고 있어.  
주문이 완료되면 고객에게 **문자 알림**을 보내야 해.

---

### 🚫 주입 없이 직접 객체 만들기 (테스트 어려움)

```java
// 실제로 메시지를 보내는 클래스
class MessageSender {
    public void send(String message) {
        System.out.println("문자 보냄: " + message);
        // 여기서 실제 통신 모듈과 연결된다고 가정
    }
}

// 피자 주문 서비스
class PizzaOrderService {
    private MessageSender sender = new MessageSender(); // 💥 직접 new 함

    public void orderPizza(String name) {
        // 피자 주문 처리 로직...
        sender.send(name + "님의 피자가 주문되었습니다!");
    }
}
```

---

### 😓 문제: 테스트하려면?

```java
PizzaOrderService service = new PizzaOrderService();
service.orderPizza("철수");

// ❌ 실제 메시지를 보내버림 (문자 비용 들 수도 있음)
// ❌ 테스트에서 메시지를 제대로 보냈는지 검증도 불가능
```

---

## ✅ 의존성 주입 사용 (테스트 쉬움)

---

### 1️⃣ 인터페이스로 추상화

```java
interface MessageSender {
    void send(String message);
}
```

---

### 2️⃣ 실제 구현 (운영용)

```java
class RealMessageSender implements MessageSender {
    public void send(String message) {
        System.out.println("📱 실제 문자 발송: " + message);
    }
}
```

---

### 3️⃣ 서비스에 주입받도록 변경

```java
class PizzaOrderService {
    private MessageSender sender;

    // 💡 생성자를 통해 외부에서 주입받음
    public PizzaOrderService(MessageSender sender) {
        this.sender = sender;
    }

    public void orderPizza(String name) {
        // 피자 주문 처리
        sender.send(name + "님의 피자가 주문되었습니다!");
    }
}
```

---

### 4️⃣ 테스트용 가짜 구현 (Fake)

```java
class FakeMessageSender implements MessageSender {
    public String lastMessage = "";

    public void send(String message) {
        lastMessage = message; // 메시지를 기억만 함 (보내지는 않음)
    }
}
```

---

### ✅ 테스트 코드에서 가짜 주입

```java
@Test
void 피자주문_시_문자보내기_검증() {
    FakeMessageSender fakeSender = new FakeMessageSender(); // 가짜
    PizzaOrderService service = new PizzaOrderService(fakeSender); // 가짜 주입

    service.orderPizza("영희");

    assertEquals("영희님의 피자가 주문되었습니다!", fakeSender.lastMessage);
    // 💥 진짜 문자 안 보내고도, 보낼 내용을 검증할 수 있다!
}
```

---

## 🎯 핵심 요점

|구분|DI 없이|DI 있음|
|---|---|---|
|메시지 전송|진짜 전송됨|가짜로 대체 가능|
|테스트 비용|실제 문자, 느림, 비용 들 수 있음|빠르고 안전하게 테스트 가능|
|유연성|하나의 구현만 사용 가능|다양한 구현 (실제, 가짜, 로그 등) 사용 가능|

---

## 🚀 요약 한 줄

> 의존성 주입(DI)을 하면, 진짜 대신 가짜(Fake)를 쉽게 끼워넣을 수 있어서  
> **테스트가 안전하고, 빠르고, 검증 가능해진다.**

---
