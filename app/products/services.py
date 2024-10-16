import requests
import logging

logger = logging.getLogger(__name__)

def get_product_data_from_wildberries(nm_id):
    url = f"https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1257786&spp=30&ab_testing=false&nm={nm_id}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "products" in data["data"]:
                product_data = data["data"]["products"][0]

                # Извлекаем нужные данные
                id = product_data["id"]
                brand = product_data["brand"]
                name = product_data["name"]
                entity = product_data["entity"]
                review_rating = product_data["reviewRating"]
                feedbacks = product_data["feedbacks"]
                basic_price = product_data["sizes"][0]["price"]["basic"] / 100
                current_price = product_data["sizes"][0]["price"]["total"] / 100
                discount_amount = basic_price - current_price
                discount_percentage = (discount_amount / basic_price) * 100
                total_quantity = product_data["totalQuantity"]

                # Возвращаем данные
                return {
                    "nm_id": id,
                    "brand": brand,
                    "name": name,
                    "entity": entity,
                    "review_rating": review_rating,
                    "feedbacks": feedbacks,
                    "basic_price": basic_price,
                    "current_price": current_price,
                    "discount_percentage": discount_percentage,
                    "discount_amount": discount_amount,
                    "total_quantity": total_quantity,
                }
        else:
            logger.error(f"Failed to fetch product data for {nm_id}, status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching product data for {nm_id}: {e}")
        return None
