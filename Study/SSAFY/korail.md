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



피드백 시작

기부, 그냥 기부 하는 것도 좋지만 기부의 수혜자도 정해놓았나요?
- 기부의 수혜자는 없지만, 러브 포인트에 병합하는 방식을 생각했습니다.

AI 학습 했다고 했는데, 멘토링 기간에 한 것인가요?
- 일주일 동안 학습했다는 걸 언급하는 게 좋음.

발표 자료를 어느 방식으로 만들어보는 게 좋을까요

수익 모델 어디서 금액을 따올 것인가요

실제 데이터를 필요하다는 메일도 발표에 스리슬쩍 끼워보는 건 어떨까요?

광고에 대한 부분은 어떻게 생각해보았나요?
- 광고는 생각 안해봤습니다.
	- 우리 주제가 코레일 측에서 좋아할 것 같은 주제라는 말(오피셜은 아님)

합치는 쪽으로 가고 싶으면?
- 시간을 1분 정도 남겨놓은 다음에 코레일 앱에 기술을 탑재할 수 있다는 점을 어필하면 좋을 것 같음
- 우리가 또 통일성을 가져가고자 