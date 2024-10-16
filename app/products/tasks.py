from celery import shared_task
from .models import Product
from .services import get_product_data_from_wildberries, get_product_price_from_wildberries
import logging
import asyncio

# Настраиваем логирование
logger = logging.getLogger(__name__)


@shared_task
def fetch_product_data(nm_id):
    logger.info(f"Starting task for product {nm_id}")

    # Получаем основную информацию о товаре с использованием asyncio.run()
    data = asyncio.run(get_product_data_from_wildberries(nm_id))
    if data:
        logger.info(f"Product data received for {nm_id}: {data}")
    else:
        logger.error(f"Failed to fetch product data for {nm_id}")

    # Получаем информацию о самой последней цене товара с использованием asyncio.run()
    latest_price = asyncio.run(get_product_price_from_wildberries(nm_id))
    if latest_price is not None:
        logger.info(f"Latest price for product {nm_id}: {latest_price}")
    else:
        logger.error(f"Failed to fetch latest price for product {nm_id}")

    if data and latest_price is not None:
        # Извлекаем нужные данные из основного ответа
        product_data = {
            'nm_id': nm_id,
            'imt_name': data.get('imt_name', 'Без названия'),
            'description': data.get('description', 'Описание отсутствует'),
            'categories': data.get('subj_root_name', 'Категория отсутсвует'),
            'sub_categories': data.get('subj_name', 'Дочерняя категория отсутсвует'),
            'price': latest_price / 100
        }

        logger.info(f"Saving product data for {nm_id}: {product_data}")
        # Обновляем или создаем товар в базе данных
        product, created = Product.objects.update_or_create(nm_id=nm_id, defaults=product_data)

        if created:
            logger.info(f"New product created: {product}")
        else:
            logger.info(f"Product updated: {product}")

        return f"Product {nm_id} was successfully updated or created."
    else:
        logger.error(f"Failed to fetch complete data for product {nm_id}")
        return f"Failed to fetch data for product {nm_id}"
