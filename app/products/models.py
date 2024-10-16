from django.db import models
from django.utils import timezone

class Product(models.Model):
    nm_id = models.BigIntegerField(primary_key=True, verbose_name="Артикул")
    brand = models.CharField(max_length=255, verbose_name="Бренд",null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Название товара")
    entity = models.CharField(max_length=255, verbose_name="Категория")
    review_rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Рейтинг")
    feedbacks = models.IntegerField(verbose_name="Количество отзывов")
    basic_price = models.IntegerField(verbose_name="Стандартная цена")
    current_price = models.IntegerField(verbose_name="Текущая цена",null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Процент скидки",null=True, blank=True)
    discount_amount = models.IntegerField(verbose_name="Размер скидки",null=True, blank=True)
    total_quantity = models.IntegerField(verbose_name="Остаток на складе")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время добавления")

    def __str__(self):
        return f"{self.name} ({self.nm_id})"
