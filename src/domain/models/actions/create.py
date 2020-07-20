"""Module Abstract for Create"""

# Develop: Vmgabriel

# Libraries
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

_T = TypeVar('T')


class Create(ABC, Generic[_T]):
    """Abstract Class fro Create"""
    @abstractmethod
    def execute(self, data: _T) -> _T:
        """Execute order for create"""

    @abstractmethod
    def to_entity(self, data: _T) -> (str, str):
        """Convert to Entity DB a Object Class define"""

    @abstractmethod
    def to_query(self, data: _T) -> str:
        """Generate a New Query to save data"""
