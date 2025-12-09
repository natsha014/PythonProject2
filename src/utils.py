import json
from pathlib import Path

from src.category import Category
from src.product import Product


def read_json(path: Path) -> list[dict]:
    """
    Чтение json файла
    """
    with open(path, "r", encoding="utf=8") as f:
        result = json.load(f)
    return result  # type: ignore


def create_objects(load_json: list[dict]) -> list[Category]:
    """
    Подгрузка данных по категориям и товарам из файла JSON
    """
    categories = []
    for category in load_json:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
