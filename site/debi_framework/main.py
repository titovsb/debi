from debi_framework.templator import render

ANSWER404 = '404 Not Found'

class Page404:
    def __call__(self):
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

        # Находим нужный контроллер
        if sitepath in self.sitemap:
            view = self.sitemap[sitepath]
        else:
            view = Page404()

        # Запускаем контроллер
        code, body = view()
        response(code, [('Content-Type','text/html')])
        return [body.encode('utf-8')]

if __name__ == '__main__':
    exit(0)
