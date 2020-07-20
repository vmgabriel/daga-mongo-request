"""Module Abstract for Delete Class"""

# Develop: Vmgabriel

# Libraries
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

_T = TypeVar('T')


class Delete(ABC, Generic[_T]):
    """Abstract Class for Delete Process into Database"""
    @abstractmethod
    def execute(self, data: _T) -> _T:
        """Define Execute process into database"""

    @abstractmethod
    def to_query(self, data: _T, id: int) -> str:
        """Convert to query a order"""
