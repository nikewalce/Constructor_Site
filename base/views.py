from django.shortcuts import render, redirect
from django.http import HttpResponse
#Импортируем модель(Таблицу БД)
from .models import Constructor
#Импортируем обработчик формы
from .forms import ConstructorForm

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

def create(request):
    error=''
    if request.method == 'POST':
        #Создание объекта с полученными данными из формы
        form = ConstructorForm(request.POST)
        #Если данные из формы введены верно, тогда сохраняем
        if form.is_valid():
            form.save()
            #После сохранения делаем переадресацию на страницу base
            return redirect('base')
        else:
            error='Форма введена неверно'

    form = ConstructorForm()

    data={
        'form': form,
        'error':error,
    }
    return render(request, 'base/create.html', data)
