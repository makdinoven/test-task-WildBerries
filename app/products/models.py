from django.db import models

class Product(models.Model):
    nm_id = models.CharField(max_length=50, unique=True, verbose_name="Артикул товара")
    imt_name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Цена товара")
    categories = models.CharField(max_length=50,verbose_name="Категория",null=True)
    sub_categories = models.CharField(max_length=50,verbose_name="Дочерняя категория",null=True)

    def __str__(self):
        return self.imt_name
