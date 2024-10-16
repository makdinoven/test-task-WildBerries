from django.urls import path
from .views import fetch_product_view, list_products_view

urlpatterns = [
    path('fetch-product/', fetch_product_view, name='fetch-product'),
    path('products/', list_products_view, name='list-products'),
]
