
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

**주요 메서드**
![[Pasted image 20250728141752.png]]
- List의 조회, 만약 찾지 못하면 `-1` 을 반환

**배열과 ArrayList**
- 배열의 장점
	- 가장 기본적인 형태의 자료 구조로 간단하며 사용 쉬움
	- 접근 속도가 빠름
- 배열의 단점
	- 크기를 변경할 수 없어, 추가 데이터를 위해 새로운 배열을 만들고 복사해야 함.
	- 비순차적 데이터의 추가, 삭제에 많은 시간이 걸림
![[Pasted image 20250728144132.png]]
- 배열을 사용하는 ArrayList도 태생적으로 배열의 장-단점을 그대로 가져감

**LinkedList**
- 배열의 단점 극복
- 각 요소를 Node로 정의하고 Node는 다음 요소의 참조 값과 데이터로 구성됨
	- 각 요소가 다음 요소의 링크 정보를 가지며 연속적으로 구성될 필요가 없다.
![[Pasted image 20250728144233.png]]
- 데이터 삭제 및 추가
![[Pasted image 20250728144243.png]]

**ArrayList vs LinkedList**
![[Pasted image 20250728144427.png]]

- 결론
	- 특정 클래스가 좋고 나쁨이 아니라, 용도에 적합하게 사용해야 함.
	- 소량의 데이터를 가지고 사용할 경우에는 큰 차이가 없음
	- 정적인 데이터 활용, 단순한 데이터 조회용 : ArrayList
	- 동적인 데이터 추가, 삭제가 많은 작업 :LinkedList

## Set Interface
- 특징
	- 입력 순서를 관리하지 않고 주머니에 구슬(데이터)을 넣는 형태
	- 데이터를 구별할 순서(idx)가 없어서 중복이 허용되지 않음
		- 효율적인 중복 데이터 제거 수단
![[Pasted image 20250728150625.png]]
- 관련 클래스 관계도
![[Pasted image 20250728150633.png]]

```java
// TODO: 동일한 번호의 SmartPhone이면 하나만 추가될 수 있도록 처리하시오.

@Override
public boolean equals(Object obj) {
	if (obj instanceof SmartPhone sphone) {
	return sphone.number.equals(this.number);
	}
	return false;
}

// 이 객체가 가질 수 있는 unique한 값을 만들어주는 메서드
@Override
public int hashCode() {
	return this.number.hashCode();
}
// END
```

```text
`HashSet`은 내부적으로 `HashMap`을 사용한다.

원소를 추가할 때 **1단계**로 `hashCode()`를 호출해 어느 버킷(bucket)에 저장할지 결정한다.  
그리고 같은 해시코드를 가진 객체가 이미 있다면, **2단계**로 `equals()`를 호출해 실제로 같은 객체인지 확인한다.

따라서 `hashCode()`와 `equals()`를 **둘 다 일관되게 오버라이딩**해야 한다.  
이렇게 해야만 `HashSet`이 값이 같은 객체를 **중복으로 저장하지 않고 하나만 유지**할 수 있다.

반대로 하나만 오버라이딩하거나 둘 다 기본 구현을 쓰면,  
객체는 주소값 기준으로만 비교되어 같은 값이라도 서로 다른 객체로 취급되어 중복 저장될 수 있다.
```


## Map Interface
- 특징
	- Key와 Value를 하나의 Entry로 묶어서 데이터 관리
		- key : Object 형태로 데이터 중복을 허락하지 않음
		- Value : Object 형태로 데이터 중복이 허락됨.
![[Pasted image 20250728152144.png]]
- 관련 클래스 관계도
![[Pasted image 20250728152154.png]]
- 일반적으로는 HashMap
- 정렬이 필요하면 TreeMap

**Map Interface의 주요 메서드**
![[Pasted image 20250728152240.png]]
- HashMap에서는 putifAbsent()가 있음.
	- 값이 없을 때만 추가하는 메서드



## 정렬
- 정렬 가능한 Collection
	- 배열, List 계열
	- Set에서는 SortedSet 계열
	- Map에서는 SortedMap 계열 (key 기준)

**Comparable**
```java
public interface Comparable<T> {
	public int compareTo(T o);
}
```

> 양수 : 자리 바꿈
> 음수 : 자리 유지
> 0 : 동일 위치


```java
@Override
public int compareTo(SmartPhone o) {
	return this.number.compareTo(o.number);
}
```

**Comparator**
- 객체가 Comparable을 구현하고 있지 않거나 사용자 정의 알고리즘으로 정렬하려는 경우
	- String을 알파벳 순이 아닌 글자 수로 정렬하려면?
- `sort(List<T> list, Comparator<? Super T> c)`

```java
public interface Comparator<T> {
	int compare(T o1, T o2);
}
```

> 양수 : 자리 바꿈
> 음수 : 자리 유지
> 0 : 동일 위치

- 1회성 객체 사용시 anonymous inner class 사용
	- 클래스 정의, 객체 생성을 한 번에 처리할 수 있음
```java
Collections.sort(names, new Comparator<String>() {
	@Override
	public int compare(String o1, String o2) {
		int len1 = o1.length();
		int len2 = o2.length();
		return Integer.compare(len1, len2) * -1;
	}
});
```








--- 

## 추상 Class 객체 생성법
1. 구현한 하위 class 참조
2. 자신의 객체를 Return하는 static method
3. 외부 Class를 이용
4. 자신의 생성자 이용 (익명 클래스)



# Day 7

## Lambda
- 타겟 타입과 @FunctionalInterface
	- 타겟 타입 또는 함수형 인터페이스
		- Lambda 식이 할당되는 인터페이스를 Lambda 식의 타겟 타입이라 함
		- 타겟 타입은 abstract 메서드가 반드시 하나만 존재해야 함. (default, static 등은 무관)
			- 이 메서드 구현부가 Lambda 식으로 대체됨
	- `FunctionallInterface`
		- 컴파일러가 재정의해야 하는 abstract method가 하나만 있음을 체크
			- 그렇지 않을 경우 오류 발생 -> 안정적인 programming을 위한 option
```java
@FunctionalInterface
public interface Comparator<T> {
	int compare(T o1, T o2);

	boolean equals(Object obj);

	default Comparator<T> reversed() {
		return Collections.reverseOrder(this);
	}
}
```
- abstract method가 2개 이상 존재하는 경우는 여전히 익명의 inner claass를 사용해줘야 함.

- 구현체 작성 방법
	- `(type variable_name[,...]) -> {실행문;};`
		- 선언된 변수들을 이용해서 실행문을 실행하면 됨
		- 매개변수 부분은 실행문 블록에서 사용하기 위한 값 제공 (일반적인 변수 선언)
			- `(String str) -> {System.out.println(str);`
		- 매개변수의 타입은 런타임시에 대입되는 값에 따라서 자동으로 인식되므로 생략함
			- (str) -> {System.out.println(str);}
		- 매개변수 및 실행문이 하나일 때는 변수 및 실행문의 괄호, ';' 생략 가능
			- str -> System.out.println(str)
		- 리턴이 필요할 경우 return 문장 사용
			- num -> {
				- System.out.prinln(num);
				- return num \* 2
			- }
		- 리턴문만 있는 경우 중괄호와 return 생략 가능
			- num -> num \* 2

```java
package com.ssafy.day08.a_lambda;

public class A_BasicLambda {
    // TODO: 다음의 interface가 함수형인지 확인해보세요.
    interface MyFunctional1 {
        void sayHello(String name);
    }
    // END

    @FunctionalInterface
    interface MyFunctional2 {
        double numTo(int num);
    }

    private static void useFunction1(MyFunctional1 function, String name) {
        function.sayHello(name);
    }

    private static void useFunction2(MyFunctional2 function, int num) {
        System.out.println(function.numTo(num));
    }

    public static void main(String[] args) {
        // TODO: useFunction1과 useFunction2를 lambda식을 이용해서 호출해보세요.
    	useFunction1(new MyFunctional1() {
			@Override
			public void sayHello(String name) {
				System.out.println("Hello " + name);
				}
			}, "hong");
    	
    	useFunction1((String name) -> {System.out.println("Hello " + name);}, "jang");
    	useFunction1(name -> {System.out.println("Hello " + name);}, "jang");
    	
    	useFunction2(new MyFunctional2() {

			@Override
			public double numTo(int num) {
				// TODO Auto-generated method stub
				return num * 100;
			}
    	}, 10);
    	
    	useFunction2((int num) -> {return num * 100;}, 10);
    	useFunction2(num -> num * 100, 10);
    	// END
    }
}
```



## 표준 함수형 Interface
**강의 다시보기로 이 부분만 다시 볼 필요 있을 듯**
- java.util.function package에 정의
	- 주로 메서드 또는 생성자의 parameter로 Lambda 식을 제공하기 위함임
![[Pasted image 20250729093159.png]]


**Consumer**
![[Pasted image 20250729093942.png]]

![[Pasted image 20250729093955.png]]

**Supplier**
![[Pasted image 20250729094015.png]]

**Function**
![[Pasted image 20250729094049.png]]

**Operator**
![[Pasted image 20250729094115.png]]

**Predicate**
![[Pasted image 20250729094132.png]]

**Optional\<T>**
- T 타입의 객체에 대한 Wrapper
- 객체가 있을 수도 있고 없을 수도 있는 (null) 상태를 나타내는 객체
	- NullPointerException에 대한 적극적 대처 가능
	- java.util.function은 아님 (java.util.package)
- 기존의 NullPointerException 처리 과정
```java
public void useString1(String str) {
	// 어떤 문제가 있을 수 있을까?
	System.out.println(str + " : " + str.length());
}
```
- str이 null일 수도 있음.
```java
public void useString1(String str) {
	if (str != null) {
		System.out.println(str + " : " + str.length());
	} else {
		System.out.println("str is null");
	}
}
```
- 옛날 방식은 이러했지만, 이제는 Optional\<T> 객체를 활용함

```java
public void useString2(Optional<String> str) {
	if (str.isPresent()) {
		System.out.println(str + " : " + str.length());
	} else {
		System.out.println("str is null");
	}
```
- 이게 요즘 방식

![[Pasted image 20250729094532.png]]



## 메서드 참조와 생성자 참조

**메서드 참조**
- 람다 실행문 내부에서 다른 함수 하나만을 실행하는 경우 :: 연산자를 이용해 기존 메서드를 참조함
	- <소유자>::<파라미터를 사용하는 소유자의 메서드>
- 파라미터의 인스턴스 메서드 참조
	- 객체::인스턴스 메서드
		- 첫 번째 파라미터는 메서드의 소유자, 나머지 파라미터는 메서드의 파라미터 순서대로 전달됨
- 정적 메서드 참조
	- 클래스::정적 메서드
		- 모든 파라미터가 메서드의 파라미터 순서대로 전달됨
![[Pasted image 20250729102233.png]]

**메서드 참조**
- 특정 객체의 instance의 메서드 참조
	- 객체::인스턴스 메서드 형태
		- 객체의 메서드가 호출되며 파라미터는 메서드에 그대로 전달됨
```java
List<String> names = new ArrayList<>();

names.forEach(item -> names.add(item));
names.forEach(names::add);

names.forEach(item -> sysout(item));
names.forEach(System.out::println);
```

## Stream API
- JDK 8에서 추가된 java.util.stream package
- 배열 및 Collection의 요소를 하나씩 참조해서 처리하는 목적
	- 람다와 내부 반복자를 이용해 컬렉션을 다루는 코드를 간결화

```java
public void streamStyle() {
	double avg = heroes.stream()
						.mapToInt(String::length)  // 글자 수로 변환
						.filter(len -> len > 3)    // 필터링
						.average()                 // 평균
						.getAsDouble();            // 결과
	System.out.println(avg);
}
```

**Stream API의 역할 및 특징**
- 컬렉션 배열 등 데이터 소스에 대한 공통된 접근 방식 제공
![[Pasted image 20250729103253.png]]

- 손쉬운 병렬 처리
```java
set        .stream().forEach(System.out::println); // 순차 처리 (:: 있음 주의)
set.parallelStream().forEach(System.out::println); // 병렬 처리 (:: 있음 주의)
```

**맵/리듀스 모델 지원**
- 맵: 데이터를 작은 단위(chunk)로 나누어(splitting) 지정된 함수를 적용(mappint) 처리
- 리듀스: 결과를 모아서 최종 결과를 생성

- 중간 처리들과 최종 처리를 조합해서 사용
	- 중간 처리: 매핑, 필터링, 정렬 등 가공 처리
	- 최종 처리: 반복, 카운팅, 평균, 총합 등의 집계 처리
![[Pasted image 20250729103605.png]]
- 각각의 중간 처리는 새로운 스트림을 리턴하여 builder 패턴 적용
	- 기존의 스트림의 내용을 수정하지는 않음
- 최종 처리는 최종적으로 원하는 값(void 포함)을 반환
	- 한 번 최종 처리가 끝난 스트림은 재사용 불가

**Stream의 종류와 획득**
- java.util.stream package에 정의
- 종류
	- Stream - 객체 요소에 대한 처리
	- IntStream, LongStream, DoubleStream - 각각 int, long, double 데이터 처리
![[Pasted image 20250729103825.png]]

- Stream의 획득
	- Collection, 배열, File, Random 및 Stream 클래스의 static 또는 default method로 생성
![[Pasted image 20250729103906.png]]


**단계별 주요 처리 메서드**
![[Pasted image 20250729104415.png]]
- 중간 처리는 최종 처리가 진행될 때까지 지연됨
```java
list.stream().mapToInt(data -> {
	System.out.println("문자열의 길이: " + data);
	return data.length();
});
```
- 최종 처리가 없으므로 중간 처리는 지연(LAZY) -> 출력 없음

```java
list.stream().mapToInt(data -> {
	System.out.println("문자열의 길이: " + data);
	return data.length();
}).sum();
```
- 최종 처리 시 중간 처리 일괄 진행 -> 출력 진행



**중간 처리**
![[Pasted image 20250729104815.png]]

**최종 처리**
![[Pasted image 20250729104918.png]]

**중간 처리: 정렬**
![[Pasted image 20250729105637.png]]

**중간 처리: 매핑(변환)**
![[Pasted image 20250729105656.png]]
![[Pasted image 20250729105712.png]]

**최종 처리: 매칭**
![[Pasted image 20250729105809.png]]


**최종 처리:  집계(aggregate) - 통계**
![[Pasted image 20250729105834.png]]

**최종 처리:  사용자 정의 집계 처리 - reduce()**
![[Pasted image 20250729105907.png]]

**최종 처리: 조사 - findFirst(), findAny()**
![[Pasted image 20250729110146.png]]

**최종 처리: 결과 모으기 - collect()**
![[Pasted image 20250729110211.png]]
- `<R, A> R collect(Collector<? super T, A, R> collector)` 얘를 주로 사용
![[Pasted image 20250729110254.png]]
- 위와 같은 static 메서드를 사용해서 collect를 사용하면 됨

![[Pasted image 20250730140642.png]]

![[Pasted image 20250730140807.png]]
- Checked Exception
	- 예외에 대한 대처 코드가 없으면 컴파일이 진행되지 않음
- Unchecked Exception (RuntimeException의 하위 클래스)
	- 예외에 대한 대처 코드가 없더라도 컴파일은 진행됨

![[Pasted image 20250730141419.png]]

## try ~ catch 구문
![[Pasted image 20250730141519.png]]
![[Pasted image 20250730141539.png]]

## Exception 객체의 정보 활용
- Throwable의 주요 메서드
	- `public String getMessage()`
		- 발생된 예외에 대한 구체적인 메시지를 반환한다.
	- `public Throwable getCause()`
		- 예외의 원인이 되는 Throwable 객체 또는 null을 반환한다.
	- `public void printStackTrace()`
		- 예외가 발생된 메서드가 호출되기까지의 메서드 호출 스택을 출력한다.
		- 디버깅의 수단으로 주로 사용.
			- 예외 처리시에 꼭 사용해주자.

```java
package com.ssafy.day09.a_basic;

public class SimpleException {
    public static void main(String[] args) {
        int[] intArray = { 10 };
        try {
        	System.out.println(intArray[2]);
        } catch (ArrayIndexOutOfBoundsException e) {
        	System.out.println("예외 처리: " + e.getMessage());
        	e.printStackTrace(); 
        }
        
        System.out.println("프로그램 종료합니다.");
    }
}
```


![[Pasted image 20250730142443.png]]

![[Pasted image 20250730142606.png]]

### Checked Exception 처리
- 처리하지 않으면 컴파일 불가 : Checked Exception
![[Pasted image 20250730142846.png]]
- 예외 발생 여부와 관계 없이, 혹시나 문제가 생기면 `너 대책 있어?` 를 체크하는 것.

## 다중 exception handling
- try 블록에서 여러 종류의 예외가 발생할 경우
	- 하나의 try 블록에 여러 개의 catch 블록 추가 가능
		- 예외 종류별로 catch 블록 구성
		- 처리될 catch 문장을 찾을 때는 다형성이 적용됨

![[Pasted image 20250730143221.png]]
- `CCException` 발생, 처리 가능한가?
	- 다형성에 의해 `Exception e`에 걸림

만약 순서가
```java
try {
} catch (Exception e) {

} catch (YYException e) {

} catch (XXException e) {

}
```
- 모든 예외가 `Exception`에 걸려버리기 때문에 YY... XX... 가 아무런 의미를 가지지 못함

![[Pasted image 20250730143520.png]]

### 다중 예외 처리를 이용한 Checked Exception 처리
- 발생하는 예외들을 하나로 처리하기
![[Pasted image 20250730143757.png]]
- 예외 상황별로 처리하는 것이 쉽지 않음
	- 가급적 예외 상황별로 처리하는 것을 권장함.

**심각하지 않은 예외를 굳이 세분화해서 처리하는 것도 낭비**
![[Pasted image 20250730143918.png]]

```java
package com.ssafy.day09.a_basic;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.sql.DriverManager;
import java.sql.SQLException;

public class MultiExceptionHandling {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        // TODO: 다음에서 발생하는 예외를 처리해보자.
         try {
             Class.forName("abc.Def"); // ClassNotFoundException
             new FileInputStream("Hello.java"); // FileNotFoundException
             DriverManager.getConnection("Hello"); // SQLException
         } catch (ClassNotFoundException | FileNotFoundException e){
        	 System.out.println("뭔가 시스템 리소스가 없다");
         } catch (SQLException e){
        	 System.out.println("SQL 예외");
         } 
        // END
        System.out.println("프로그램 정상 종료");

    }
}
```

![[Pasted image 20250730144057.png]]
- 이떄 출력되는 순서는, 자식 -> 부모 순으로 출력됨


## finally
- finally는 예외 발생 여부와 상관 없이 언제나 실행
	- 중간에 return을 만나는 경우도 finally 블록을 먼저 수행 후 리턴 실행

![[Pasted image 20250730144241.png]]


### try ~ catch ~ finally 구문을 이용한 예외 처리
![[Pasted image 20250730150307.png]]
- 생성한 시스템 자원을 반납하지 않으면 장래 resource leak 발생 가능 -> close 처리
	- 제대로 썼을 때, 실패했을 때 모두 close 처리를 해줘야 함.

![[Pasted image 20250730150457.png]]
- finally ... e.printStackTrace() 여기까지 지저분하게 finally 블록을 만들었어야 했음.
	- close 메서드 자체가 IOException 유발 가능.

**이를 해결하기 위해**
- try-with-resources
	- 리소스의 자동 close 처리
```java
try (리소스 타입 res1 = 초기화; 리소스_타입2 res2 = 초기화; ...) {
 // 예외 발생 코드
} catch (Exception e) {
 // exception handling code
}
```

![[Pasted image 20250730150935.png]]
- 확장된 try~with~resources 사용 시 주의점
	- try~with~resources 문장에 하나 이상의 catch 또는 finally가 필요
- Close 시점 주의!!
	- 자동 생성되는 코드들은 마법이 아니므로 실제로 어떻게 동작되고 있는지 정확히 알 필요가 있다.
	- try~with~resources 문장은 nested try 블록을 구성
	- ![[Pasted image 20250730151111.png]]

![[Pasted image 20250730150819.png]]
- try 선언문이 꼭 `AutoCloseable interface`를 구현해야 함!


**확장된 확장된 try~with~resources 사용 시 주의점**
![[Pasted image 20250730151135.png]]
- 두 번째 예시에서, con.commit(); 이후에 con이 close 되기 때문에 catch문 이하에서 rollback()이 동작하지 않음.
	- **해결법**
		![[Pasted image 20250730151444.png]]
- 따라서 첫 번째 예시처럼 try 문이 끝나면 종료시키려고 하는 경우에만 확장된 구문을 사용하는 것이 유용.


```java
    public void useStream() {
        FileInputStream fileInput = null;
        try {
            fileInput = new FileInputStream("abc.txt");
            fileInput.read();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fileInput != null) { // 이게 없으면 아래에서 NullPtrExcep 발생할 수도 있음.
                try {
                    fileInput.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public void useStreamNewStye() {
        // TODO: useStream을 try~with~resource 문장으로 변경하세요.
    	try (FileInputStream input = FileInputStream("abc.txt")) {
    		// input 사용
    	} catch(IOException e) {
    		e.printStackTrace();
    	}
        // END
    }
```


## throws 키워드를 통한 처리 위임
- method 에서 처리해야 할 하나 이상의 예외를 호출한 곳으로 전달함 (처리 위임)
	- catch하지 않는 이상 예외가 없어지지 않음. throws는 단순히 전달하는 것.
![[Pasted image 20250730151850.png]]
- 위 예에서, Exeption1, Exeption2의 처리 구조
![[Pasted image 20250730151957.png]]
- 나를 호출한 곳으로 예외를 던지고 해당 예외는 그곳에서 예외를 처리할 책임을 갖는다.

**checked exception과 throws**
![[Pasted image 20250730152031.png]]

```java
package com.ssafy.day09.c_throws;

public class ThrowsTest {
    // TODO: 1. methodCall2()에서 uncheckedExceptionMethod()를 호출할 때 발생하는 예외를 throws로 처리하세요.
    // TODO: 2. methodCall2()에서 checkedExceptionMethod()를 호출할 때 발생하는 예외를 throws로 처리하세요.
     public static void main(String[] args){
    	 try {
    		 methodCall1();
    	 } catch (ClassNotFoundException e){
    		 e.printStackTrace();
    	 }
       
        System.out.println("done");
    }

     private static void methodCall1() throws ClassNotFoundException {
        methodCall2();
    }

     private static void methodCall2() throws ClassNotFoundException {
//        uncheckedExceptionMethod();
         checkedExceptionMethod();
    }

     private static void checkedExceptionMethod() throws ClassNotFoundException {
        Class.forName("Hello");
    }

    private static void uncheckedExceptionMethod() {
        int i = 1 / 0;
    }
}

```


우선
```java
package com.ssafy.day09.c_throws;

public class ThrowsTest {
    // TODO: 1. methodCall2()에서 uncheckedExceptionMethod()를 호출할 때 발생하는 예외를 throws로 처리하세요.
    // TODO: 2. methodCall2()에서 checkedExceptionMethod()를 호출할 때 발생하는 예외를 throws로 처리하세요.
     public static void main(String[] args){
    	 try {
    		 methodCall1();
    	 } catch (ClassNotFoundException e){
    		 e.printStackTrace();
    	 }
       
        System.out.println("done");
    }

     private static void methodCall1() throws ClassNotFoundException {
        methodCall2();
    }

     private static void methodCall2() throws ClassNotFoundException {
        uncheckedExceptionMethod();
         checkedExceptionMethod();
    }

     private static void checkedExceptionMethod() throws ClassNotFoundException {
//        Class.forName("Hello");
    	 Class.forName("com.ssafy.day09.c_throws.ThrowsTest");
    }

    private static void uncheckedExceptionMethod() { 
        int i = 1 / 0; // runtime exception 발생 (ArithmeticException)
    }
}

```
- 이 경우, main 에서도 ArithmeticException을 던져버림 (JVM에게)
- JVM의 기본 예외 처리 로직 작동
- 단, done은 호출되지 않음.

```java
package com.ssafy.day09.c_throws;

public class ThrowsTest {
    // TODO: 1. methodCall2()에서 uncheckedExceptionMethod()를 호출할 때 발생하는 예외를 throws로 처리하세요.
    // TODO: 2. methodCall2()에서 checkedExceptionMethod()를 호출할 때 발생하는 예외를 throws로 처리하세요.
     public static void main(String[] args){
    	 try {
    		 methodCall1();
    	 } catch (ClassNotFoundException e){
    		 e.printStackTrace();
    	 } catch (ArithmeticException e) {
    		 e.printStackTrace();
    	 }
       
        System.out.println("done");
    }

     private static void methodCall1() throws ClassNotFoundException {
        methodCall2();
    }

     private static void methodCall2() throws ClassNotFoundException {
        uncheckedExceptionMethod();
         checkedExceptionMethod();
    }

     private static void checkedExceptionMethod() throws ClassNotFoundException {
//        Class.forName("Hello");
    	 Class.forName("com.ssafy.day09.c_throws.ThrowsTest");
    }

    private static void uncheckedExceptionMethod() { 
        int i = 1 / 0; // runtime exception 발생 (ArithmeticException)
    }
}

```
- 이렇게 main에서 잡아주면 정상적으로 done 까지 출력함.


## 로그 분석과 예외의 추적
![[Pasted image 20250730153019.png]]

**디버깅 순서/팁**
![[Pasted image 20250730153227.png]]

![[Pasted image 20250730153236.png]]

![[Pasted image 20250730153245.png]]

![[Pasted image 20250730153257.png]]

예외 종류가 뭐고.. 원인은 이거고 제일 아래부터 호출되기 시작해서 제일 위에서 예외를 최종적으로 잡아서 throws ... 계속 전파해서 위와 같은 로그가 생겨난 것.


### throws의 목적과 API 활용
![[Pasted image 20250730153423.png]]
- 왜 JVM에서 처리 안하고 개발자에게 throws를 던지는걸까?
	- API가 제공하는 메서드들은 사전에 예외가 발생할 수 있음을 선언부에 명시하고 프로그래머가 그 예외에 대처하도록 강요하기 때문.
![[Pasted image 20250730153743.png]]

### 메서드 재정의와 throws
- 메서드를 재정의 시에 조상 클래스 메서드가 전지는 예외보다 부모인 예외를 던질 수 없다.
	- 부모가 치지 않은 사고를 자식이 칠 수 없다!
![[Pasted image 20250730153902.png]]

![[Pasted image 20250730153954.png]]



![[Pasted image 20250730154052.png]]

![[Pasted image 20250730154117.png]]
![[Pasted image 20250730154127.png]]
- 배송은 주문 시스템으로 예외를 던져야 함.

![[Pasted image 20250730154203.png]]
![[Pasted image 20250730154209.png]]
- 결국 주문도 고객에게 예외를 던져줘야 함.
	- 하지만, 배송이 어떻게 되었든 상관없이 고객이 알고싶어 하는 것은
	- **주문**에 대한 예외임.

- 이를 해결하기 위해서
	- `throws new OrderException(d)`
	- 그럼 이제 고객은, 주문이 실패했다는 걸 인지할 수 있게 됨.
		- d가 의미하는 바는, `원인 예외`를 의미함.

**실제 예시**
![[Pasted image 20250730154522.png]]


### 사용자 정의 예외
- Exception 또는 RuntimeException 등을 Extends 받아서 내가 원하는 예외를 만들면 됨.
- API에 정의된 exception 이외에 필요에 따라 사용자 정의 예외 클래스 작성

![[Pasted image 20250730155004.png]]


![[Pasted image 20250730155258.png]]

에러
- 문법
- 논리
- System

예외(Exception) 처리(Handling)
- Checked Exception
	- Non Runtime Exception
		- Compile Error
		- 반드시 예외 처리를 해주어야 함. (try ~ catch)
- UnChecked Exception
	- Runtime Exception
		- `~OutOfBoundException`
		- `NullPointerException`
		- `NumberFormatException`
			- 즉, Runtime Exception은 예외 처리를 하지 않아도 됨.
			- 예외 처리가 아니라, 예외가 발생하지 않게끔 로직을 처리해야 함.


`throw` - 현재진행형
- 예외를 직접 발생 시킬 때.
	- `if (order == null) throw new ...Exception`
`throws` - 미래형
- 앞으로 던질 수도 있다.
	- 예를 들어, 이 메서드가 `...Exception`을 던질 수 있음을 시사하는 것.

### 예외 처리
- try ~ catch
- throws


# Day 8

## I/O와 Stream
- I/O? 데이터의 입력과 출력
- 데이터는 한 쪽에서 주고 한 쪽에서 받는 구조로 되어있음.
	- 이때 입력과 출력의 끝단을 **노드(Node)** 라고 함
	- 두 노드를 연결하고 데이터를 전송할 수 있는 개념 **스트림(Stream)**
	- 스트림은 단방향으로만 통신이 가능하며 하나의 스트림으로 입출력 동시에는 불가능
![[Pasted image 20250731090529.png]]

## Node Stream의 종류와 Naming
- 데이터 타입에 따라
	- byte
		- XXStream
	- char
		- XXer
- 방향에 따라
	- XXStream
		- 입력
			- InputStream
			- OutputStream
	- XXer
		- 출력
			- Reader
			- Writer
- 노드 타입에 따라
	- 키보드, 콘솔, File, ByteArray, Pipe...
- 최종 노드 스트림

![[Pasted image 20250731090822.png]]

### InputStream의 주요 메서드
![[Pasted image 20250731090916.png]]

### Reader의 주요 메서드
![[Pasted image 20250731091556.png]]


### OutputStream의 주요 메서드
![[Pasted image 20250731092208.png]]

## Writer의 주요 메서드
![[Pasted image 20250731092338.png]]


## 노드 스트림 활용
### File
- 가장 기본적인 입출력 장치 중 하나로 파일과 디렉터리를 다루는 클래스
![[Pasted image 20250731092452.png]]
- 파일 내용 수정과 관련된 건 `stream`과 연관이 있음.

![[Pasted image 20250731092549.png]]
- 절대경로
	- `C:/./././././abc.txt`
- 상대경로
	- 현재 디렉토리를 기준으로
	- `./abc.txt`


![[Pasted image 20250731093933.png]]

![[Pasted image 20250731094851.png]]

![[Pasted image 20250731095022.png]]

## 보조 스트림
- Filter Stream, Processing Stream
	- 다른 스트림에 부가적인 기능을 제공하는 스트림
![[Pasted image 20250731101017.png]]

- 스트림 체이닝 (Stream Chaining)
	- 필요에 따라 여러 보조 스트림을 연결해서 사용 가능
![[Pasted image 20250731101039.png]]

### 보조 스트림의 종류
![[Pasted image 20250731101206.png]]

#### 생성
- 이전 스트림을 생성자의 파라미터에 연결
![[Pasted image 20250731101226.png]]
- `BufferedReader br = new BufferedReader(new InputStreamReader(System.in));`
#### 종료
- 보조 스트림의 close()를 호출하면 노드 스트림의 close() 까지 호출됨

### 사용할 스트림의 결정 과정
![[Pasted image 20250731101533.png]]

![[Pasted image 20250731101608.png]]
![[Pasted image 20250731101736.png]]
![[Pasted image 20250731102023.png]]
![[Pasted image 20250731102134.png]]
- 다 외우진 않더라도 뭐가 뭔지는 알아야 할 듯


## 보조 스트림 활용
### InputStreamReader & OutputStreamWriter
- byte 기반 스트림을 cahr 기반으로 변경해주는 스트림
	- 문자열을 관리하기 위해서는 byte 단위보다 char 단위가 유리함
	- 키보드에서 입력(byte stream) 받은 데이터를 처리할 경우 등
- 변환시 Encoding 지정 가능
![[Pasted image 20250731102326.png]]

### Buffered 계열
- 버퍼의 역할
![[Pasted image 20250731102350.png]]

- 스트림의 입/출력 효율을 높이기 위해 버퍼를 사용하는 스트림
![[Pasted image 20250731102410.png]]
- BufferedReader: readLine() -> 줄 단위로 데이터를 읽어 들임
![[Pasted image 20250731102800.png]]


## 객체 직렬화(serialization)
- 객체를 파일 등에 저장하거나 네트워크로 전송하기 위해 연속적인 데이터로 변환하는 것
- 반대의 경우는 역직렬화(deserialization)
![[Pasted image 20250731103254.png]]
![[Pasted image 20250731103445.png]]

- 직렬화 되기 위한 조건
	- Serializable 인터페이스를 구현할 것
	- 클래스의 모든 멤버가 Serializable 인터페이스를 구현해야 함
	- 직렬화에서 제외허려는 멤버는 transient 선언
![[Pasted image 20250731103548.png]]

## 객체 직렬화
- seria Version UID
![[Pasted image 20250731103743.png]]
- 직렬화 할 때의 UID와 역직렬화 할 때의 PID가 다른 경우 예외 발생
- 직렬화되는 객체에 UID가 설정되지 않았을 경우 컴파일러가 자동 생성
	- 멤버 변경으로 인한 컴파일 시마다 변경 -> InvalidClassException 초래
- 직렬화되는 객체에 대해서 serialVersionUID 설정 권장

**직렬화에 쓰이는 보조 스트림 정리**
![[Pasted image 20250731104043.png]]



---

z## CSV / XML / JSON

![[Pasted image 20250731153303.png]]

### XML
- Markup Language
	- 태그 등을 이용하여 문서나 데이터의 구조를 명기하는 언어
	- HTML, SGML
- Extesible Markup Language
- HTML과 달리
	- 필요에 따라서 태그를 확장해서 사용 가능
	- 정확한 문법을 지켜야 동작: Well formed
		- 문서의 시작은 `<?xml version="1.0" encoding="UTF-8"?>`
		- 반드시 root element가 존재해야 한다.
			- 나머지 태그들은 Tree 형태로
		
		- 시작 태그와 종료 태그는 일치해야 한다.
		- 시작 태그는 key-value 구조의 속성을 가질 수 있다.
			- 속성 값은 " " 또는 ' '로 묶어서 표현한다.
		- 태그는 대소문자를 구별한다.


### Valid
![[Pasted image 20250731153415.png]]
![[Pasted image 20250731153514.png]]
- `phone?`: Optional 하다는 뜻.

## 파싱
- 문서에서 필요한 정보를 얻기 위해 태그를 구별하고 내용을 추출하는 과정
	- 전문적인 parser 활용

- SAX parser
	- Simple API for XML parser
	- 문서를 읽으면서 태그의 시작, 종료 등 이벤트 기반으로 처리하는 방식

- DOM parser
	- Document Object Model parser
	- 문서를 다 읽고 난 후 문서 구조 전체를 자료구조에 저장하여 탐색하는 방식

- SAX는 빠르고 한번에 처리하기 때문에 다양한 탐색이 어렵다.
- DOM은 다양한 탐색이 가능하지만 느리고 무거우며 큰 문서를 처리하기 어렵다.



### SAX parser
![[Pasted image 20250731153909.png]]


**SAX 실습 - DTO**
![[Pasted image 20250731154307.png]]


## DTO vs VO vs record
- 데이터를 보관하는데 사용되는 **불변 객체**를 간단하고 명료하게 정의 가능
- 불변의 DTO를 구현할 때 유용

- 주요 특징
	- 불변성: 객체의 상태는 객체 생성시 정의되며 이후는 변경할 수 없음 - 모든 field가 final
	- 간결성: 변수 선언 외에 필요한 코드는 컴파일 시점에 자동 생성
		- field에 대한 final 선언, blank final 초기화를 위한 생성자, getter, equals, hashCode, toString ...

- 제한 사항
	- 이미 묵시적으로 java.lang.Record를 상속받았기 때문에 추가로 다른 클래스를 상속받을 수 없음
	- 다른 클래스가 상속 받을 수도 없음

**예시**
![[Pasted image 20250731154750.png]]

![[Pasted image 20250731154758.png]]
- 이렇게 정의 가능.

### record 클래스
![[Pasted image 20250731154836.png]]

### Handler 작성성
![[Pasted image 20250731154911.png]]



## DOM Parser
![[Pasted image 20250731163452.png]]
![[Pasted image 20250731163521.png]]

## ✅ 정리

**SAX (Simple API for XML)**
- ✔ **이벤트 기반 파싱**
- XML을 **순차적으로 읽으면서** 시작/종료 태그, 텍스트 등 이벤트 발생 시 핸들러 호출
- 문서 전체를 메모리에 올리지 않음 → **메모리 효율적**
- 읽기 전용, 랜덤 접근 불가

**DOM (Document Object Model)**
- ✔ **메모리에 XML 전체를 트리 구조로 적재**
- 노드(태그) 간의 **관계(Tree) 기반으로 탐색 및 수정 가능**
- 자유로운 접근과 수정 가능
- 대규모 XML에서는 메모리 사용량이 큼

📌 따라서
- **SAX → 이벤트 기반**
- **DOM → 메모리에 올라간 트리 기반 관계**


---

## JSON
![[Pasted image 20250731165051.png]]

```JSON
{
	"boxOfficeResult": {
		"boxofficeType": "일별 박스 오피스",
		"showRange": "20120101~20120101",
		"dailyBoxOfficeList": [...],
		...
	}
}
```
- 자바로 표현해보면?
	- `Map<String, Map<String, Object>>`

```JSON
{
	"boxOfficeResult": {
		"boxofficeType": "일별 박스 오피스",
		"showRange": "20120101~20120101",
		"dailyBoxOfficeList": [
		{
			"rank": "1",
			"movieNm": "미션임파서블",
			"openDt": "2011-12-15",
			"audiAcc": "5328435"
		},
		{
			"rank": "2",
			...
		}
		
		],
		...
	}
}
```
- dailyBoxOfficeList를 다시 확장해보면?
	- `List<Map<String, Object>>`

결국
`Map<String, Map<String, List<Map<String, Object>>>>`
- 물론
	- **Object 꺼낼 때 (List<Map<String,Object>>)로 캐스팅해서 써야함**

![[Pasted image 20250731170805.png]]




