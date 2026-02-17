from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
from datetime import datetime


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        ruta = self.url().path
        if ruta == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Server", "WebRequestHandler/1.0")
            self.send_header("Date", datetime.now().astimezone().strftime("%a, %d %b %Y %H:%M:%S %Z"))
            self.end_headers()
            with open("home.html", "r", encoding="utf-8") as f:
                contenido = f.read()
            self.wfile.write(contenido.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.send_header("Server", "WebRequestHandler/1.0")
            self.send_header("Date", datetime.now().astimezone().strftime("%a, %d %b %Y %H:%M:%S %Z"))
            self.end_headers()
            error_html = """<!DOCTYPE html>
            <html lang="es">
            <head><meta charset="UTF-8"><title>404 No Encontrado</title></head>
            <body>
            <h1>Error 404</h1>
            <p>La página solicitada no fue encontrada.</p>
            <a href="/">Volver al inicio</a>
            </body>
            </html>"""
            self.wfile.write(error_html.encode("utf-8"))


if __name__ == "__main__":
    port = 8000
    print(f"Starting server on port {port}")
    server = HTTPServer(("localhost", port), WebRequestHandler)
    server.serve_forever()