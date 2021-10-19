from debi_framework.templator import render

ANSWER200 = '200 OK'

class Index:
    def __call__(self,request):
        return ANSWER200, render('index.html')

class About:
    def __call__(self, request):
        return ANSWER200, 'ABOUT'
        # return ANSWER200, render('about.html', request)
