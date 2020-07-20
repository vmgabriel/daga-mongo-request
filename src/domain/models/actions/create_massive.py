"""Module for Create Massive"""

# Develop: Vmgabriel

# Libraries
from typing import TypeVar, Generic, List, Any
from abc import ABC, abstractmethod

_T = TypeVar('T')


class CreateMassive(ABC, Generic[_T]):
    """Abstract Class for Create Massive"""
    @abstractmethod
    def execute(self, data: List[_T]) -> (List[str], int):
        """Execute the order into database"""

    @abstractmethod
    def to_entity(self, data: _T) -> Any:
        """Convert to entity a data"""

    @abstractmethod
    def to_many_entities(self, data: List[_T]) -> Any:
        """Converto to entities varioous objects"""
