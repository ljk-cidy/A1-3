# 🚀 AI 기반 맞춤형 추천 웹 서비스

**사용자 맞춤형 실시간 AI 추천 서비스**

사용자가 입력한 요구사항을 분석하여 **Google Gemini API** 기반의 추천 결과를 실시간으로 제공합니다.

---

## 📌 1. 서비스 소개

- **서비스명**: 나만의 AI 추천 서비스
- **서비스 목적**: 궁금한 것을 입력하면 AI가 빠르고 정확하게 추천해 주는 웹 서비스 (예: 오늘 저녁 메뉴 추천)
- **타겟 사용자**: 메뉴·레시피 등 일상적인 선택에 고민이 많은 사용자 (1인 가구, 자취생 포함)
- **페이지 구성**: 메인/서비스소개/AI추천/FAQ
- **주요 기능**
  - 사용자 요구사항 입력 폼 제공
  - Gemini API 연동을 통한 실시간 맞춤 답변 생성
  - 입력값 유효성 검사 및 로딩/에러 화면 제공
  - 모바일 및 데스크톱 환경 지원 (반응형 웹)
  - 자주 묻는 질문(FAQ) 제공

---

## 🔗 2. 배포 URL

- **서비스 웹사이트**: https://a1-3-eight.vercel.app
- **GitHub 저장소**: https://github.com/ljk-cidy/A1-3

---

## 🛠️ 3. 기술 스택 (Tech Stack)

| 구분 | 사용 기술 |
|---|---|
| Frontend | HTML5, CSS3, JavaScript (Vanilla JS) |
| Backend | Vercel Serverless Functions (Python 3.9+) |
| AI Engine | Google Gemini API (`google-genai` 라이브러리) |
| Deployment & Hosting | Vercel, GitHub |

---

## ⚙️ 4. API 키 설정 방법 (환경 변수)

본 프로젝트는 보안을 위해 **Gemini API Key를 환경 변수로 관리**하며, 코드 내에 직접 작성하지 않습니다.

### 🔑 Vercel 환경 변수 설정

1. [Google AI Studio](https://aistudio.google.com/app/apikey)에서 API Key를 발급받습니다.
2. [Vercel Dashboard](https://vercel.com)에 로그인 후 해당 프로젝트로 이동합니다.
3. `Settings` ➔ `Environment Variables` 메뉴로 이동합니다.
4. 아래와 같이 환경 변수를 등록합니다.

| Key | Value | 필수 |
|---|---|---|
| `GEMINI_API_KEY` | 발급받은 API 키 (`AIza...`) | 필수 |
| `GEMINI_MODEL` | 사용할 모델명 (미설정 시 코드의 기본값 사용) | 선택 |
| `GEMINI_FALLBACK_MODELS` | 기본 모델이 혼잡할 때 넘어갈 예비 모델명 (여러 개는 쉼표로 구분) | 선택 |

5. `Environments`에서 **Production이 포함**되도록 선택하고 `Save`를 누릅니다.
6. **Redeploy(재배포)** 합니다. 환경 변수는 등록 이후에 만든 배포부터 적용됩니다.

> ⚠️ **보안 주의사항**: API Key는 절대로 Git 저장소, 문서, 채팅, 스크린샷에 공개하지 않습니다.
> 노출되었다면 즉시 키를 삭제하고 새로 발급하여 Vercel 값을 교체한 뒤 재배포합니다.

> 📝 환경 변수 **이름은 코드와 한 글자도 다르면 안 됩니다** (대소문자·밑줄·공백 포함).
> 모델명은 자주 바뀌므로 Google AI Studio에서 현재 사용 가능한 이름을 확인해 입력합니다.

---

## 💻 5. 로컬 실행 및 테스트 방법

### 1) 저장소 클론 (Clone)

```bash
git clone https://github.com/ljk-cidy/A1-3.git
cd A1-3
```

### 2) 실행 방법

- **프론트엔드 테스트**: `index.html` 파일을 브라우저로 직접 열거나 Live Server 확장 프로그램을 통해 실행합니다.
  (이 방식은 화면 확인용이며, 서버 API는 호출되지 않습니다.)
- **API 테스트**: 백엔드 API 연동 테스트는 Vercel CLI(`vercel dev`) 또는 배포된 서버리스 환경에서 진행합니다.
  ```bash
  npm i -g vercel
  vercel dev
  ```
  로컬에서 실행할 때도 `GEMINI_API_KEY`가 필요하며, 키가 담긴 파일(`.env` 등)은 `.gitignore`에 추가해 저장소에 올라가지 않게 합니다.

---

## 📂 6. 프로젝트 디렉토리 구조

```
.
├── api/
│   └── recommend.py     # Vercel Python Serverless Function (백엔드 API, /api/recommend)
├── css/
│   └── style.css        # 반응형 웹 스타일시트
├── js/
│   └── main.js          # 프론트엔드 자바스크립트 (API 호출 및 DOM 제어)
├── index.html           # 메인 UI 페이지
├── README.md            # 서비스 설명 및 문서
├── requirements.txt     # Python 패키지 의존성 목록 (google-genai)
└── vercel.json          # Vercel 배포 설정 파일
```

> `requirements.txt`는 반드시 **프로젝트 루트**에 두고 **UTF-8**로 저장합니다.
> `vercel.json`은 JSON 문법만 허용되며(주석·JS 코드 불가), 파일별 함수 방식으로 빌드되도록 프레임워크 자동 감지를 조정하는 최소 설정만 둡니다.

---

## 🧭 7. 서비스 기획 및 구현 현황

### 7-1. 페이지/섹션 구성

| 기획 섹션 | 기획 내용 | 현재 구현 | 상태 |
|---|---|---|---|
| Home (Hero) | 서비스 소개 및 시작하기 버튼 | Hero 배너(제목·소개 문구) 구현, **시작하기 버튼 없음** | 🔶 부분 |
| AI Recommendation | 입력 폼 및 결과 출력 창 | 입력창 + 추천받기 버튼 + 결과 카드 구현 | ✅ 구현 |
| FAQ / Contact | 자주 묻는 질문 및 문의 안내 | FAQ 2개 구현, **문의(Contact) 안내 없음** | 🔶 부분 |

### 7-2. AI 기능 상세 설계

| 항목 | 기획 내용 | 현재 구현 | 상태 |
|---|---|---|---|
| 입력 | 보유 재료 (예: 계란, 대파, 밥) | 자유 질문 입력 (예: "오늘 저녁 메뉴 추천해 줘") | 🔶 차이 |
| 출력 | 요리 이름, 필요한 추가 양념, 3단계 조리법 | 서버가 입력 문장을 그대로 Gemini에 전달하며 **출력 형식 지시 없음** | ✅ 구현 |
| 빈 입력 처리 | "재료를 1개 이상 입력해주세요." 경고창 | 경고창은 있으나 문구가 "내용을 입력해주세요!" | 🔶 문구 차이 |
| API 오류 처리 | "서버 연결에 실패했습니다. 잠시 후 다시 시도해주세요." | 화면에 `오류 발생: <서버가 보낸 상세 메시지>` 표시 (503만 별도 한국어 안내) | 🔶 차이 |
| 로딩 중 | 버튼 비활성화 + "AI가 레시피를 생각 중입니다..." 애니메이션 | 버튼 비활성화 + "생성 중..." + "AI가 답변을 생각하는 중입니다..." + 회전 스피너 | 🔶 문구 차이 (동작은 충족) |
| 반응형 | 모바일·데스크톱 지원 | 600px 이하에서 입력창·버튼 세로 배치 | ✅ 구현 |
| 입력값 유효성 검사 | 빈 입력 방지 | 빈 값 검사 구현 (서버에서도 400 응답) | ✅ 구현 |

### 7-3. 문서(템플릿)와 실제 구현의 차이 정리

| 항목 | 템플릿 기재 | 실제 프로젝트 |
|---|---|---|
| AI 엔진 | OpenAI API (`gpt-4o-mini`) | **Google Gemini API** |
| API 키 환경 변수 | `OPENAI_API_KEY` (`sk-proj-...`) | **`GEMINI_API_KEY`** (`AIza...`) |
| 키 발급처 | OpenAI Platform | **Google AI Studio** |
| 파이썬 라이브러리 | (미기재) | `google-genai` |
| `vercel.json` 역할 | 배포 및 라우팅 설정 | 프레임워크 자동 감지 조정 등 최소 설정 (특별한 라우팅 없음) |

---

## 🧪 8. API 명세

### `POST /api/recommend`

**요청**

```json
{ "prompt": "오늘 저녁 메뉴 추천해 줘" }
```

**응답**

| 상태 | 본문 | 의미 |
|---|---|---|
| 200 | `{ "result": "AI 답변" }` | 성공 |
| 400 | `{ "error": "prompt가 비어 있습니다." }` | 질문이 비어 있음 |
| 500 | `{ "error": "..." }` | 키 미설정, 인증 오류, 서버 내부 오류 등 |
| 503 | `{ "error": "현재 AI 서버에 요청이 많이 몰려 있습니다..." }` | Google 서버 혼잡 (재시도 후에도 실패) |

- 프론트엔드(`main.js`)와 서버(`recommend.py`)는 **`prompt` / `result` / `error`** 세 이름으로 데이터를 주고받습니다. 한쪽을 바꾸면 반드시 다른 쪽도 함께 바꿉니다.
- 일시적 오류(429, 5xx, 503)는 서버에서 **최대 3회 재시도**하고, 예비 모델이 설정되어 있으면 자동으로 전환합니다.
- 브라우저 주소창(GET)으로 열면 `do_POST`만 정의되어 있어 오류 문구가 나오는 것이 정상입니다.

**동작 흐름**

```
[브라우저]                     [Vercel 서버 함수]                [Google]
 질문 입력, "추천받기" 클릭
     │  POST /api/recommend { "prompt": "질문" }
     ├────────────────────────▶ 환경 변수에서 키 읽기
     │                          Gemini API 호출 ──────────────▶ 답변 생성
     │                          (일시 오류 시 재시도/예비 모델) ◀────────────
     │  { "result": "답변" }
     ◀──────────────────────── 응답 반환
 결과 표시
```

---

## 🩺 9. 트러블슈팅 기록

| # | 증상 / 오류 | 원인 | 해결 |
|---|---|---|---|
| 1 | 디자인이 없는 기본 화면, 버튼 무반응, 콘솔에 `main.js`·`style.css` 404 | 배포가 실패한 상태에서 예전 버전이 계속 서비스됨 (폴더 구조와 `index.html` 경로 자체는 정상) | 아래 2~3번 해결 후 재배포, 강력 새로고침 |
| 2 | VS Code: `vercel.json` "JSON 개체, 배열 또는 리터럴이 필요합니다" | 파일이 비어 있거나 JSON이 아닌 내용(JS 코드 등)이 섞임 | 파일에는 **JSON만** 유지 |
| 3 | 배포 목록에서 빌드가 2~3초 만에 「오류」 | 라이브러리 설치 전 설정 검사 단계에서 거부됨 (`vercel.json`) | `vercel.json`을 단순하게 정리, 충돌 설정 제거 |
| 4 | `requirements.txt` 불일치 (`openai` 기재 vs `anthropic` import) | 서버에 필요한 라이브러리가 설치되지 않음 | import 문과 `requirements.txt` 일치 (현재 `google-genai`) |
| 5 | 프론트·서버 데이터 이름 불일치 위험 | 요청 `prompt`, 응답 `result`, 오류 `error` 통일 필요 | `main.js`와 `recommend.py` 이름 통일 |
| 6 | 빌드 오류 `No python entrypoint found in default locations, but potential entrypoint found: api/recommend.py (variable: handler)` | Vercel이 프로젝트를 단일 Python 앱으로 빌드하려다 진입점 파일(app, index, main 등)을 찾지 못함 | `vercel.json`의 `"framework": null` 또는 대시보드 Framework Preset을 **Other**로 설정 (대안: `pyproject.toml`의 `[tool.vercel] entrypoint`) |
| 7 | 화면 `서버에 API 키가 설정되지 않았습니다` | 서버에 키 환경 변수가 없었고, 코드는 Anthropic용이었지만 실제 보유 키는 **Gemini** 키였음 | `recommend.py`를 Gemini SDK로 교체, `GEMINI_API_KEY` 등록 후 재배포 |
| 8 | 재배포 후에도 키 미설정 문구 | 이름 오타, Production 미적용, 등록 후 재배포 누락 등이 원인 후보 | 이름·환경 재확인, 필요 시 삭제 후 재등록, 새 배포 생성. 진단용 `do_GET`으로 존재 여부 확인 후 **삭제** |
| 9 | 콘솔 `favicon.ico` 404 | 아이콘 파일이 없어 브라우저가 알리는 메시지 (기능과 무관) | 무시 가능. 없애려면 `<link rel="icon" href="data:,">` 추가 |
| 10 | 개발자 도구의 `Missing param(s) [id]...`, `Tracking Prevention`, `status 400 (/event)` | **Vercel 대시보드 자체**의 콘솔 메시지 (내 사이트와 무관) | 조치 불필요. 확인은 내 사이트 주소의 Console·Network 탭에서 수행 |
| 11 | `503 UNAVAILABLE ... high demand` | Google 모델 서버의 일시적 혼잡 (키·설정은 정상) | 잠시 후 재시도. 서버 코드에 **자동 재시도**와 **예비 모델 전환** 적용 |

**교훈**

- 배포가 실패하면 **이전 성공 버전이 계속 서비스**되므로, 코드를 고쳐도 화면이 그대로일 수 있습니다. 먼저 Deployments 상태를 확인합니다.
- 빌드 시간이 2~3초로 짧은 오류는 설정 파일 검사 단계 실패일 가능성이 큽니다.
- 오류 문구가 **내 코드가 보낸 것**인지 **외부 서비스가 보낸 것**인지 구분하면 원인 파악이 빨라집니다.
- 라이브러리를 바꾸면 `import` 문, `requirements.txt`, 환경 변수 이름, 키 종류를 **한 세트로** 점검합니다.

---

## ✅ 10. 배포 후 점검 체크리스트

- [ ] Vercel **Deployments** 최신 항목이 **Ready**이고 Production 배지가 붙어 있는가
- [ ] 대표 도메인으로 `Ctrl+Shift+R` 강력 새로고침 후 접속했는가
- [ ] `/css/style.css`, `/js/main.js` 주소를 직접 열면 내용이 보이는가
- [ ] `requirements.txt`가 루트에 있고 `google-genai`가 UTF-8로 적혀 있는가
- [ ] `vercel.json`에 문법 오류가 없는가
- [ ] `GEMINI_API_KEY` 이름이 정확하고 Production에 적용되어 있는가
- [ ] 환경 변수 등록 **이후**에 새 배포를 만들었는가
- [ ] 개발자 도구 **Network** 탭의 `recommend` 요청 Status와 Response를 확인했는가
- [ ] Vercel **Logs**에서 `/api/recommend`의 서버 오류를 확인했는가

**화면 오류 문구별 대응**

| 문구 | 의미 | 대응 |
|---|---|---|
| `GEMINI_API_KEY가 설정되지 않았습니다` | 서버가 키를 못 찾음 | 이름·적용 환경 확인 후 새 배포 |
| `API key not valid` 계열 (400) | 키 값이 틀림 | 새 키 발급, 값 교체 후 새 배포 |
| `model not found` 계열 (404) | 모델명이 다름 | `GEMINI_MODEL`을 현재 사용 가능한 모델명으로 변경 |
| `quota`, `RESOURCE_EXHAUSTED` (429) | 사용 한도 초과 | 잠시 후 재시도, 결제·한도 설정 확인 |
| `503 UNAVAILABLE` | Google 서버 혼잡 | 잠시 후 재시도, 예비 모델 설정 |
| `No module named ...` | 라이브러리 미설치 | `requirements.txt` 내용·위치·인코딩 확인 |

---

## 🔒 11. 보안 및 운영 유의사항

- **API 키를 코드, GitHub, 채팅, 스크린샷에 노출하지 않습니다.** 키는 `GEMINI_API_KEY` 환경 변수로만 보관하고, 브라우저에서 AI를 직접 호출하지 않습니다.
- 공개 주소를 아는 사람은 누구나 서비스를 사용할 수 있고, 사용량은 내 키에 반영됩니다. FAQ의 "누구나 무료로 이용" 문구를 실제 운영 방식에 맞게 조정하고, 사용량 알림·한도를 설정합니다.
- 진단용으로 임시 추가한 코드(`do_GET` 등)는 확인 후 삭제하고 다시 배포합니다.

---

## 🔧 12. 향후 개선 사항 (기획서 대비 보완)

- [ ] 입력 문구를 **보유 재료 입력** 형태로 변경 (라벨·placeholder·경고 문구 "재료를 1개 이상 입력해주세요.")
- [ ] 서버에서 Gemini에 **출력 형식 지시**(요리 이름 / 필요한 추가 양념 / 3단계 조리법) 추가
- [ ] 오류 문구를 기획서 문구("서버 연결에 실패했습니다. 잠시 후 다시 시도해주세요.")로 통일
- [ ] 로딩 문구를 "AI가 레시피를 생각 중입니다..."로 변경
- [ ] Hero 섹션에 **시작하기 버튼** 추가 (AI 추천 섹션으로 이동)
- [ ] FAQ 아래에 **문의(Contact) 안내** 추가
- [ ] 사용자별 요청 횟수 제한, 입력 길이 제한
- [ ] 파비콘 추가, 모바일 화면 점검