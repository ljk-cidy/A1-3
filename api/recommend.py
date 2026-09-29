# api/recommend.py
from http.server import BaseHTTPRequestHandler
import json, os
import anthropic # type: ignore

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
            prompt = (body.get("prompt") or "").strip()
            if not prompt:
                return self._send(400, {"error": "prompt가 비어 있습니다."})

            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if not api_key:
                return self._send(500, {"error": "서버에 API 키가 설정되지 않았습니다."})

            client = anthropic.Anthropic(api_key=api_key)
            msg = client.messages.create(
                model="claude-sonnet-5-5",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}],
            )
            self._send(200, {"result": msg.content[0].text})
        except Exception as e:
            self._send(500, {"error": str(e)})