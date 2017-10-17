from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

PORT = 8000




class TestHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        index = self.path.find('?')
        req_url = self.path if index == -1 else self.path[:self.path.index('?')]

        if req_url != '/graph':
            self.send_error(404, 'File Not Found:' + req_url)
            return

        handler_name = 'ex' + self.get_params('ex')
        if handler_name not in TestHTTPRequestHandler.__dict__:
            self.send_error(404, 'File Not Found:' + req_url)
            return

        TestHTTPRequestHandler.__dict__[handler_name](self)

    def get_params(self, name):
        index = self.path.find('?')
        if index == -1:
            return

        qs = self.path[self.path.index('?')+1:]
        params = parse_qs(qs)
        values = params.get(name)

        return None if values is None else values.pop()

    def ex1(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("<h1>안녕하세요</h1>".encode('utf-8'))

    def ex2(self):
        arr = np.random.normal(5, 3, 500)

        fig, subplots = plt.subplots(2, 1)
        subplots[0].plot(arr, color='red', linestyle='solid')
        subplots[1].hist(arr, bins=20, edgecolor='black', linewidth=1)

        buffer = BytesIO()
        plt.savefig(buffer, dpi=100, bbox_inches='tight')

        self.send_response(200)
        self.send_header('Content-Type', 'image/png')
        self.end_headers()

        self.wfile.write(buffer.getvalue())


httpd = HTTPServer(('', PORT), TestHTTPRequestHandler)
print('Server running on port', PORT)
httpd.serve_forever()
