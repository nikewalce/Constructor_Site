#этот файл нужно создавать самостоятельно

from django.urls import path
#из данной папки импортируем метод views
from . import views
#Тут отслеживают адресса
#При переходе на base/ запускаем метод views. Круглые скобки не нужны(если ставить их, то метод выполняется. А тут нужно обратиться только)
#'' срабатывает, когда переходят по base/
urlpatterns = [
    path('', views.index, name='home'),
    path('data', views.db, name='db')
]
