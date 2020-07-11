# Develop vmgabriel

from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Any

from domain.models.filter_interface import Attribute_Filter, Filter_Interface

T = TypeVar('T')

class Database_Interface(ABC, Generic[T]):

    @abstractmethod
    def create(self, data: T) -> T:
        pass

    @abstractmethod
    def create_massive(self, data: List[T]) -> List[str]:
        pass

    @abstractmethod
    def builder(self, definition: str) -> None:
        pass
