import quopri

from debi_framework.templator import render
from debi_framework.framework_requests import GetRequests, PostRequests

ANSWER404 = '404 Not Found'


class Page404:
    def __call__(self, request):
        return ANSWER404, render('404.html')


class Framework:
    def __init__(self, obj):
        self.sitemap = obj

    def __call__(self, environment, response):
        # Получаем адрес, по которому пользователь выполнил переход
        sitepath = environment['PATH_INFO']

        # Добавляем закрывающий слеш если надо
        if not sitepath.endswith('/'):
            sitepath = f'{sitepath}/'

        request = dict()
        # Получаем данные запроса POST или GET
        method = environment['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environment)
            request['data'] = data
            print(f'Поступил POST запрос {Framework.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environment)
            request['request_params'] = request_params
            print(f'Поступил GET запрос {Framework.decode_value(request_params)}')

        # Находим нужный контроллер
        if sitepath in self.sitemap:
            view = self.sitemap[sitepath]
        else:
            view = Page404()

        # Запускаем контроллер
        code, body = view(request)
        response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data: dict):
        new_dict = dict()
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_dict[k] = val_decode_str
        return new_dict


if __name__ == '__main__':
    print('Приложение запускается на базе wsgiref.simple_server')
    print('Для начала работы запустите "run.py"')
    exit(0)
