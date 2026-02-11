from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
from datetime import datetime


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Server", "WebRequestHandler/1.0")
        self.send_header("Date", datetime.now().astimezone().strftime("%a, %d %b %Y %H:%M:%S %Z"))
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

    def get_response(self):
        return f"""
    <h1> Hola Web </h1>
    <p> URL Parse Result : {self.url()}         </p>
    <p> Path Original: {self.path}         </p>
    <p> Headers: {self.headers}      </p>
    <p> Query: {self.query_data()}   </p>
"""


if __name__ == "__main__":
    port = 8000
    print(f"Starting server on port {port}")
    server = HTTPServer(("localhost", port), WebRequestHandler)
    server.serve_forever()

