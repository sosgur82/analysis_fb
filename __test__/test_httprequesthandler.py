from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000


class TestHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)


httpd = HTTPServer(('', PORT), TestHTTPRequestHandler)
print('Server running on port', PORT)
httpd.serve_forever()
