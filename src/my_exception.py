class ZeroQuantityProduct(ValueError):
    def __init__(self, message: str="Добавлен товар с нулевым количеством") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
