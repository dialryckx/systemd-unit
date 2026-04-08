from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Отправляем HTTP-статус 200 (OK)
        self.send_response(200)
        # Указываем тип контента
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        # Тело ответа
        response_text = "<h1>Привет! Это твой сервер на Python.</h1>"
        self.wfile.write(response_text.encode("utf-8"))

def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Запуск кастомного сервера на порту {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
