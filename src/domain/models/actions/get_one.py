"""Abstract Module for Get One Data"""
# Develop: Vmgabriel

# Libraries
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

_T = TypeVar('T')


class Get_One(ABC, Generic[_T]):
    """Abstract Class for Get One Data into Database"""
    @abstractmethod
    def execute(self, id: int) -> _T:
        """Execute Process of get one into database"""

    @abstractmethod
    def to_query(self, data: int) -> str:
        """Convert to Query Data"""
