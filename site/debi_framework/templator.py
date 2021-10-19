from os.path import join
from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment


def render(filename, home='templates', **kwargs):
    '''
    Рендеринг шаблона по адресу home+filename
    :param filename: имя шаблона
    :param home: папка, где ищем шаблон
    :param kwargs: параметры передаваемые в метод Template.render
    :return: результат который должны передать на сервер
    '''
    # вариант для единичного рендеринга страниц
    # fullpath = join(home, filename)
    # with open(fullpath, encoding='utf-8') as f:
    #     template = Template(f.read())

    # подключаем наследование шаблонов из папки
    env = Environment()
    print(f'HOME={home}')
    env.loader = FileSystemLoader(home)
    template = env.get_template(filename)
    return template.render(**kwargs)

if __name__ == '__main__':
    print('Приложение запускается на базе wsgiref.simple_server')
    print('Для начала работы запустите "run.py"')
    exit(0)
