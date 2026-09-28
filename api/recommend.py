from http.server import BaseHTTPRequestHandler
import json
import os
from openai import OpenAI

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # 1. Request Body 읽기
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            user_prompt = data.get('prompt', '')

            if not user_prompt:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Prompt is required'}).encode())
                return

            # 2. OpenAI API 호출 (환경변수 사용)
            api_key = os.environ.get("OPENAI_API_KEY")
            client = OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "너는 친절하고 유용한 AI 추천 도우미야."},
                    {"role": "user", "content": user_prompt}
                ]
            )

            result_text = response.choices[0].message.content

            # 3. 성공 응답 전송 (200 OK)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_body = json.dumps({'result': result_text})
            self.wfile.write(response_body.encode('utf-8'))

        except Exception as e:
            # 4. 서버 오류 처리 (500 Internal Server Error)
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_body = json.dumps({'error': str(e)})
            self.wfile.write(error_body.encode('utf-8'))