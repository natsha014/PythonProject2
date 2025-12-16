from typing import List, Optional

from src.product import Product


class Category:
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]]=None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_ret(self) -> list[Product]:
        return self.__products

    def add_product(self, products: Product) -> None:
        self.__products.append(products)
        Category.product_count += 1
