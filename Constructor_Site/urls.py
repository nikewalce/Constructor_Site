"""
URL configuration for Constructor_Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#подключаем include, чтобы работать с приложениями
from django.contrib import admin
from django.urls import path, include
#копируем для статических файлов https://docs.djangoproject.com/en/5.0/howto/static-files/
from django.conf import settings
from django.conf.urls.static import static

#Тут отслеживают адресса
#при переходе по адресу admin/ будет открываться панель администратора admin.site.urls
#при переходе по адрессу '' (главная страница) переходим в main_site(передаем работу этому приложению)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_site.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
