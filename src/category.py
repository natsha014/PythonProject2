from typing import List
from typing import Optional

from src.product import Product


class Category:
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        sum_quantity = 0
        for product in self.__products:
            sum_quantity += product.quantity
        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_ret(self) -> list[Product]:
        return self.__products

    def add_product(self, products: Product) -> None:
        self.__products.append(products)
        Category.product_count += 1
