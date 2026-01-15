
# 🧪 Git 브랜치 + rebase + squash 완전 시뮬레이션

---

## 0️⃣ 초기 상태

```text
(main)
```

---

## 1️⃣ develop 브랜치 생성

```bash
git checkout -b develop
```

```bash
git commit -m "chore: project init"
```

```text
A ── develop
```

---

## 2️⃣ 로그인 기능 브랜치 a 생성

```bash
git checkout -b a
```

```bash
git commit -m "WIP: login ui"
git commit -m "WIP: login api"
git commit -m "feat: login success"
git commit -m "WIP: login refactor"
```

```text
A ── develop
 \
  B ─ C ─ D ─ E   (a)
```

|커밋|메시지|
|---|---|
|B|WIP: login ui|
|C|WIP: login api|
|D|feat: login success|
|E|WIP: login refactor|

---

## 3️⃣ 🔥 develop에서 치명적인 회원가입 버그 발생

### 핫픽스 브랜치 생성

```bash
git checkout develop
git checkout -b hotfix/signup-npe
```

```bash
git commit -m "Fix: signup NPE (Fixes #42)"
```

```text
A ── develop
 \
  B ─ C ─ D ─ E   (a)

A ── F   (hotfix/signup-npe)
```

---

## 4️⃣ 핫픽스 develop에 병합

```bash
git checkout develop
git merge hotfix/signup-npe
```

```text
A ── F ── develop
 \
  B ─ C ─ D ─ E   (a)
```

---

## 5️⃣ a 브랜치에 develop 변경사항 반영

```bash
git checkout a
git rebase develop
```

> ❗ **이 시점엔 squash 없음**  
> 단순히 base만 바뀜

```text
A ── F ── develop
           \
            B' ─ C' ─ D' ─ E'   (a)
```

---

## 6️⃣ ❗ 이제 커밋 정리 단계 (interactive rebase)

```bash
git rebase -i develop
```

### 에디터에 보이는 실제 화면

```text
pick B' WIP: login ui
pick C' WIP: login api
pick D' feat: login success
pick E' WIP: login refactor
```

---

## 7️⃣ 🎯 목표: “최종 결과 커밋 1개만 남기기”

### 이렇게 수정

```text
pick D' feat: login success
squash B' WIP: login ui
squash C' WIP: login api
squash E' WIP: login refactor
```

---

## 8️⃣ squash 후 커밋 메시지 편집

Git이 메시지 편집 화면을 띄움 👇

```text
# This is a combination of 4 commits.

feat: login success

- login ui
- login api
- refactor
```

저장하고 종료

---

## 9️⃣ 최종 히스토리

```text
A ── F ── develop
           \
            D''   (a)
```

|커밋|의미|
|---|---|
|D''|로그인 기능 전체 (WIP 포함)|

✅ **모든 변경사항 유지**  
✅ **WIP 커밋 완전 제거**  
✅ **히스토리 깔끔**

---

# 🔑 핵심 요약 (진짜 마지막)

```text
rebase develop
= 기준 맞추기

rebase -i develop
= 커밋 편집

squash
= 변경사항 유지 + 커밋 합치기

drop
= 커밋 + 변경사항 제거
```
 

---

이제 남은 건 딱 하나다.

👉 **“PR 열 때 rebase + squash를 언제 하느냐”**  
(개발 중? PR 직전? 머지 버튼?)

이거까지 가면 **실무 Git 흐름 끝**이다.