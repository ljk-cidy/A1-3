# [서비스명] 기획서

1. 서비스 개요
- 서비스명: AI 자취생 냉장고 파먹기 (예시)
- 목적: 남은 재료로 만들 수 있는 간단 요리 추천
- 타겟 사용자: 요리가 어려운 1인 가구 및 자취생

2. 페이지/섹션 구성 (최소 3개 이상)
- Home (Hero 섹션): 서비스 소개 및 시작하기 버튼
- AI Recommendation (AI 추천): 재료 입력 폼 및 결과 출력 창
- FAQ / Contact: 자주 묻는 질문 및 문의 안내

3. AI 기능 상세 설계
- 입력: 보유 재료 (예: 계란, 대파, 밥)
- 출력: 요리 이름, 필요한 추가 양념, 3단계 조리법
- 예외/실패 처리 기준:
  - 빈 입력시: "재료를 1개 이상 입력해주세요." 경고창 출력
  - API 오류시: "서버 연결에 실패했습니다. 잠시 후 다시 시도해주세요."
  - 로딩 중: 버튼 비활성화 및 "AI가 레시피를 생각 중입니다..." 애니메이션 표시


# 🚀 

$$
서비스명 입력 - 예: AI 오늘 뭐 먹지?
$$

> **AI 기반 맞춤형 추천 웹 서비스**
>
> 사용자가 입력한 요구사항을 분석하여 AI가 최적의 추천 결과를 실시간으로 제공합니다.

## 📌 1. 서비스 소개

* **서비스명:** 

  $$
  서비스명 입력 - 예: AI 오늘 뭐 먹지?
  $$

* **서비스 목적:** 

  $$
  서비스 목적 입력 - 예: 남은 재료를 활용해 자취생이 빠르게 만들 수 있는 요리 레시피 추천
  $$

* **타겟 사용자:** 

  $$
  타겟 입력 - 예: 요리 선택에 고민이 많은 1인 가구 및 자취생
  $$

* **주요 기능:**

  * 사용자 요구사항 입력 폼 제공

  * OpenAI API 연동을 통한 실시간 맞춤 답변 생성

  * 입력값 유효성 검사 및 로딩/에러 UI 제공

  * 모바일 및 데스크톱 환경 지원 (반응형 웹)

## 🔗 2. 배포 URL

* **서비스 웹사이트:** [https://](https://a1-3-eight.vercel.app)a1-3-eight[.vercel.app](https://a1-3-eight.vercel.app)

* **GitHub 저장소:** [https://github.com/](https://github.com/ljk-cidy/A1-3?utm_source=gemini)ljk-cidy/A1-3

## 🛠️ 3. 기술 스택 (Tech Stack)

* **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS)

* **Backend:** Vercel Serverless Functions (Python 3.9+)

* **AI Engine:** OpenAI API (`gpt-4o-mini`)

* **Deployment & Hosting:** Vercel, GitHub

## ⚙️ 4. API 키 설정 방법 (환경 변수)

본 프로젝트는 보안을 위해 OpenAI API Key를 환경 변수로 관리하며, 코드 내에 직접 작성하지 않습니다.

### 🔑 Vercel 환경 변수 설정

1. [OpenAI Platform](https://platform.openai.com/api-keys?utm_source=gemini)에서 API Key를 발급받습니다.

2. [Vercel Dashboard](https://vercel.com?utm_source=gemini)에 로그인 후 해당 프로젝트로 이동합니다.

3. `Settings` ➔ `Environment Variables` 메뉴로 이동합니다.

4. 아래와 같이 환경 변수를 등록합니다.

   * **Key:** `OPENAI_API_KEY`

   * **Value:** 발급받은 API 키 (`sk-proj-...`)

5. `Save` 버튼을 누르고 프로젝트를 **Redeploy(재배포)** 합니다.

> ⚠️ **보안 주의사항:** API Key는 절대로 Git 저장소나 문서에 공개하지 않습니다.

## 💻 5. 로컬 실행 및 테스트 방법

### 1) 저장소 클론 (Clone)

```
git clone https://github.com/ljk-cidy/A1-3.git
cd 저장소-이름


```

### 2) 실행 방법

* **프론트엔드 테스트:** `index.html` 파일을 브라우저로 직접 열거나 Live Server 확장 프로그램을 통해 실행합니다.

* **API 테스트:** 백엔드 API 연동 테스트는 Vercel CLI (`vercel dev`) 또는 배포된 서버리스 환경에서 진행합니다.

## 📂 6. 프로젝트 디렉토리 구조

```
.
├── api/
│   └── recommend.py     # Vercel Python Serverless Function (백엔드 API)
├── css/
│   └── style.css        # 반응형 웹 스타일시트
├── js/
│   └── main.js          # 프론트엔드 자바스크립트 (API 호출 및 DOM 제어)
├── index.html           # 메인 UI 페이지
├── README.md            # 서비스 설명 및 문서
├── requirements.txt     # Python 패키지 의존성 목록
└── vercel.json          # Vercel 배포 및 라우팅 설정 파일


```