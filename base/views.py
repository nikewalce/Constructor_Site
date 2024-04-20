from django.shortcuts import render
from django.http import HttpResponse
#отвечает за те методы, которые будут вызваны при переходе пользователя на определенную страницу
#обязательно прописывать аргумент запроса(request)
def index(request):
    #render(request, 'директория с название приложения в templates HTML документ', словарь для передачи данных в шаблоны)

    return render(request, 'base/base_index.html')

def db(request):
    return HttpResponse('<h1>Проверка base/data </h1>')
