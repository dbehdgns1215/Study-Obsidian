
# D1
## 2056. 연월일 달력
```java
package codingtest;
import java.io.*;

class Solution
{
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

	    int[] maxDays = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	    
	    for(int test_case = 1; test_case <= T; test_case++)
		{
			String input = br.readLine();
            String result;
		
            int year = Integer.parseInt(input.substring(0, 4));
            int month = Integer.parseInt(input.substring(4, 6));
            int day = Integer.parseInt(input.substring(6, 8));
            
            if (month >= 1 && month <= 12) {
            	int maxDay = maxDays[month];
            	if (day >= 1 && day <= maxDay) {
            		result = String.format("%04d/%02d/%02d", year, month, day);
            	} else {
            		result = "-1";
            	}
            } else {
            	result = "-1";
            }
            
            System.out.println("#" + test_case + " " + result);
		}
	}
}
```
- 한줄 띄어쓰기 없는 라인 입력 받기 (12345)
	- substring 활용
- 출력 형식 포맷

## 2058. 자릿수 더하기
```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int sum = 0;
		
	    String line = br.readLine();
	    for (int j = 0; j < 4; j++) {
	    	sum += line.charAt(j) - '0';
	    }
		
		bw.write(sum + "");
		bw.flush();
	}
}
```
- 띄어쓰기 없는 입력에 대해서 각 자리수 매핑
- `line.charAt()` 의 반환 값은 `char` 이기 때문에, `Integer.parseInt()` 불가능.
	- `Integer.parseInt()`: String to Int
	- 따라서 `- '0'` 으로 형변환

## 2072. 홀수만 더하기
```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt((br.readLine()));
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			String[] numbers = br.readLine().split(" ");
			int sum = 0;
			
			for (String number : numbers) {
                int num = Integer.parseInt(number);
                if (num % 2 == 1) {
                    sum += num;
                }
            }
			
			bw.write("#" + test_case + " " + sum + "\n");
			bw.flush();
		}
	}
}
```
- 한 칸씩 띄어진 정수 입력 받기 (1 2 3 4 5)

## 2070 큰 놈, 작은 놈, 같은 놈
```java


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			
			if (A > B) {
				bw.write("#" + test_case + " " + ">\n");
			} else if(A < B) {
				bw.write("#" + test_case + " " + "<\n");
			} else {
				bw.write("#" + test_case + " " + "=\n");
			}
			
			bw.flush();
		}
	}
}
```

## 2068. 최대수 구하기
```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			String[] nums = br.readLine().split(" ");
			List<Integer> li = new ArrayList<Integer>();
			
			for (int i = 0; i < 10; i++) {
				li.add(Integer.parseInt(nums[i]));
			}
			
			Collections.sort(li);
			
			bw.write("#" + test_case + " " + li.get(9) + "\n");
			bw.flush();
		}
	}
}
```
- 띄어쓰기로 구분된 숫자들 입력 받아서 나누기
- List에 넣고 Collections sort 활용


## 2063. 중간값 찾기
```java
package codingtest;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		
		int target = T / 2;
		
		String[] input = br.readLine().split(" ");
		List<Integer> numbers = new ArrayList<>();
		
		for (int i = 0; i < T; i++) {
			numbers.add(Integer.parseInt(input[i]));
		}
		
		Collections.sort(numbers);
		
		int result = numbers.get(target);
		bw.write(result + "");
		bw.flush();
	}
}
```
- 한 칸씩 띄어진 정수 입력 받기 (1 2 3 4 5)
- Collections sort 활용
- ArrrayList 활용

## 2050. 알파벳을 숫자로 변환
```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String line = br.readLine();
		
		for (int i = 0; i < line.length(); i++) {
			if (line.charAt(i) >= 'A' && line.charAt(i) <= 'Z') {
				int ans = line.charAt(i) - 'A' + 1;
				bw.write(ans + " ");
			} else if (line.charAt(i) >= 'a' && line.charAt(i) <= 'a') {
				int ans = line.charAt(i) - 'a' + 1;
				bw.write(ans + " ");
			}
		}
		
		bw.flush();
	}
}
```
- 띄어쓰기 없는 입력들을 나누어서 출력
- 영어 대소문자에 따라서 다른 로직 적용
	- 대소문자 구분 안해도 통과하기는 함.

## 2019. 더블더블
```java

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int idx = Integer.parseInt(br.readLine());
		int base = 1;
		
		bw.write(base + " ");
		
		for (int i = 0; i < idx; i++) {
			base *= 2;
			bw.write(base + " ");
		}
		
		bw.flush();
	}
}
```


## 1945. 간단한 소인수분해
```java


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= T; test_case++) {
			
			int target = Integer.parseInt(br.readLine());
			
			int two = 0;
			int three = 0;
			int five = 0;
			int seven = 0;
			int eleven = 0;
			
			while (target != 1) {
				if (target % 2 == 0) {
					target /= 2;
					two++;
				} else if (target % 3 == 0) {
					target /= 3;
					three++;
				} else if (target % 5 == 0) {
					target /= 5;
					five++;
				} else if (target % 7 == 0) {
					target /= 7;
					seven++;
				} else if (target % 11 == 0) {
					target /= 11;
					eleven++;
				}
			}
			
			bw.write("#" + test_case + " " + two + " " + three + " " + five + " " + seven + " " + eleven + " \n");
			bw.flush();
		}
	}
}
```
- 소인수분해 활용
- 시간복잡도가 엄청 널널했음


## 1288. 새로운 불면증 치료법
