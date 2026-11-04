from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

print("Starting server on port 8000...")
server = HTTPServer(('0.0.0.0', 8000), MyHandler)
server.serve_forever()
