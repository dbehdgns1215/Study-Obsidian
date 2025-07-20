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
	- 순서 보장하지 않음
- List: `ArrayList<Integer> A = new ArrayList<Integer>();`
	- 중복 허용함
	- 순서 보장함


## Collection Interface
```java
// Accessors + Collectors
boolean isEmpty()
boolean add / remove (Object o)
boolean addAll / removeAll (Collection c)

// Object
boolean equals (Object o)
int hashCode ()

// Other Public Methods
void clear ()
boolean contains (Object o)
boolean containsAll (Collection c)
Iterator iterator ()
boolean retainAll (Collection c)
int size ()
Object[] toArray ()
Object[] toArray (Object a[])
```

## Set Interface \<extends Collection>
```
Collection과 기능적으로 똑같은 API를 제공함.
```

## List Interface \<extends Collection>
```java
// Accessors
boolean get / set (int idx)
Object set (int idx, Object element)

// Collectors
void add (int idx, Object element)
boolean addAll (int idx, Collection c)
Object remove (int idx)

// Other Public Methods
int indexOf (Object o)
int lastIndexOf (Object o)
List Iterator iterator ()
List Iterator iterator (int idx)
List subList (int fromIdx, int toIdx)
```


## Iterator
```java
public class Iterator
	public static void main(String[] args) {
		HashSet<Integer> A = new HashSet<Integer>();
		A.add(1);
		A.add(2);
		A.add(3);

		Iterator hi = A.iterator();
		while(hi.hasNext()) {
			System.out.println(hi.next());
		}
	}
```
- `hasNext()`
- `next()`

## Map
![[Pasted image 20250720172627.png]]
`{key:value}`

```java
import java.util.Collection;

public class MapDemo {

	public static void main(String[] args) {
	HashMap<String, Integer> a = new HashMap<String, Integer>();
	a.put("one", 1);
	a.put("two", 2);
	a.put("three", 3);
	System.out.println(a.get("one"));
	System.out.println(a.get("two"));
	System.out.println(a.get("three"));
	
	iteratorUsingForEach(a);
	iteratorUsingIterator(a);
	}

	static void iteratorUsingForEach(HashMap map) {
		Set<Map.Entry<String, Integer>> entries = map.entrySet();
		for (Map.Entry<String, Integer> entry : entries) {
			System.out.println(entry.getKey() + " : " + entry.getValue());
		}
	}

		static void iteratorUsingIterator(HashMap map) {
		Set<Map.Entry<String, Integer>> entries = map.entrySet();
		Iterator<Map.Entry<String, Integer>> i = entries.iterator();
		while(i.hasNext()) {
			Map.Entry<String, Integer> entry = i.next();
			System.out.println(entry.getKey() + " : " + entry.getValue());
		}
	}
}
```

## Collection Sort

```java
import java.util.*;

class Computer implements Comparable {
	int serial;
	String owner;
	
	Computer(int serial, String owner) {
		this.serial = serial;
		this.owner = owner;
	}

	public int compareTo(Object o) {
		return this.serial - ((Computer)o).serial;
		// a.compareTo(b) -> a > b: 양수 반환 | a == b: 0 반환 | a < b: 음수 반환
	}

	public String toString() {
		return serial + " " + owner;
	}
}

public class CollectionsDemo {
	public static void main(String[] args) {
		List<Computer> computers = new ArrayList<Computer>();
		computers.add(new Computer(500, "egoing"));
		computers.add(new Computer(200, "leezche"));
		computers.add(new Computer(3233, "graphittie"));

		Iterator i = computers.iterator();
		System.out.println("before");
		while(i.hasNext()) {
			System.out.println(i.next());
		}
		
		Collections.sort(computers);
		System.out.println("\nafter");
		i = computers.iterator();
		while(i.hasNext()) {
			System.out.println(i.next());
		}
	}
}
```