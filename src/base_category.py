from abc import ABC
from abc import abstractmethod


class BaseCategory(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass
