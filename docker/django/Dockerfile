# Используем образ Python 3.10
FROM python:3.10

# Указываем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями в контейнер
COPY ./app/requirements.txt /app/requirements.txt

# Устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Копируем все файлы проекта в контейнер
COPY ./app /app

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

# Команда по умолчанию для контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
