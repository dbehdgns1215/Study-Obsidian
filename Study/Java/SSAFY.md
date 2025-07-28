
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



## 매개변수의 다형성
사실 println은..
```java
public void println(Object x) {
	String s = String.valueOf(x);
	synchronized (this) {
		print(s);
		newLine();
	}
}
```
- 여러 매개 변수를 받을 땐, `StringBuilder`가 개입함

**equals()**
- Object.equals()는, 값이 같은지 확인함
- == 은, 객체의 주소가 동일한지 확인함
```java
String a = new String("hello");
String b = new String("hello");

System.out.println(a == b);       // false (다른 객체)
System.out.println(a.equals(b));  // true (내용 같음)
```


# Day 5

## Interface
- 최고 수준의 추상화 단계: 일반 메서드는 모두 abstract 형태
	- JDK 8에서 default method와 static method 추가
- 형태
	- 클래스와 유사하게 interface 선언
	- 멤버 구성
		- 모든 멤버 변수는 public static final이며 생략 가능
		- 모든 메서드는 public abstract이며 생략 가능
- 클래스와 다른 점은 인터페이스는 다중 상속이 가능하다는 것

```java
interface Fightable{
	int fire();
}

interface Transformable {
	void changeShape(boolean isHeroMode);
}

public interface Heroable extends Fightable, Transformable {
	void upgrade();
}
```

# Day 6

## Generics
- 다양한 타입의 객체를 다루는 메서드, 컬렉션 클래스에서 컴파일시에 타입을 체크함
	- 미리 사용할 타입을 명시해서 형변환을 하지 않아도 되게 함

`public interface Interface_Name<T>()`
`public class Class_Name<T>{}`
- `<T>`: 형인자(Type Parameter)
	- 단순히 임의의 참조형 타입을 말하며 성격에 따라 선언 (T: reference Type, E: Element, K: Key, V: Value)
- 객체 생성
	- 변수 쪽과 생성 쪽의 타입은 반드시 같아야 함. (상속 관계 등 X)
	- `ClassName<Number> generic = new ClassName<Number>();`
	- `ClassName<Number> generic = new ClassName<>();` (자바 7 이후 생략 가능)
	- `ClassName rawType = new ClassName()` (컴파일 경고 발생)


**주의사항**
- raw type의 사용과 `@SuppresWarning`
	- 무분별한 사용은 금지
```java
@SuppressWarnings({"rawtypes", "unused"})
public void useRawType() {
GenericBox box = new GenericBox();
}
```

- 헷갈리는 사용법
```java
public void confusing() {
	GenericBox<Person> pbox = new GenericBox<>();
	pbox.setSome(new Person());
	pbox.setSome(new SpiderMan());
	// pbox = new GenericBox<SpiderMan>(); // 가능할까?
}
```
- pbox는 Person 타입을 담을 수 있다.
	- Person을 담는 박스와 SpiderMan을 담는 박스는 상속 관계가 없다.

- 타입 파라미터는 인스턴스 레벨에서 결정됨
	- 클래스 레벨의 static 멤버에서는 사용할 수 없음
	- `static I item; //Cannot make a static reference to the non-static type T`

- Generic은 컴파일 타입에 지정한 타입으로 존재 -> 런타임에는 타입 정보 소거(Type Erasure: 단순 Object로 관리)
	- Compiler가 이미 타입을 체크했기 때문에 runtime에는 자유롭게 사용
	- runtime에 동작하는 new, instanceof 키워드 사용 불가
```java
I i = new I(); // compile error: Cannot instantiate the type I

GenericBox<SpiderMan> obj new GenericBox<>(); // compile error: Type Object cannot be safely cast to GenericBox<String>

if (obj instanceof GenericBox gb) {
	System.out.println("맞지만 타입에 안전하지 않음");
	gb.setSome("Hello"); // 에러는 아니지만 타입에 안전하지 않음
}

if (obj instanceof GenericBox<?>) { // wild card 사용
	Sysyem.out.println("이것이 최선: 타입이 훼손될 일은 없다.");
}
```

- Generic 타입의 배열 생성 불가
	- `GenericBox<String> [] boxes1 = new GenericBox<>[3];`
	- 배열은 runtime에 객체의 저보를 유지하고 동일한 타입의 객체만 처리함
	- 만약 `GenericBox<T>[]`이 된다고 가정했을 때는 runtime에 GenericBox[]로 변경됨
		- T가 Integer였을 때 runtime에는 box에 뭐든지 들어가버림

- raw 타입 객체의 형변환 주의
	- 실제 메모리에는 모든 객체를 담을 수 있으므로 형이 보장되지 못함

```java
public void genericArray() {
	GenericBox<Person>[] boxes3 = (GenericBox<Person>[]) new GenericBox[3];
	boxes3[0] = new GenericBox<Person>();
	GenericBox<String> box = new GenericBox<>("Hello");
	
	boxes3[1] = (GenercBox) (box);
	System.out.println(boxes3[1].getSome());
}
```



**한정형 형인자(bounded type parameter)**
- 필요에 따라 구체적인 타입 제한 필요
	- 계산기 프로그램 구현 시 Number 이하의 타입(Byte, Short, Integer...)로만 제한
		- type parameter 선언 뒤 extends 와 함께 상위 타입 명시
```java
class NumberBox<T extends Number> {
	public void addSomes(T... ts) {
		double d = 0;
		for (T t : ts) {
			d += t.doubleValue();
		}
		System.out.println("총 합은: " + d);
	}
}
```
- 인터페이스로 제한할 경우에도 `implement` 대신 `extends` 사용
- 클래스와 함께 인터페이스 제약 조건을 이용하라 경우 &로 연결
`class TypeRestrict1<T extends Compiler & ClassA>{}`


**Generic Method**
- 파라미터와 리턴 타입으로 type parameter를 갖는 메서드
	- 메서드 리턴 타입 앞에 타입 파라미터 변수 선언
```java
public class TypeParameterMethodTest<T> { // 객체 생성시 T 결정, 전체 객체에게 영향 줌
}

public <P> P method(P p) { // 메서드 호출시 P 결정, 메서드 내에서만 영향 줌줌
	System.out.printf("클래스..."
	return p;
}

public static void main(String[] args) {
	TypeParameterMethodTest<String> tpmt = new TypeParameterMethodTest<>("Hello");
	tpmt.<Long>method(20L); // 타입이 Long
	tpmt.method<10>; // 타입이 Integer
	}
```


**와일드 카드(?) 자료형**
- 제네릭 타입 변수 선언시 실제 type parameter가 무엇인지 모르거나 신경쓰고 싶지 않을 경우
	- 비한정형 와일드카드 자료형
		- `Generic_type <?>`
	- 한정형 와일드카드 자료형
		- `Generic_type <? extends T>`
		- `Generic_type <? super T>`

- PECS
	- Producer Extens: 제네릭 타입이 데이터를 생산하여 외부로 공급하는 역할

```java
void useWildCardType2(GenericBox<? extends Person> boxEntendsPerson) {
}
```

	 - Consume Super: 제네릭 타입이 데이터를 소비하는 역할(제네릭 타입에 추가, 수정)
```java
void useWildCardType3(GenericBox<? super Person> boxSuperPerson) {
}
```

**Generic Type 객체를 할당 받을 떄 와일드 카드 사용**
- java.util.List.addAll
```java
public interface List<E> extends Collection<E> {
	boolean addAll(int index, Collection<? extends E> c);
}
```
![[Pasted image 20250728102508.png]]

- 만약 `List<Person>`에 다른 요소들을 추가하는데 Collection의 타입 파라미터가
- `E` 였다면?
	- `List<Person> 만 처리` - `List<SpiderMan>`을 추가할 수 없음
- `<?>` 였다면?
	- 모든 대상을 받겠다는 얘기
		- 안됨
- `<? super E>` 였다면?
	- Object를 받겠다는 얘기
		- 안됨

타입을 콕 집어버리면 하위에 있는 애들을 처리할 수 없음.

- java.util.Arrays.compare
```java
public static <T> int compare(T[] a, T[] b, Comparator<? super T> cmp) {}
```
![[Pasted image 20250728102520.png]]

- 만약 SpiderMan을 비교하는데 Comparator의 타입 파라미터가
	- `T` 였다면?
		- SpiderMan 만 처리 - `Comparator<SpiderMan>`이 없으므로 처리 불가
		- 여러 타입을 받으려면 와일드 카드가 필요함
	- `<?>` 였다면?
		- 모두의 기준으로 사용 가능 - 처리할 수 없음
	- `<? extends E>` 였다면?
		- `Comparator<Venom>`을 받겠다는 이야기 - 원하는 게 아님

## Enum
- 열거형 데이터 타입
	- 데이터가 몇가지 한정된 값(주로 상수들)만을 갖는 형태로 구성되는 경우
		- 요일, 월, 계절 등
	- java.langEnum을 내부적으로 상속 받은 형태의 특별한 클래스
		- class 대신 enum 키워드 사용

```java
enum Grade{
	SALES, PART_TIME_JOB, NORMAL
}
```
- Enum 타입에 선언된 내용은 enum 상수로 불림: 일반적인 상수 선언의 컨벤션을 따름

```java
Grade grade = Grade.SALES;
```

![[Pasted image 20250728103120.png]]

**Enum을  이용한 연산**
- 비교 연산에서 주로 사용
	- `==`, `equals`: 두 개의 enum 상수 값이 같은지 비교 (주로 `equals`)

**Enum의 주요 메서드**
- java.lang.Enum의 메서드
![[Pasted image 20250728103825.png]]

- 자체 멤버 추가
	- 일반 클래스처럼 Enum에도 멤버 변수, 메서드 추가 가능
	- 단, enum 상수 선언 끝에 ; 추가 필요

```java
enum Greeting {
	GOOD_MORNING("좋은 아침");
	GOOD_AFTERNOON("오후도 힘내");
	GOOD_EVENING("오늘도 수고했어");

	private String message;

	Greeting(String message) {
		this.message = message;
	}

	public String getMessage() {
		return message;
	}
}
```


**Annotation**
- 컴파일러, JVM, 프레임워크 등이 보는 주석으로 소스코드에 메타 데이터를 삽입하는 형태
	- 코드에 대한 정보 추가 -> 소스 코드의 구조 변경, 환경 설정 정보 추가 등의 작업 진행

- JDK의 기본 Annotation의 예
	- `@Deprecated`
		- 컴파일러에게 해당 메서드가 deprecated 되었다고 알려줌
	- `@Override`
		- 컴파일러에게 해당 메서드는 override했다고 알려줌
	- `@SuppressWarings`
		- 컴파일러에게 사소한  warning의 경우 신경쓰지 말라고 알려줌

- 선언
	- interface와 유사하게 @interface 사용
- 구성
	- `@Target`, `@Retention` 등 메타 Annotation
![[Pasted image 20250728104540.png]]

- Annotation 설정을 위한 Annotation
	- `@Document`: JavaDoc을 만들 때, Annotation이 문서에 표시되어야 함
	- `@Inherited`: Annotation이 하위 클래스에 상속됨
	- `@Repeatable`: 해당 Annotation이 반복해서 적용될 수 있는지 표시

- 메타 Annotation
	- `@Retention`: 어느 단계까지 Annotation 정보를 유지할 것인가?
		- `RetentionPolicy enum`의 항목 중 용도에 맞춰 하나 선택 가능
		- `RetentionPolicy`의 상수 값
![[Pasted image 20250728104836.png]]

- `@Target`: Annotation을 어디에서 사용할 수 있는가?
```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.ANNOTATION_TYPE)
public @interface Targer {
	ElementType[] valuse();
}
```
![[Pasted image 20250728105054.png]]

- 속성
	- 추상 메서드처럼 선언
		- 메서드 이름 = 속성명, 리턴 타입 = 속성의 타입
![[Pasted image 20250728105215.png]]
- 일반 속성처럼 '키 = 값' 으로 사용
	- 설정하는 속성이 valuse 하나인 경우, 속성 생략 가능
	- 배열 {}를 쓰는데, 길이가 1일 때는 {} 생략 가능
	- 속성은 default 값을 가질 수 있으며 이 경우 속성 설정 생략 가능
	- 속성이 value 하나일 경우에는 key 값인 value 생략 가능 (주로 빈번히 사용되는 속성)

```java
// 키 = 값 형태로 배열 할당
@SuppressWarnings(valus = {"unused", "rawtypes"})

// 배열이지만 값이 하나인 경우는 중괄호 생략 가능
@SuppressWarnings(value = "unused")

// 할당하려는 속성이 하나일 경우에는 key 값 생략 가능
@SuppressWarnings({"unused", "rawtypes"})
```

## Collection Framework
- java.util 패키지
	- 다수의 데이터를 쉽게 처리하는 방법 제공 -> DB 처럼 CRUD 기능 중요
- collection framework 핵심 interface

![[Pasted image 20250728141000.png]]

- List
	- 입력 순서가 있는 데이터의 집합.
	- 순서가 있으니까 데이터의 중복을 허락
		- ex) 일렬로 줄 서기
	- 대표적 구현체: ArrayList, LinkedList
- Set
	- 입력 순서를 유지하지 않는 데이터의 집합.
	- 순서가 없어서 같은 데이터 구별할 수 없음
	- 중복 허락 X
		- ex) 알파벳이 한 종류씩 들어있는 주머니
	- 대표적 구현체: HashSet, TreeSet
- Map
	- key와 value의 쌍으로 데이터를 관리하는 집합.
	- 순서는 없고 key의 중복은 불가.
	- value의 중복은 가능
		- ex) 속성 - 값, 지역번호 - 지역
	- 대표적 구현체: HashMap, TreeMap



## List
- 특징
	- 입력 순서가 있는 데이터의 집합
	- 입력 순서가 있으므로 데이터의 중복을 허락
	![[Pasted image 20250728141312.png]]
- 관련 클래스 관계도
![[Pasted image 20250728141328.png]]
- 과거 버전들은 Thread Safe 하고, 그 외의 것들은 Thread Safe 하지 않음.
