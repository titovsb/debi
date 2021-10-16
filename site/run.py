from wsgiref.simple_server import make_server
from debi_framework.main import Framework
from urls import routes

PORT = 8080

# Создаем объект WSGI-приложения
debiapp = Framework(routes)

with make_server('', PORT, debiapp) as httpd:
    print(f'Server started on 8080 port...')
    httpd.serve_forever()

