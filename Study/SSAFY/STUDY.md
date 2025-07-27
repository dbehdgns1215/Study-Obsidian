
````markdown
# 🧠 SSAFY Git 스터디 브랜치 관리 가이드

스터디 팀원들이 깃을 통해 주차별로 안정적이고 깔끔하게 협업하기 위한 Git 사용 가이드입니다.

---

## 📌 기본 원칙

- `main` 브랜치는 설정 및 기준 브랜치입니다. **직접 커밋/푸시 금지**
- `src/본인이름/` 폴더만 수정합니다.
- 각 주차는 별도 브랜치 (`week1`, `week2`, …)로 관리합니다.
- 항상 **작업 전 `pull`**, 푸시 전에는 **`pull --rebase`**를 합니다.

---

## 🔁 매 주차 작업 순서 (예: week1)

### ✅ 1. main 최신화 (작업 시작 전 1회)
```bash
git checkout main
git pull origin main
````

---

### ✅ 2. 주차별 브랜치 생성 또는 이동

```bash
# week1 브랜치가 없으면 새로 생성
git checkout -b week1

# 이미 있는 경우 이동만
git checkout week1
```

---

### ✅ 3. 원격 브랜치 최신화

```bash
git pull origin week1
```

---

### ✅ 4. 작업물 추가

`src/내이름/` 폴더에 파일을 추가 또는 수정합니다.

예: `src/donghun/BOJ1234.java`

---

### ✅ 5. 커밋

```bash
git add .
git commit -m "week1: BOJ1234 풀이 추가"
```

---

### ✅ 6. 푸시 전 rebase

```bash
git pull --rebase origin week1
```

> 깔끔한 커밋 히스토리를 유지합니다. 충돌 시 직접 해결 후 `git rebase --continue`를 입력합니다.

---

### ✅ 7. 푸시

```bash
git push origin week1
```

---

## 📝 커밋 메시지 예시

```text
week1: BOJ1234 풀이 추가
week2: 과제 제출
week3: 자바 파일 리팩토링
```

---

## 🔍 유용한 명령어 모음

|목적|명령어|
|---|---|
|현재 브랜치 확인|`git branch`|
|변경 파일 확인|`git status`|
|전체 커밋 히스토리 보기|`git log --oneline --graph --all`|
|원격 저장소 확인|`git remote -v`|
|원격 브랜치 목록|`git branch -r`|
|변경사항 임시 저장|`git stash`|
|임시 저장한 작업 복원|`git stash pop`|

---

## ⚠️ 자주 발생하는 실수 및 해결법

|상황|원인|해결책|
|---|---|---|
|`error: src refspec week1 does not match any`|브랜치 만들기 전에 커밋 없음|커밋 후 푸시하거나 브랜치 다시 생성|
|pull 하려는데 변경사항 있어서 막힘|변경 중인 파일 있음|`git stash`, `pull`, `git stash pop`|
|main에서 커밋해버림|브랜치 안 바꾸고 작업|`git checkout -b weekN`으로 커밋 옮기기|

---

## 🛠️ 최초 레포 설정 방법 (최초 1회)

1. 레포 클론

```bash
git clone https://github.com/your-team-url/algo_study.git
```

2. 본인 폴더 생성

```bash
cd algo_study/src
mkdir donghun  # ← 본인 이름
```

3. main 브랜치 최신화 후 주차 브랜치 생성

```bash
git checkout main
git pull origin main
git checkout -b week1
```

---

## ✅ 핵심 요약

- 항상 `main → 최신화 → 주차 브랜치 이동`
- 작업 후 `commit → pull --rebase → push`
- 커밋 충돌 최소화 + 협업 안정성 최대화
- 커밋 메시지는 명확하고 통일성 있게 작성

---

> `git init`
> 필수적으로 `git remote add origin <주소>`


