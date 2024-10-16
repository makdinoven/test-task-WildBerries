from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'nm_id', 'brand', 'name', 'entity', 'review_rating',
            'feedbacks', 'basic_price', 'current_price', 'discount_percentage',
            'discount_amount', 'total_quantity'
        ]
