from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import fetch_product_data
from .models import Product
from .serializers import ProductSerializer

@api_view(['POST'])
def fetch_product_view(request):
    nm_id = request.data.get('nm_id')
    if not nm_id:
        return Response({"error": "nm_id is required"}, status=400)

    # Запускаем задачу Celery
    fetch_product_data.delay(nm_id)

    return Response({"message": f"Task for fetching product {nm_id} has been started."})

@api_view(['GET'])
def list_products_view(request):
    # Получаем все товары из базы данных
    products = Product.objects.all()

    # Сериализуем данные
    serializer = ProductSerializer(products, many=True)

    # Возвращаем данные в виде JSON
    return Response(serializer.data)
