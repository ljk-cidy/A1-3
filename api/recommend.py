# api/recommend.py
from http.server import BaseHTTPRequestHandler
import json, os
from google import genai

class handler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(payload, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        names = sorted(
            k for k in os.environ
            if any(w in k.upper() for w in ("GEMINI", "GOOGLE", "API", "KEY"))
        )
        value = os.environ.get("GEMINI_API_KEY", "")
        self._send(200, {
            "matching_env_names": names,
            "GEMINI_API_KEY_exists": "GEMINI_API_KEY" in os.environ,
            "GEMINI_API_KEY_length": len(value)
        })

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length) or "{}")
            prompt = (body.get("prompt") or "").strip()
            if not prompt:
                return self._send(400, {"error": "prompt가 비어 있습니다."})

            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                return self._send(500, {"error": "서버에 GEMINI_API_KEY가 설정되지 않았습니다."})

            model = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash")
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(model=model, contents=prompt)

            self._send(200, {"result": response.text or "응답이 비어 있습니다."})
        except Exception as e:
            self._send(500, {"error": str(e)})