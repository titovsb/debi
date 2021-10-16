from debi_framework.templator import render

ANSWER200 = '200 OK'

class Index:
    def __call__(self):
        return ANSWER200, render('index.html')

class About:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    def __call__(self):
        return ANSWER200, render('about.html', **self.kwargs)
