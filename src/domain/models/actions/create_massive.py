# Develop: Vmgabriel

# Libraries
from typing import TypeVar, Generic, List, Any
from abc import ABC, abstractmethod

T = TypeVar('T')

class CreateMassive(ABC, Generic[T]):
    @abstractmethod
    def execute(self, data: List[T]) -> (List[str], int):
        pass

    @abstractmethod
    def to_entity(self, data: T) -> Any:
        pass

    @abstractmethod
    def to_many_entities(self, data: List[T]) -> Any:
        pass

