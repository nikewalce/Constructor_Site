from django.shortcuts import render
#метод для вызова текста
#from django.http import HttpResponse

#отвечает за те методы, которые будут вызваны при переходе пользователя на определенную страницу

#обязательно прописывать аргумент запроса(request)
def index(request):
    #render(request, 'директория с название приложения в templates HTML документ', словарь для передачи данных в шаблоны)
    data = {
        'title': 'Главная страница',
        'values': ['One', 'Two'],
        'obj':{
            '1': 1,
            '2': 'Twot',
            '3': ['1','2']
        }
    }
    return render(request, 'main_site/index.html', data)

def about(request):
     return render(request, 'main_site/about.html')
# def about(request):
#     return HttpResponse('<h1>Проверка aboutt</h1>')
