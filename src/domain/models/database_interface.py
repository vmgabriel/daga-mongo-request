"""Database Interface for Data"""

# Develop vmgabriel

from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

_T = TypeVar('T')


class Database_Interface(ABC, Generic[_T]):
    """Database Interface Basic"""
    @abstractmethod
    def create(self, data: _T) -> _T:
        """Create Fachade for any database"""

    @abstractmethod
    def create_massive(self, data: List[_T]) -> List[str]:
        """Create Massive Fachade for any database"""

    @abstractmethod
    def builder(self, definition: str, other_definition: str = '') -> None:
        """With a valid name of database in configuration this
        build the class for valid database"""
