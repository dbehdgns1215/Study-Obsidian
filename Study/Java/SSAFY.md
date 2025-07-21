
# BufferedReader 사용법
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

# 정리
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


# IO

## 출력 형식 지정
![[Pasted image 20250721093600.png]]


## 형변환
![[Pasted image 20250721094746.png]]
- long -> float
	- 표현 범위의 크기 자체는 long(64bit), float(32bit)이나, 표현 범위는 float이 더 큼 (정밀도 손실은 존재)


# Wrapper Class
![[Pasted image 20250721095631.png]]

- 객체형은 기본형과 달리 추가적인 속성과 기능을 포함
	- `Integer.parseInt(String str)` -> String to int
	- `Integer.valueOf(int i)` -> int to Integer // autoboxing 가능
	- `Integer.intValue()` -> Integer to int // unboxing 가능

