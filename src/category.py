from typing import List
from typing import Optional

from src.base_category import BaseCategory
from src.my_exception import ZeroQuantityProduct
from src.product import Product


class Category(BaseCategory):
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        sum_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    @property
    def products_format(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products(self) -> list[Product]:
        return self.__products

    def add_product(self, products: Product) -> None:
        if isinstance(products, Product):
            try:
                if products.quantity == 0:
                    raise ZeroQuantityProduct
            except ZeroQuantityProduct as e:
                print(e)
            else:
                self.__products.append(products)
                Category.product_count += 1
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    def middle_price(self) -> float:
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
