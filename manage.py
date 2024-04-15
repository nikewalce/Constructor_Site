#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#cd Constructor_Site
#python manage.py runserver   ctrl + c завершить - запустить локальный сервер
#python manage.py startapp название приложения - создать приложение
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Constructor_Site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
