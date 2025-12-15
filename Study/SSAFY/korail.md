![[Pasted image 20251212144433.png]]

# 뱃지 - 여행 기록
- AI가 추천해준 장소 리스트
	- 장소 정보
- 여행 제목
- 여행 일자
- 방문한 지역 (시, 구)
- 총 개수 및 방문한 개수

```d
{
  id: string,              // 고유 ID
  title: string,           // 여행 이름
  regions: Array<string>,  // 여행 지역 배열 ["대전 동구", "대전 중구"]
  startDate: string,       // 여행 시작 날짜 (YYYY-MM-DD)
  endDate: string,         // 여행 종료 날짜 (YYYY-MM-DD)
  progress: number,        // 방문 완료한 장소 수 (자동 계산)
  total: number,           // 전체 장소 수 (자동 계산)
  places: Array<Place>,    // 여행 장소 목록
  status: string,          // 뱃지 상태 (not_started/in_progress/completed)
  color: string|null,      // 프로그레스 바 색상 (없으면 자동 계산)
  createdAt: Date,         // 생성 시간
  completedAt: Date|null   // 완료 시간
}
```



![[Pasted image 20251212145214.png]]

# 장소
- 장소명
- 장소 타입 (음식점, 카페, 관광지 등)
- 주소
	- 신주소, 구주소
- 방문 여부
- 영업 시간
- 전화번호

```d
  id: string,              // 장소 고유 ID
  name: string,            // 장소 이름
  type: string,            // 장소 타입 (음식점/카페/관광지 등)
  businessHours: string,   // 영업 시간
  closedDay: string|null,  // 휴무일
  visitDate: string|null,  // 방문 날짜 (null이면 미방문)
  visited: boolean,        // 방문 여부
  imageUrl: string|null,   // 장소 이미지 URL
  location: object|null,   // 위치 정보 (위도, 경도)
  address: string|null,    // 주소
  phone: string|null       // 전화번호
```


---


지역

## 서울
- 한복 저고리 (리본 달린)
- 서울타워

## 부산
- 갈매기





# 최은성 멘토님 피드백

경유지 포함해서 예매하는 게 어렵게 느낌.
좌석 선택, 시간 선택 등등 시스템적인 부족함을 해결해보고자.
예매 + 여행 경로 + 계획을 합친 애플리케이션

경유지를 선택했을 때, 정보가 바로 나오는 것이 좋으냐 안좋으냐에 대한 의견을 나누어 보았음.
기다리는 시간이 긴 경우에는 토스에서 발상을 얻은 이미지를 출력해줌

관광지나 맛집에 대한 추천을 진행


