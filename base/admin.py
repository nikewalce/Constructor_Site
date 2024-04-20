from django.contrib import admin
#импортируем название класса(таблицы БД) из models
from .models import Constructor

# Регистрациию модели(таблицы)
admin.site.register(Constructor)
