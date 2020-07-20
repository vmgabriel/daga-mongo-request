# Develop: Vmgabriel

"""Module Abstract of Average"""

# Libraries
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

_T = TypeVar('T')


class Average(ABC, Generic[_T]):
    """Average Abstract Class"""
    @abstractmethod
    def execute(self, *datas) -> _T:
        """Execute Process average"""

    @abstractmethod
    def to_query(self, *datas) -> str:
        """to query data"""
