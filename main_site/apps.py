from django.apps import AppConfig
#глобальные настройки для приложения(main_site)

class MainSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_site'
