# Wildberries Product Fetcher API

Этот проект предназначен для получения информации о товарах с Wildberries через артикул товара и сохранения этих данных в базе данных. Он использует Django, Django REST Framework, Celery и PostgreSQL для реализации API, асинхронных задач и хранения данных.

## Установка и запуск
### 1. Клонирование репозитория

```bash
git clone git@github.com:makdinoven/test-task-WildBerries.git
cd wildberries-product-fetcher
```
### 2.Запуск приложения через Docker compose 
```bash
docker-compose up --build -d
```

### 3.Миграции
```bash
docker-compose exec app python manage.py makemigrations 
docker-compose exec app python manage.py migrate
```

## API Эндпоинты
### 1. Добавление товара по артикулу
    URL: /fetch-product
    Метод: POST
Пример запроса, где 219496815 - артикул товара:
```bash
curl -X POST http://localhost:8000/api/fetch-product/ -d '{"nm_id": "219496815"}' -H "Content-Type: application/json"
```
### 2. Вывод всех товаров
    URL: /products
    Метод: GET
Запрос:
```bash
curl -X GET http://localhost:8000/api/products/
```