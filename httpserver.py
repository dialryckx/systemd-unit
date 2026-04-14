from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response_text = "<h1>Hello! This is your Python server.</h1>"
        self.wfile.write(response_text.encode("utf-8"))

def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Starting the server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
