
# Day 1
## BufferedReader 사용법
```java
import java.io.BufferedReader;

// Constructors
Class BufferedReader(Reader in)
Class BufferedReader(Reader in, int size)

// Basic
InputStream is = System.in;
Reader r = new InputStreamReader(is);
BufferedReader in = new BufferedReader(r);

// Enhanced
BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

System.out.print("이름 입력 : ");
String name = in.readLine(); // main에 throws ... 추가
System.out.print("입력한 이름은 : " + name);

System.out.print("나이 입력 : ");
int age1 = Integer.parseInt(in.readLine());
int age2 = Integer.parseInt(in.readLine());

System.out.print("5년 후 나이는 : " + (age1 + 5)); // 255 (String이 append 됨)
System.out.print("5년 후 나이는 : " + (age2 + 5)); // 30 (연산이 이루어짐)
```

## 정리
```java
public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	int N = Integer.parseInt(br.readLine());

	for (int i = 0; i < N; i++) {
		String s = br.readLine(); // String으로 라인 입력 받기
		StringTokenizer st = new StringTokenizer(s); // 공백 기준으로 구분

		// st.hasMoreTokens() // 토큰 있으면 True, 없으면 False

		int a = Integer.parseInt(st.nextToken()); // NoSuchElementException 조심
		int b = Integer.parseInt(st.nextToken());

		bw.write(String.valueOf(a + b));
		bw.newLine();
	}
	bw.flush();
	bw.close(); // 코테에서는 굳이?
}
```


## IO

## 출력 형식 지정
![[Pasted image 20250721093600.png]]


## 형변환
![[Pasted image 20250721094746.png]]
- long -> float
	- 표현 범위의 크기 자체는 long(64bit), float(32bit)이나, 표현 범위는 float이 더 큼 (정밀도 손실은 존재)


## Wrapper Class
![[Pasted image 20250721095631.png]]

- 객체형은 기본형과 달리 추가적인 속성과 기능을 포함
	- `Integer.parseInt(String str)` -> String to int
	- `Integer.valueOf(int i)` -> int to Integer // autoboxing 가능
	- `Integer.intValue()` -> Integer to int // unboxing 가능

![[Pasted image 20250721100037.png]]


## 배열
![[Pasted image 20250721103539.png]]

## String to char, String to int
```java

```
![[Pasted image 20250721104401.png]]

![[Pasted image 20250721104417.png]]

![[Pasted image 20250721105524.png]]


## 배열 복사
```java
System.arrayCopy(Object src, int srcPos, Object dest, int destPos)
Arrays.copyOf(int[] original, int newLength)
```


## 배열 선언

|선언 방식|허용 여부|이유|
|---|---|---|
|`int[] arr = new int[];`|❌ 불가능|배열 **크기를 반드시 지정**해야 함 (초기화 없이 크기 생략 불가)|
|`int[][] arr = new int[3][];`|✅ 가능|**바깥 배열(행) 크기만 지정**가능, 각 행(내부 배열)은 추후 할당|
- 두 번째 방식이 가능한 이유
	- 바깥 배열만 생성된거고 내부 배열은 아직 생성되지 않았기 때문.


# Day 2
![[Pasted image 20250722091255.png]]
- 만약 장미꽃이 아니라면?
	- 다형성의 좋은 예

![[Pasted image 20250722091350.png]]
- 주체지향적이 아닌 객체지향적인 경우
	- 장미꽃이 아니더라도 꽃 교환 가능
	- 꽃집도 교체 가능
- 꽃집, 꽃을 변경하더라도 꽃을 배달한다는 전체적인 꽃을 배달하는 프로세스는 변하지 않음

**객체지향 프로그래밍의 장점**
![[Pasted image 20250722091641.png]]

**클래스, 객체, 인스턴스**
![[Pasted image 20250722091949.png]]
- 인스턴스:
	- 사실 붕어빵 틀에 의해 만들어진 붕어빵은 여러 모양이 존재할 수 있음.
	- 이 붕어빵(객체)은 A라는 붕어빵 틀(클래스)에서 만들어낸 것 같아. 그러므로 이 붕어빵은 A의 `인스턴스`야.


**추상화**
![[Pasted image 20250722092754.png]]
- 구체화
`Person`
```java
Person P = new Person();

p.name = "철수";
p.age = 20;
p.isHungry = false;

p.eat();
p.work();
```

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
- static 변수의 `값`은 Heap 영역에 저장됨

**JVM 메모리 구조**
![[Pasted image 20250722094459.png]]



**static 변수**
![[Pasted image 20250722101239.png]]
- 지역 변수, 파라미터 매개 변수 -> Stack의 메서드 프레임 내부
	- 소멸 시점 -> { } 을 벗어날 때

## Variable arguments
![[Pasted image 20250722103616.png]]
```java
main
VariableTest vt = new VariableTest();
vt.addAll(1, 2, 3);

public void addAll (int... params) {
	int sum = 0;
	for (int i : params) {
		sum += i;
	}
}
```

## class 멤버와 instance 멤버간의 참조와 호출
![[Pasted image 20250722103928.png]]


## 기본형 변수와 참조형 변수
![[Pasted image 20250722105113.png]]
- Java에서는 `Call By Value`만 지원함.
	- `Call By Reference`에 대해서는 생각할 필요가 없음.
- 기본형이면 `값`을, 참조형이면 `참조값(메모리 주소의 복사값)`을 넘겨주는 것.

## 메서드 오버로딩
![[Pasted image 20250722110157.png]]
- 리턴 타입이 다른 경우 -> 리턴 타입만 다른 경우
- 메서드 오버로딩은, 같은 메서드 이름 + 매개변수 (타입, 개수, 순서) 중 하나 이상이 다르면 가능


## 생성자
아무런 역할이 없더라도, 메모리에 올려주는 역할을 한다는 게 포인트



`A a = new A();`
1. `A a`
	1. A라는 타입을 만나는 순간 JVM 클래스 로더가 a(클래스 변수)를 초기화시킴 (모호함)
	2. 스택 메모리에 참조 변수 a 공간 확보
2. `new A()`
	1. Heap 메모리 영역에 A 객체가 할당됨.
	2. 인스턴스 변수, 인스턴스 메서드는 객체가 만들어지는 순간에 할당
	3. `A()`가 생성자
3. 대입
	1.  a에 이전에 할당된 객체의 주소를 대입해줌

## 초기화 블록

자바에서 **초기화 블록(initialization block)이란,  
클래스 필드(변수)의 초기화 작업을 담당하는 블록**으로,  
생성자보다 먼저 실행되는 특별한 코드 영역을 말합니다.  
주로 **복잡한 초기화나 생성자 코드의 중복 제거**에 사용됩니다

## 종류

1. **인스턴스 초기화 블록**
    - `{ ... }` 형태
    - **객체가 생성될 때마다 실행**
    - 모든 생성자보다 항상 먼저 실행됨
    - 같은 클래스의 여러 생성자에 중복되는 초기화 코드가 있을 때, 공통 부분을 이 블록에 작성하면 코드 중복을 줄일 수 있음
        
2. **클래스(static) 초기화 블록**
    - `static { ... }` 형태
    - **클래스가 처음 메모리에 로딩될 때 단 한 번만 실행**
    - 주로 static 변수의 복잡한 초기화가 필요할 때 사용

## 초기화 순서(대표 예시)

- **클래스 변수(static 변수)**
    1. 기본값
    2. 명시적 초기값
    3. static 초기화 블록
       
- **인스턴스 변수**
    1. 기본값
    2. 명시적 초기값
    3. 인스턴스 초기화 블록
    4. 생성자

```java
class Example {
    static int a;
    int b;

    static { // 클래스 초기화 블록
        a = 10;
    }

    { // 인스턴스 초기화 블록
        b = 20;
    }

    public Example() { // 생성자
        b = 30;
    }
}
```


> 비교 연산자 '\=='
- 기본형의 경우 `값` 비교
- 참조형의 경우 `주소값` 비교

# Day 3

## Inheritance

>참고
>인터페이스, 구현체, 업캐스팅과는 다르게 상속의 관계에서 생각해볼만한 내용
	`Stack<Integer> st = new Stack<>(); st.push(1); st.push(2); System.out.println(st.pop());  // 2`
  **주의할 점**
	 만약 `List`나 `Vector` 타입으로 선언하면, **`push()`, `pop()`, `peek()` 같은 Stack 고유 메서드는 호출할 수 없습니다**.
	이 메서드들은 `Stack` 클래스에만 정의되어 있기 때문이에요.



## Sealed Class
- JDK 15에 추가된 키워드, 자바 17에서 정식 지원
- 봉인된 클래스로 내가 관리하는 특정 클래스에게만 상속 가능
	- 상속 계층 내에서 엄격한 제어를 통해
		- 프로그램의 구조를 명확하게 유지하고 의도치 않은  상속으로 인한 복잡성과 혼란 방지
		- 명확한 역할과 직무 분류 중요한 개념에서 주로 사용
- 작성법
	- class (interface 포함)에 sealed 키워드를 사용하고 상속(구현)을 허락하는 클래스를 permits 뒤에 나열해줌.
		- sealed가 선언된 클래스는 permits가 반드시 필요
	- 구현 클래스는 다음 키워드 중 하나 사용 필요
		- sealed: 여전히 봉인된 클래스로 추가적으로 permits로 하위 클래스 나열 필요
		- final: 더 이상 상속 받을 수 없는 클래스
		- non-sealed: 봉인이 해제된 클래스로 자유롭게 상속 가능
![[Pasted image 20250723093603.png]]

![[Pasted image 20250723095117.png]]

## Package
- 일반적인 package naming 룰
	- 소속, 프로젝트, 용도
	- com.ssafy.hrm.common
	- 주로 소속은 도메인 주소를 뒤집어서 사용


## Blank final
- 값이 할당되지 않은 멤버 변수
	- final 멤버 변수에 초기 값이 할당되어 버리면 모든 객체는 같은 값을 사용해야 함.
	- 객체가 생성되면 값을 변경할 기회가 없기 때문에 반드시 생성자에서 1회 초기화 가능 


### Quiz
```java
package com.ssafy.day03.c_modifier.last;  
  
public class LoadingSequenceTest {  
  
	private static LoadingSequenceTest lst = new LoadingSequenceTest();  
	// TODO: array의 length가 10이 될 수 있도록 코드를 개선해보자.  
	private static int SIZE = 10;  
	  
	// END  
	private int[] array;  
	  
	public static LoadingSequenceTest getInstance() {  
		return lst;  
	}  
	  
	private LoadingSequenceTest() {  
		// 멤버 변수의 초기화  
		array = new int[SIZE];  
	}  
  
	public static void main(String[] args) {  
		LoadingSequenceTest lst = LoadingSequenceTest.getInstance();  
		System.out.println(lst.array.length);  
	}  
}
```
- 1번 해결법
	- `private static LoadingSequenceTest lst = new LoadingSequenceTest(); `
	- 해당 코드를 `int SIZE` 보다 아래로 옮긴다
- 이유
	- 자바에서 클래스가 로드될 때, **static** (정적) 멤버들은 작성된 순서대로, 순차적으로 초기화 된다.
	- 따라서, `private static LoadingSequenceTest`를 제일 먼저 초기화 하는 시점에서는 `static int SIZE` 가 0인 상태로 존재하기 때문.
- 2번 해결법
	- `private final static int SIZE = 10;`
- 이유
	- `final static` 상수는 컴파일 시점에 상수로 처리되어 순서에 상관 없음.


# Day 4

캡슐화를 이루어내는 방식
- 변수는 private
- getter/setter
	- 그런데, getter 가 있는 데도 완전한 캡슐화라고 할 수 있는가?
		- 무분별한 getter 지양
		- private final 멤버 변수를 setter로 단 한번 할당해주고 getter로 접근
		- getter에서 값이 아닌 객체를 반환해주는 방식
		- 마치 불변 객체를 이용하는 것처럼 구성하면 캡슐화 장점이 극대화 될 듯'
			- 아니면 setter 대신, 생성자를 이용해서 생성하는 것도 좋은 방식임.
				- setter 자체가 값을 할당하는 메서드니까, 외부 접근이 일어날 수도?




