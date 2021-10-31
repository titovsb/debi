from debi_framework.templator import render
from components.models import Engine

ANSWER200 = '200 OK'

site = Engine()

class Index:
    def __call__(self,request):
        return ANSWER200, render('index.html', objects_list=site.categoties)

class CourseList:
    def __call__(self, request):
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            return ANSWER200, render('course_list.html',
                                     objects_list=category.courses,
                                     name=category.name,
                                     id=category.id)
        except KeyError:
            return ANSWER200, 'Курс не может быть добавлен'

# Класс-контроллер создания курса
class CreateCourse:
    category_id = -1
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))
                course = site.create_course('video', name, category)
                site.courses.append(course)
            return ANSWER200, render('course_list.html',
                                     objects_list=category.courses,
                                     name=category.name,
                                     id=category.id)
        else:
            try:
                self.category_id = int(request['request_params']['id'])
                print(f'axx {request}')
                category = site.find_category_by_id(int(self.category_id))
                return ANSWER200, render('create_course.html',
                                         name=category.name,
                                         id=category.id)
            except KeyError:
                return ANSWER200, 'Категория не может быть добавлена'

class About:
    def __call__(self, request):
        return ANSWER200, 'ABOUT'
        # return ANSWER200, render('about.html', request)
