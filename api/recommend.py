from http.server import BaseHTTPRequestHandler
import json
import os
from openai import OpenAI

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # 1. Content-Length 확인 및 데이터 읽기
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                self._send_response(400, {'error': '요청 본문이 비어 있습니다.'})
                return

            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            user_prompt = data.get('prompt', '').strip()

            if not user_prompt:
                self._send_response(400, {'error': '입력값이 없습니다.'})
                return

            # 2. API Key 확인
            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                self._send_response(500, {'error': '서버에 OPENAI_API_KEY가 설정되지 않았습니다.'})
                return

            # 3. OpenAI API 호출
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "너는 사용자에게 친절하고 명확하게 맞춤 추천을 제공하는 AI 도우미야."},
                    {"role": "user", "content": user_prompt}
                ]
            )

            result_text = response.choices[0].message.content
            self._send_response(200, {'result': result_text})

        except Exception as e:
            self._send_response(500, {'error': f'서버 내부 오류: {str(e)}'})

    def _send_response(self, status_code, body):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(body, ensure_ascii=False).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()