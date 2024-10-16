from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import fetch_product_data


class FetchProductDataView(APIView):
    def post(self, request):
        nm_id = request.data.get('nm_id')

        if nm_id:
            # Запускаем задачу Celery для получения данных о товаре
            fetch_product_data.delay(nm_id)
            return Response({"message": f"Task for fetching product {nm_id} has been started."},
                            status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"error": "nm_id is required."}, status=status.HTTP_400_BAD_REQUEST)
