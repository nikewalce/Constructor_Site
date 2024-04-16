#этот файл нужно создавать самостоятельно

from django.urls import path
#из данной папки импортируем метод views
from . import views
#Тут отслеживают адресса
#При переходе на главную страницу запускаем метод views. Круглые скобки не нужны(если ставить их, то метод выполняется. А тут нужно обратиться только)
#При переходе на about обращаемся к функции about метода views
urlpatterns = [
    path('', views.index, name='home'),
    path('about123', views.about, name='about')
]
