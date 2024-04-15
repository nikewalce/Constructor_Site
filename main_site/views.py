from django.shortcuts import render
#метод для вызова текста
from django.http import HttpResponse
#отвечает за те методы, которые будут вызваны при переходе пользователя на определенную страницу
#обязательно прописывать аргумент запроса(request)
def index(request):
    return HttpResponse('<h1>Проверка</h1>')

def about(request):
    return HttpResponse('<h1>Проверка aboutt</h1>')
