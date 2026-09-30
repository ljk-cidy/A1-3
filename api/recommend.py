# api/recommend.py
from http.server import BaseHTTPRequestHandler
import json, os, time
from google import genai

RETRY_CODES = {429, 500, 502, 503, 504}
MAX_ATTEMPTS = 3   # 모델 하나당 최대 시도 횟수
MAX_LEN = 100      # 재료 입력 최대 글자 수 (main.js/index.html의 maxlength와 동일하게 유지)

# 출력 형식 지시: 요리 이름 / 추가 양념 / 3단계 조리법
INSTRUCTION = (
    "당신은 자취생을 위한 요리 도우미입니다. "
    "사용자가 가진 재료로 만들 수 있는 간단한 요리 1가지를 추천하세요.\n"
    "반드시 아래 형식의 일반 텍스트로만 답하고, 마크다운 기호(#, *, **)는 쓰지 마세요.\n\n"
    "요리 이름: (이름)\n"
    "추가로 필요한 양념: (없으면 '없음')\n"
    "조리법:\n"
    "1단계. (설명)\n"
    "2단계. (설명)\n"
    "3단계. (설명)\n\n"
    "입력이 재료와 무관한 내용이면 '재료를 다시 입력해 주세요.'라고만 답하세요.\n\n"
    "사용자가 보유한 재료: "
)


def call_gemini(client, models, prompt):
    """모델 목록을 순서대로 시도하고, 일시적 오류는 잠깐 기다렸다가 재시도"""
    last_error = None
    for model in models:
        for attempt in range(MAX_ATTEMPTS):
            try:
                response = client.models.generate_content(model=model, contents=prompt)
                return response.text or ""
            except Exception as e:
                last_error = e
                code = getattr(e, "code", None)
                text = str(e)

                # 모델 이름을 못 찾으면 다음 모델로 넘어감
                if code == 404 or "NOT_FOUND" in text:
                    break

                # 일시적인 오류가 아니면 바로 중단
                retryable = code in RETRY_CODES or "UNAVAILABLE" in text
                if not retryable:
                    raise

                # 재시도 전에 잠깐 대기 (1.5초, 3초)
                if attempt < MAX_ATTEMPTS - 1:
                    time.sleep(1.5 * (attempt + 1))
    raise last_error


class handler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(payload, ensure_ascii=False).encode("utf-8"))

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length) or "{}")
            ingredients = (body.get("prompt") or "").strip()

            if not ingredients:
                return self._send(400, {"error": "재료를 1개 이상 입력해주세요."})
            if len(ingredients) > MAX_LEN:
                return self._send(400, {"error": f"재료는 {MAX_LEN}자 이내로 입력해주세요."})

            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                return self._send(500, {"error": "서버에 GEMINI_API_KEY가 설정되지 않았습니다."})

            primary = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash")
            fallbacks = [
                m.strip()
                for m in os.environ.get("GEMINI_FALLBACK_MODELS", "").split(",")
                if m.strip()
            ]
            models = [primary] + fallbacks

            client = genai.Client(api_key=api_key)
            result = call_gemini(client, models, INSTRUCTION + ingredients)
            self._send(200, {"result": result or "응답이 비어 있습니다."})

        except Exception as e:
            text = str(e)
            code = getattr(e, "code", None)
            if code == 503 or "UNAVAILABLE" in text:
                return self._send(503, {
                    "error": "현재 AI 서버에 요청이 많이 몰려 있습니다. 잠시 후 다시 시도해 주세요."
                })
            self._send(500, {"error": text})