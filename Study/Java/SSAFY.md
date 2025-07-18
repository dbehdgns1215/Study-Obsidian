
```java
import java.io.BufferedReader;

// Constructors
Class BufferedReader(Reader in)
Class BufferedReader(Reader in, int size)

InputStream is = System.in;
Reader r = new InputStreamReader(is);
BufferedReader in = new BufferedReader(r);

System.out.print("이름 입력 : ");
String name = ;
System.out.print("입력한 이름은 : " + name);

```
