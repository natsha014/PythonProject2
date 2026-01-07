from typing import Protocol


class SupportPrint(Protocol):
    name: str
    description: str
    price: float
    quantity: int


class PrintMixin:

    def __init__(self: SupportPrint) -> None:
        print(repr(self))

    def __repr__(self: SupportPrint) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
