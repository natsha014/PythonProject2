from src.base_category import BaseCategory
from src.my_exception import ZeroQuantityProduct
from src.product import Product


class Order(BaseCategory):
    def __init__(self, product: Product, quantity: int):
        try:
            if quantity == 0:
                raise ZeroQuantityProduct()
        except ZeroQuantityProduct as e:
            print(e)
            raise
        else:
            self.product = product
            self.quantity = quantity
            self.total_cost = product.price * quantity
            print("Товар успешно добавлен в заказ")
        finally:
            print("Обработка добавления товара завершена")

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итого: {self.total_cost} руб."
