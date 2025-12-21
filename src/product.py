class Product:
    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price: float, quantity):  # type: ignore
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        return self.__price * self.quantity + other.__price * other.quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if self.__price > value:
            answer = input("Если согласны понизить цену, введите y, если нет, введите n    ").lower()
            if answer == "y":
                self.__price = value
        else:
            self.__price = value

    @classmethod
    def new_product(
        cls, name: str, description: str, price: float, quantity: int, products: list["Product"]
    ) -> "Product":
        for product in products:
            if product.name == name:
                product.quantity += quantity
                if price > product.price:
                    product.price = price
                return product
        new_product = cls(name, description, price, quantity)
        products.append(new_product)
        return new_product
