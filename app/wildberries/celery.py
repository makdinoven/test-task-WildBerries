from __future__ import absolute_import
import os
from celery import Celery

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wildberries.settings')

# Создаем приложение Celery
app = Celery('wildberries')

# Загружаем настройки из файла настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим задачи в приложениях Django
app.autodiscover_tasks()
