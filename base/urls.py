#этот файл нужно создавать самостоятельно

from django.urls import path
#из данной папки импортируем метод views
from . import views
#Тут отслеживают адресса
#При переходе на base/ запускаем метод views. Круглые скобки не нужны(если ставить их, то метод выполняется. А тут нужно обратиться только)
#'' срабатывает, когда переходят по base/
#<int:pk> - отслеживание динамической записи с типом int
urlpatterns = [
    path('', views.index, name='base'),
    path('data', views.db, name='db'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.BaseDetailView.as_view(), name='base_detail'),
    path('<int:pk>/update', views.BaseUpdateView.as_view(), name='base_update'),
    path('<int:pk>/delete', views.BaseDeleteView.as_view(), name='base_delete'),
]
