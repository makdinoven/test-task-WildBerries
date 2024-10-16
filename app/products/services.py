import aiohttp
import asyncio
import logging

logger = logging.getLogger(__name__)


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
        except Exception as e:
            logger.error(f"Error fetching data from {url}: {e}")
    return None

async def get_product_data_from_wildberries(nm_id):
    tasks = []

    # Перебираем возможные варианты серверов от basket-01 до basket-20
    for i in range(1, 21):
        server_number = f"{i:02d}"  # Форматируем числа от 1 до 9 как 01, 02 и т.д.

        # Перебираем варианты с 3 и 4 цифрами после /vol
        for vol_size in [4, 3]:
            vol_part = nm_id[:vol_size]  # Извлекаем нужное количество символов для vol

            # Перебираем варианты с 6 и 7 цифрами после /part
            for part_size in [6, 7]:
                part_part = nm_id[:part_size]  # Извлекаем нужное количество символов для part

                url = f"https://basket-{server_number}.wbbasket.ru/vol{vol_part}/part{part_part}/{nm_id}/info/ru/card.json"
                logger.info(f"Adding URL to tasks: {url}")
                tasks.append(fetch_data(url))  # Добавляем задачу для выполнения

    # Асинхронно выполняем все запросы
    results = await asyncio.gather(*tasks)

    # Вернем первый успешный результат
    for result in results:
        if result is not None:
            logger.info(f"Data found: {result}")
            return result

    logger.error(f"Failed to fetch product data for {nm_id} after trying all server and vol/part combinations")
    return None

# Функция для вызова асинхронного кода из синхронного контекста
def get_product_data(nm_id):
    return asyncio.run(get_product_data_from_wildberries(nm_id))


async def fetch_price(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data and isinstance(data, list):
                        latest_price_info = data[-1]  # Последний элемент списка
                        latest_price = latest_price_info['price'].get('RUB', 0)  # Извлекаем цену в рублях
                        return latest_price
        except Exception as e:
            logger.error(f"Error fetching price from {url}: {e}")
    return None


async def get_product_price_from_wildberries(nm_id):
    tasks = []

    # Перебираем возможные варианты серверов от basket-01 до basket-20
    for i in range(1, 21):
        server_number = f"{i:02d}"  # Форматируем числа от 1 до 9 как 01, 02 и т.д.

        # Перебираем варианты с 3 и 4 цифрами после /vol
        for vol_size in [4, 3]:
            vol_part = nm_id[:vol_size]  # Извлекаем нужное количество символов для vol

            # Перебираем варианты с 6 и 7 цифрами после /part
            for part_size in [6, 7]:
                part_part = nm_id[:part_size]  # Извлекаем нужное количество символов для part

                url = f"https://basket-{server_number}.wbbasket.ru/vol{vol_part}/part{part_part}/{nm_id}/info/price-history.json"
                logger.info(f"Adding URL to tasks: {url}")
                tasks.append(fetch_price(url))  # Добавляем задачу для выполнения

    # Асинхронно выполняем все запросы
    results = await asyncio.gather(*tasks)

    # Вернем первую успешную цену
    for result in results:
        if result is not None:
            logger.info(f"Found price: {result}")
            return result

    logger.error(f"Failed to fetch price for {nm_id} after trying all server and vol/part combinations")
    return None


# Функция для вызова асинхронного кода из обычной функции
def get_product_price(nm_id):
    return asyncio.run(get_product_price_from_wildberries(nm_id))
