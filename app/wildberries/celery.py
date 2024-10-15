from __future__ import absolute_import
import os
from celery import Celery

# Устанавливаем переменные окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Используем настройки Django для конфигурации Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем задачи (tasks.py в приложениях)
app.autodiscover_tasks()
