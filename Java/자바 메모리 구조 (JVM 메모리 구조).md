```mathematica
┌───────────────────────────┐
│  Method Area (메서드 영역)  │ ← 클래스 정보, static, 상수 등
├───────────────────────────┤
│       Heap (힙 영역)       │ ← 인스턴스 (new로 생성된 객체)
├───────────────────────────┤
│     Stack (스택 영역)      │ ← 메서드 호출 정보, 지역 변수
├───────────────────────────┤
│  PC Register (PC 레지스터) │ ← 현재 실행 중인 명령 주소
├───────────────────────────┤
│    Native Method Stack    │ ← C/C++ native 메서드용
└───────────────────────────┘
```

정말 좋은 질문이에요!  
개발자라면 꼭 이해하고 있어야 하는 **자바 메모리 구조 (JVM 메모리 구조)**를 아주 **쉽고 확실하게 기억할 수 있게** 정리해드릴게요.

#  각 영역 상세 설명

## 1. 🧠 **메서드 영역 (Method Area)**

- **클래스의 구조적인 정보가 저장됨**
- 저장되는 것들
    - 클래스 이름, 메서드 이름
    - `static` 변수
    - 상수 (`final`)
- 클래스 로딩 시 한 번만 올라옴 (JVM 시작 후 메모리 공유됨)

## 2. 🧶 **힙 영역 (Heap)**

- **new로 생성한 객체(instance)**가 저장됨
- 모든 스레드가 공유하는 공간
- 예: `new Member()`, `List<String>` 같은 객체들
- GC(Garbage Collector)의 대상

## 3. 📋 **스택 영역 (Stack)**

- **각 스레드마다 개별적으로 할당**
- 메서드 호출 시마다 **스택 프레임**이 생성됨
    - 지역 변수
    - 매개 변수
    - 리턴 주소
- 메서드가 끝나면 스택 프레임은 자동 제거됨 (LIFO 구조)

## 4. ⚙️ **PC 레지스터**

- 각 스레드마다 하나씩 있음
- **현재 어떤 명령어(바이트코드)를 실행 중인지 기록**

> 보통 JVM 내부적으로 쓰이므로 우리가 직접 신경 쓸 일은 거의 없음

## 5. ⚙️ **Native Method Stack**

- 자바 외부의 **C/C++ 메서드(native code)** 실행 시 사용

> JNI(Java Native Interface) 사용할 때 사용됨

# 🎯 핵심 키워드로 암기하기

|구분|저장되는 것|특징|
|---|---|---|
|메서드 영역|static, 클래스 정보|한 번 로딩, 공유|
|힙 영역|new 객체|GC 대상, 공유됨|
|스택 영역|지역 변수, 매개변수|스레드 별 개별 관리|
|PC 레지스터|실행 중인 명령 주소|스레드마다 있음|
|네이티브 스택|C/C++ native 호출|특수 상황에서 사용|

---

# 🔁 예제로 전체 구조 정리

```java
public class Example {
    static int staticVar = 10; // 메서드 영역

    int instanceVar = 5;       // 힙 영역

    public void run() {
        int localVar = 3;      // 스택 영역
        Example ex = new Example(); // ex → 힙 영역에 객체 생성됨
    }
}
```

---

# ✅ 최종 정리 슬로건

```
📌 static은 메서드 영역
📌 new는 힙
📌 지역 변수는 스택
```




---
# 자바 공식 문서 기반: 상속 객체의 메모리 할당과 다운캐스팅 동작 설명

## 1. 상속 객체 생성 시 힙과 스택 메모리의 동작

## 힙(Heap) 메모리

- **객체 인스턴스는 JVM의 힙에 생성**됩니다. 자바 가상 머신 명세에 따르면, "The heap is the run-time data area from which memory for all class instances and arrays is allocated." 즉, 모든 클래스 인스턴스와 배열의 메모리는 힙에서 할당됩니다[1](https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html)
    
- **상속 객체 생성 시**(예: `Child c = new Child();`) 힙에는 가장 상위 부모 클래스(Object)부터 차례로 각 상위 클래스의 멤버 변수에 필요한 메모리가 한 구조체처럼 연속적으로 잡힙니다. 이 안에는 부모 클래스의 멤버 변수, 자식 클래스의 멤버 변수 모두 포함됩니다.
    
- **메서드 영역**에는 클래스별 코드(메서드 정보, static 등)가 올라가 있지만, 실제 인스턴스필드는 힙에만 저장됩니다.
    

## 스택(Stack) 메모리

- **참조 변수(레퍼런스)**는 스택에 저장됩니다. 예를 들어, `Child c = new Child();` 코드에서 변수 `c` 자체는 스택에, 객체 자체는 힙에 위치합니다[2](https://www.geeksforgeeks.org/java/java-memory-management/)[3](https://www.scaler.com/topics/java/heap-memory-and-stack-memory-in-java/).
    
- **메서드 호출 시** 해당 메서드의 지역 변수, 매개변수, 참조 변수 등이 스택 프레임에 할당되고, 힙의 객체를 가리키는 '주소값'이 저장됩니다.
    
- 객체의 실제 데이터(필드 값 등)는 스택이 아니라 힙에 저장된다는 점이 핵심입니다.
    

## 예시

`Parent p = new Child();`
- `p`라는 참조 변수(스택에 저장)가 힙에 생성된 'Child' 객체 전체(부모 필드 포함)를 가리킵니다. 이때, 힙에는 Parent와 Child의 모든 필드가 모두 존재합니다.
    
## 2. 다운캐스팅 시 형 변환 동작 (자바 공식 문서 기준)

## 다운캐스팅 기본 원칙

- **다운캐스팅이란**: 부모 타입의 레퍼런스가 실제로 자식 인스턴스를 가리키고 있을 때, 자식 타입으로 강제 변환하는 것[4](https://docs.oracle.com/javase/specs/jls/se11/html/jls-5.html).
    
- **구문**:
    `Parent p = new Child(); Child c = (Child) p;`
    
- **필수 점검**: 다운캐스팅은 반드시 명시적 형변환이 필요합니다. 컴파일러가 강제 형변환을 허용하더라도, 실제 객체가 해당 타입이 아니면 런타임에 `ClassCastException`이 발생합니다[4](https://docs.oracle.com/javase/specs/jls/se11/html/jls-5.html).
    

## 자바 공식 문서 설명

- 명세에 따르면 "Reference type casting may require an explicit cast to convert a value of superclass type to a subclass type."
    
- 다운캐스팅은 실행 시점에 동적으로 객체의 실제 타입을 체크합니다. 실제로 부모 타입이 아닌 객체를 잘못된 형변환으로 변환하는 경우 예외가 발생합니다[4](https://docs.oracle.com/javase/specs/jls/se11/html/jls-5.html).
    
- 타입 체크 보호를 위해, 보통 `instanceof` 연산자를 활용해 안전성을 검증합니다.
    

## 다운캐스팅 처리 순서

1. 컴파일러는 다운캐스팅 구문 자체를 허용(단, 부모-자식 관계가 충족되어야 함).
2. 런타임 시 JVM은 해당 객체가 지정한 타입의 인스턴스인지 검사(`instanceof`).
3. 맞다면 변환하여 자식 타입 참조가 가능.
4. 아니라면 `ClassCastException` 런타임 예외 발생.

## 공식 문서 예시

`Object obj = "string"; String str = (String) obj; // 다운캐스팅, 성공 Integer num = (Integer) obj; // 런타임에 ClassCastException 발생`

- 위 예시는 [자바 명세(JLS) 5장][4](https://docs.oracle.com/javase/specs/jls/se11/html/jls-5.html)에서 언급되는 타입 변환 동작을 보여줍니다.
    

## `instanceof` 활용

다운캐스팅 전 반드시 다음과 같이 검사하는 것이 안전합니다:

`if (obj instanceof String) {     String str = (String) obj; // 안전하게 다운캐스팅 }`

## 요약

- **상속 객체 생성** 시, 객체 그 자체는 힙 메모리에 모두 통합 저장되며, 참조 변수(레퍼런스)는 스택에 저장됩니다. 
    
- **다운캐스팅**은 반드시 명시적 형변환을 해야 하며, 실행 시 타입을 체크하여 실제 객체 타입이 일치할 때만 변환이 완료됩니다. 그렇지 않으면 런타임 예외가 발생합니다. 이는 모두 자바 공식 명세와 API 문서에서 규정된 동작 방식입니다[1](https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html)[4](https://docs.oracle.com/javase/specs/jls/se11/html/jls-5.html).

1. [https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html](https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html)
2. [https://www.geeksforgeeks.org/java/java-memory-management/](https://www.geeksforgeeks.org/java/java-memory-management/)
3. [https://www.scaler.com/topics/java/heap-memory-and-stack-memory-in-java/](https://www.scaler.com/topics/java/heap-memory-and-stack-memory-in-java/)
4. [https://docs.oracle.com/javase/specs/jls/se11/html/jls-5.html](https://docs.oracle.com/javase/specs/jls/se11/html/jls-5.html)
5. [https://devstep.tistory.com/79](https://devstep.tistory.com/79)
6. [https://stackoverflow.com/questions/75085035/memory-allocation-for-inherited-objects-in-java](https://stackoverflow.com/questions/75085035/memory-allocation-for-inherited-objects-in-java)
7. [https://devkingdom.tistory.com/226](https://devkingdom.tistory.com/226)
8. [https://www.geeksforgeeks.org/java/rules-of-downcasting-objects-in-java/](https://www.geeksforgeeks.org/java/rules-of-downcasting-objects-in-java/)
9. [https://truehong.tistory.com/54](https://truehong.tistory.com/54)
10. [https://www.tutorialspoint.com/downcasting-in-java](https://www.tutorialspoint.com/downcasting-in-java)
11. [https://www.protechtraining.com/bookshelf/java_fundamentals_tutorial/object_oriented](https://www.protechtraining.com/bookshelf/java_fundamentals_tutorial/object_oriented)
12. [https://www.tutorialspoint.com/rules-of-downcasting-objects-in-java](https://www.tutorialspoint.com/rules-of-downcasting-objects-in-java)
13. [https://yaboong.github.io/java/2018/05/26/java-memory-management/](https://yaboong.github.io/java/2018/05/26/java-memory-management/)
14. [https://dev.to/dhanush9952/upcasting-and-downcasting-in-java-an-overview-of-typecasting-3djl](https://dev.to/dhanush9952/upcasting-and-downcasting-in-java-an-overview-of-typecasting-3djl)
15. [https://intellipaat.com/blog/tutorial/java-tutorial/downcasting-in-java/](https://intellipaat.com/blog/tutorial/java-tutorial/downcasting-in-java/)
16. [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management)
17. [https://softwareengineering.stackexchange.com/questions/65281/stack-and-heap-memory-in-java](https://softwareengineering.stackexchange.com/questions/65281/stack-and-heap-memory-in-java)
18. [https://viera.tistory.com/3](https://viera.tistory.com/3)
19. [http://people.eecs.berkeley.edu/~jrs/4/lec/16.pdf](http://people.eecs.berkeley.edu/~jrs/4/lec/16.pdf)
20. [https://inpa.tistory.com/entry/JAVA-%E2%98%95-%EC%97%85%EC%BA%90%EC%8A%A4%ED%8C%85-%EB%8B%A4%EC%9A%B4%EC%BA%90%EC%8A%A4%ED%8C%85-%ED%95%9C%EB%B0%A9-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0](https://inpa.tistory.com/entry/JAVA-%E2%98%95-%EC%97%85%EC%BA%90%EC%8A%A4%ED%8C%85-%EB%8B%A4%EC%9A%B4%EC%BA%90%EC%8A%A4%ED%8C%85-%ED%95%9C%EB%B0%A9-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0)



---

