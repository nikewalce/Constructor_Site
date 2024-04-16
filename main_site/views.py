from django.shortcuts import render
#метод для вызова текста
#from django.http import HttpResponse

#отвечает за те методы, которые будут вызваны при переходе пользователя на определенную страницу
#обязательно прописывать аргумент запроса(request)
def index(request):
    #render(request, 'директория с название приложения в templates HTML документ')
    return render(request, 'main_site/index.html')

def about(request):
     return render(request, 'main_site/about.html')
# def about(request):
#     return HttpResponse('<h1>Проверка aboutt</h1>')
