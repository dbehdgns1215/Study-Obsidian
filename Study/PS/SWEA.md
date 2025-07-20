
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