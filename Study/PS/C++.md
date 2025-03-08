
# 메모리와 포인터

## 메모리
메모리 주소
0x0000              메모리 셀 1 Byte
0x0001              메모리 셀 1 Byte
0x0002              메모리 셀 1 Byte
0x0003              메모리 셀 1 Byte
0x0004              메모리 셀 1 Byte

- int 변수를 저장한다 -> 4 Byte 할당

메모리 주소
0x0000              int i
0x0001              int i
0x0002              int i
0x0003              int i
0x0004              메모리 셀 1 Byte

- int i의 주소 -> 사용하는 영역의 첫 번째 주소 -> 0x0000

- 만약 int i 에 0이라는 값을 할당한다면? -> 주소의 차이는 없음


## 포인터
메모리 관리는 언어마다 다르게 관리됨.
자바, 파이썬, 자바 스크립트 등은 개발자가 직접 변수에 메모리를 할당하거나 해제할 수 없고 가비지 컬렉터를 통해서 이를 수행함.
조금 더 로우레벨 언어인 C, C++ 등은 가비지 컬렉터가 없어서 개발자가 직접 메모리를 할당하고 해제해주어야 함

**포인터** = **메모리의 주소를 담는 타입** (0x0000...)
- 포인터는 변수의 첫 번째 바이트 주소를 가리킴
- 포인터는 메모리 동적 할당, 복사 없이 매개 변수로 사용, 클래스 및 구조체 연결 등에 사용
	- ex) 연결리스트의 노드
	```C++
	class Node  {
	public:
		int data;
		Node* next;
	};
	```
- data를 감싸는 Node라는 클래스
- 그리고 Node는 다음 노드의 주소값을 가리키는 next라는 포인터를 가지고 있음
- **\*** : 에스터리스크(Asterisk Operator)
- **&**: 앰퍼샌드(Ampersand)

```C++
double a = 4.4;
int c = 10;
int main() {
	double *b = &a;
	int *d = &c;

	cout << sizeof(b) << '\n';
	cout << sizeof(d) << '\n';
```

```Output
8
8
```

- int는 4바이트, double은 8바이트니까 포인터도 4, 8바이트가 되어야 하는 게 아닌가?
	- 포인터의 크기는 실행 OS 체제의 비트마다 달라짐
	- Window OS 64비트를 사용하는 경우의 포인터 사이즈 = 8 Byte
	- Window OS 32비트를 사용하는 경우의 포인터 사이즈 = 4 Byte


## 역참조 연산자 (에스터리스크)

**\*의 쓰임**
- 곱셈 연산
- 포인터 선언
- **역참조 연산자**

```C++
int main() {
	string a = "Dongni"
	string *b = &a;
	
	cout << b << '\n';
	cout << *b << '\n';
	return 0;
}
```

```Output
0x7fff4f6bbd20
Dongni
```

- Dongni라는 변수를 메모리 공간에 담게됨 -> 첫 번쨰 출력값을 주소값으로 하는 메모리 공간
- 이러한 메모리 주소를 가리키는 b라는 포인터가 존재함
- b라는 포인터를 기반으로 역참조 연산을 통해서 해당 메모리 주소의 **값**을 꺼냄

## Array to Pointer Decay

- int a[N]
	- int 형 변수가 N개 담겨있는 배열
	- int \*c = a 로 할당할 수도 있음
		- int\[] 와 int는 서로 다른데 어떻게 가능할까?
		- Array to Pointer Decay
			- a라는 배열의 이름을 포인터에 할당할 수가 있음
			- 할당함과 동시에 배열 a의 크기 정보가 날라가게 됨(Decay)
			- 그리고 배열 a의 첫 번째 주소가 배열의 이름 a에 바인딩 됨 
			- **배열의 이름 = 주소값**
				- 참고: a + 1에 대한 값을 찍어보면 첫 번째 주소의 다음 주소에 대한 값이 나오게 됨


# 중복된 요소 제거 로직

- 1, 1, 2, 2, 3, 3 이러한 숫자들이 있다고 했을 때, 중복을 제거해서 1, 2, 3을 뽑아내는 방법

1. Map 사용
	1. {1, 1}, {2, 1}, {3, 1}
	2. 이미 값이 있는 키 값들은 스킵해서 하나씩만 저장되게끔
```C++
map<int, int> mp;

int main() {
	vector<int> v{1, 1, 2, 2, 3, 3};
	for (int i : v) {
		if(mp[i]) {
		continue;
		} else {
			mp[i] = 1;
		}
	}
	vector<int> ret;
	for (auto it : mp) {
		ret.push_back(it.first);
	}
	for (int i : ret) cout << i << '\n';
}
```