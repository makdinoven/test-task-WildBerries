from django.urls import path
from .views import FetchProductDataView

urlpatterns = [
    path('fetch-product/', FetchProductDataView.as_view(), name='fetch-product'),
]
