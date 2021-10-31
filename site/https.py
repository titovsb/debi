from wsgiref.simple_server import make_server
import uWSGI
# import http.server, ssl
from debi_framework.main import Framework
from urls import routes

PORT = 4443

# Создаем объект WSGI-приложения
debiapp = Framework(routes)

with make_server('', PORT, debiapp) as httpd:
    print(f'Server started on 8080 port...')
    httpd.serve_forever()


# import http.server, ssl
#
# server_address = ('localhost', 4443)
# httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
# httpd.socket = ssl.wrap_socket(httpd.socket,
#                                server_side=True,
#                                certfile='localhost.pem',
#                                ssl_version=ssl.PROTOCOL_TLS)
# httpd.serve_forever()
