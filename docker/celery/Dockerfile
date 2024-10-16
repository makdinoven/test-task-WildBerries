# Используем образ Python 3.10
FROM python:3.10

# Указываем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями в контейнер
COPY ./app/requirements.txt /app/requirements.txt

# Устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Копируем весь проект в контейнер
COPY ./app /app

# Запускаем Celery worker
CMD ["celery", "-A", "wildberries", "worker", "--loglevel=info"]
