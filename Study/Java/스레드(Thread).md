
# ✅ 1. 스레드(Thread)란?

## 📌 정의

> 스레드는 **프로세스 내에서 실제로 작업을 수행하는 실행 단위**.

## 📦 쉽게 비유해서 설명

|개념|비유|
|---|---|
|**프로세스**|하나의 프로그램 전체 (ex. 웹브라우저)|
|**스레드**|프로그램 안에서 동작하는 작업자들|

예:
- 크롬(프로세스)은 하나지만,  
    탭 여러 개를 띄우면 **여러 작업(스레드)**가 동시에 작동하는 것과 같음

## 🧵 자바에서의 스레드

자바에서는 스레드를 다음과 같이 만들 수 있어요:

```java
Thread thread = new Thread(() -> {
    System.out.println("Hello from thread!");
});
thread.start(); // 새 스레드 시작
```

- `main()`도 사실은 기본 스레드입니다.
- 여러 스레드를 만들면, **동시에 여러 작업을 수행**할 수 있습니다.

# ✅ 2. 스레드와 메모리 관계

### 📊 메모리 구조 vs 스레드 연결

```mathematica
   [공유 영역]            [스레드별 영역]
┌──────────────┐       ┌──────────────┐
│ Method Area  │◄─────▶│  Thread-1    │
│ (static 등)  │       │  Stack       │
├──────────────┤       └──────────────┘
│     Heap     │◄─────▶│  Thread-2    │
│  (객체 저장)  │       │  Stack       │
└──────────────┘       └──────────────┘
```

### 📌 간단 정리

|영역|어떤 스레드가 접근?|무엇을 저장?|
|---|---|---|
|**Method Area**|모든 스레드가 공유|static 변수, 클래스 정보|
|**Heap**|모든 스레드가 공유|new 객체|
|**Stack**|**스레드마다 따로 존재**|지역 변수, 매개변수|
|**PC Register**|스레드마다 존재|현재 실행 중인 명령어 위치|

---

### ✅ 예제 코드로 시각화

```java
public class Example {
    static int staticVar = 1; // Method Area

    public static void main(String[] args) {
        new Thread(() -> { // Thread-1
            int local1 = 10;       // Stack (Thread-1)
            String name1 = new String("A"); // Heap
        }).start();

        new Thread(() -> { // Thread-2
            int local2 = 20;       // Stack (Thread-2)
            String name2 = new String("B"); // Heap
        }).start();
    }
}
```

🔎 이 코드가 실행되면:

- `staticVar` → Method Area (공유)
- `"A"`, `"B"` → Heap (공유 영역)
- `local1`, `name1` → Stack of Thread-1 (개별)
- `local2`, `name2` → Stack of Thread-2 (개별)

---

## ✅ 핵심 정리 슬로건

```
📌 Heap은 스레드들이 같이 본다 (공유)
📌 Stack은 스레드별로 따로 쓴다 (개별)
📌 static은 메서드 영역에 있고 모든 스레드가 같이 쓴다
```

---

## 🔒 왜 이렇게 나눌까?

- **Stack을 분리**하는 이유 → 스레드마다 독립적으로 작업해야 하니까
- **Heap과 Method Area는 공유**하는 이유 → 객체와 static은 협업하면서 같이 써야 하니까
