from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
from datetime import datetime

with open("home.html", "r", encoding="utf-8") as f:
    home_html = f.read()

with open("1.html", "r", encoding="utf-8") as f:
    proyecto1_html = f.read()

contenido = {
    '/': home_html,
    '/proyecto/1': proyecto1_html,
    '/proyecto/2': """<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ana Lee - MeFalta</title>
  </head>
  <body>
    <h1>Ana Lee</h1>
    <h2>MeFalta - ¿Qué película o serie me falta ver?</h2>
    <p>
      Aplicación web que permite llevar un registro de las películas y series que
      el usuario quiere ver o ya ha visto. El usuario puede marcar títulos como
      vistos y recibir recomendaciones personalizadas basadas en su historial.
    </p>
    <h2>Tecnologías</h2>
    <ul>
      <li>HTML5</li>
      <li>CSS</li>
      <li>JavaScript</li>
      <li>API REST</li>
    </ul>
    <a href="/">Volver al inicio</a>
  </body>
</html>""",
    '/proyecto/3': """<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ana Lee - Foto22</title>
  </head>
  <body>
    <h1>Ana Lee</h1>
    <h2>Foto22 - Gestión de fotos</h2>
    <p>
      Plataforma web para la gestión y organización de fotografías. Permite subir,
      clasificar y compartir fotos en álbumes, con herramientas de edición básica
      y almacenamiento en la nube.
    </p>
    <h2>Tecnologías</h2>
    <ul>
      <li>HTML5</li>
      <li>CSS</li>
      <li>JavaScript</li>
      <li>Cloud Storage</li>
    </ul>
    <a href="/">Volver al inicio</a>
  </body>
</html>""",
}


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        ruta = self.url().path
        if ruta in contenido:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Server", "WebRequestHandler/1.0")
            self.send_header("Date", datetime.now().astimezone().strftime("%a, %d %b %Y %H:%M:%S %Z"))
            self.end_headers()
            self.wfile.write(contenido[ruta].encode("utf-8"))
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