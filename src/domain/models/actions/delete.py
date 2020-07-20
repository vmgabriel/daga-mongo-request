"""Module Abstract for Delete Class"""

# Develop: Vmgabriel

# Libraries
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

_T = TypeVar('T')


class Delete(ABC, Generic[_T]):
    """Abstract Class for Delete Process into Database"""
    @abstractmethod
    def execute(
            self,
            idReader: int,
            idController: int,
            typeMeasure: str
    ) -> bool:
        """Define Execute process into database"""

    @abstractmethod
    def to_query(
            self,
            idReader: int,
            idController: int,
            typeMeasure: str
    ) -> str:
        """Convert to query a order"""
