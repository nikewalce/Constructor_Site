from django.shortcuts import render
from django.http import HttpResponse
#Импортируем модель(Таблицу БД)
from .models import Constructor

#отвечает за те методы, которые будут вызваны при переходе пользователя на определенную страницу
#обязательно прописывать аргумент запроса(request)
def index(request):
    #render(request, 'директория с название приложения в templates HTML документ', словарь для передачи данных в шаблоны)

    #Получаю все объекты из таблицы Constructor, передаем в render
    all_object = Constructor.objects.all()

    # #сортировка по title(в обратном порядке -title). можно выбрать кол-во записей: ('title')[:1]
    # all_object = Constructor.objects.order_by('title')

    return render(request, 'base/base_index.html', {'all_object': all_object})

def db(request):
    return HttpResponse('<h1>Проверка base/data </h1>')

