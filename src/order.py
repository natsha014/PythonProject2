from src.base_category import BaseCategory
from src.product import Product


class Order(BaseCategory):
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итого: {self.total_cost} руб."
