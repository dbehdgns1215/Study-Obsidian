
# JDBC - Java DataBase Connectivity

## 작업 순서
- Driver Loading (생략 가능)
- DB 연결 (Connection 객체 생성)
- SQL 문장 실행 준비 (Statement 객체 생성)
- SQL 문장 실행
	- `stmt.executeUpdate(sql) -> int`
	- `stmt.executeQuery(sql) -> Result Set`
- DB 접속 종료