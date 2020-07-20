"""Abstract Module for Update Process"""

# Develop: Vmgabriel

# Libraries
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

_T = TypeVar('T')


class Update(ABC, Generic[_T]):
    """Update Generic Abstract"""
    @abstractmethod
    def execute(self, id: int, data: _T) -> _T:
        """Execute Process update into database"""

    @abstractmethod
    def to_entity(self, data: _T) -> str:
        """Convert update to entity valid into database"""

    @abstractmethod
    def to_query(self, data: _T, id: int) -> str:
        """Convert to Query"""
