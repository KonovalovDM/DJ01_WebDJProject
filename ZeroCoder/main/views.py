from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1>Это действительно мой первый проект на Django!!!</h1>")

def new(request):
    return HttpResponse("<h1>А это уже вторая страница моего первого проекта на Django!!!</h1>")

def data(request):
    return HttpResponse("<h1>Эта страница организована специально для размещения важных данных.</h1>")

def test(request):
    return HttpResponse("<h1>А эта страница организована для вывода результатов тестирования проекта.</h1>")