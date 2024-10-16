from celery import shared_task
from .models import Product
from .services import get_product_data_from_wildberries
import logging

logger = logging.getLogger(__name__)


@shared_task
def fetch_product_data(nm_id):
    logger.info(f"Starting task for product {nm_id}")

    # Получаем данные о товаре
    data = get_product_data_from_wildberries(nm_id)
    if data:
        logger.info(f"Product data received for {nm_id}: {data}")

        # Обновляем или создаем запись о товаре в базе данных
        product, created = Product.objects.update_or_create(
            nm_id=nm_id,
            defaults={
                'brand': data['brand'],
                'name': data['name'],
                'entity': data['entity'],
                'review_rating': data['review_rating'],
                'feedbacks': data['feedbacks'],
                'basic_price': data['basic_price'],
                'current_price': data['current_price'],
                'discount_percentage': data['discount_percentage'],
                'discount_amount': data['discount_amount'],
                'total_quantity': data['total_quantity']
            }
        )

        if created:
            logger.info(f"New product created: {product}")
        else:
            logger.info(f"Product updated: {product}")

        return f"Product {nm_id} was successfully updated or created."
    else:
        logger.error(f"Failed to fetch complete data for product {nm_id}")
        return f"Failed to fetch data for product {nm_id}"
