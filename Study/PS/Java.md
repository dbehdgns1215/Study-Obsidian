![[Pasted image 20250720131250.png]]



## ArrayList
```java
// 구버전
ArrayList al = new ArrayList();
al.add("one");
al.add("two");
al.add("three");
for (int i = 0; i < al.size(); i++) {
	String value = al.get(i); // 컴파일 에러, get 반환 값이 String이 아니라 Object임.
	String value = (String)al.get(i); // 가능 
	System.out.println(al.get(i));
}

// 신버전 - Generic 사용
ArrayList<String> al = new ArrayList<String>();
al.add("one");
al.add("two");
al.add("three");
for (int i = 0; i < al.size(); i++) {
	String value = al.get(i); // 가능
	System.out.println(al.get(i));
}
```


## Set vs List
- Set: `HashSet<Integer> A = new HashSet<Integer>();`
	- 중복 허용하지 않음
- List: `ArrayList<Integer> A = new ArrayList<Integer>();`
	- 중복 허용함

