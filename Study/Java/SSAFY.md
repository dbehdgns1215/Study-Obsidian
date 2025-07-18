
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
	BufferedReadre bf = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	int N = Integer.parseInt(bf.readLine());

	for (int i = 0; i < N; i++) {
		String s = bf.readLine(); // String으로 라인 입력 받기
		StringTokenizer st = new StringTokenizer(s); // 공백 기준으로 구분

		int a = Integer.parseInt(st.nextToken()); // NoSuchElementException 조심
		int b = Integer.parseInt(st.nextToken());

		bw.write(String.valueOf(a + b));
		bw.newLine();
	}
	bw.flush();
	bw.close();
}
```