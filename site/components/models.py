import quopri


# Абстрактный класс пользователя
class User:
    pass


class Student(User):
    pass


class Teacher(User):
    pass


class UserFactory:
    types = {'student': Student,
             'teacher': Teacher
             }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


class Course:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)


class InteractiveCourse(Course):
    pass


class VideoCourse(Course):
    pass


class CourseFactory:
    types = {'interactive': InteractiveCourse,
             'video': VideoCourse}

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = list()

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


class Engine:
    def __init__(self):
        self.teachers = list()
        self.students = list()
        self.courses = list()
        self.categoties = list()

    @staticmethod
    def create_user(type_):
        return UserFactory.create(type_)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category_by_id(self, id):
        for item in self.categoties:
            print(f'item.id={item.id}')
            if item.id == id:
                return item
        raise Exception(f'Категория id={id} отсутствует')

    @staticmethod
    def create_course(type_, name, category):
        return CourseFactory.create(type_, name, category)

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return None

    @staticmethod
    def decode_value(val):
        tmp = bytes(val.replace('%','=').replace('+',' '), 'UTF-8')
        val_decode = quopri.decodestring(tmp)
        return val_decode.decode('UTF-8')

