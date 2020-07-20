"""Abstract Module for Gell All Data"""

# Develop: Vmgabriel

# Libraries
from typing import TypeVar, Generic, List
from abc import ABC, abstractmethod

# Interfaces
from src.domain.models.filter_interface import Filter_Interface

_T = TypeVar('T')


class Get_All(ABC, Generic[_T]):
    """Get All Data Process"""
    @abstractmethod
    def execute(
            self,
            limit: int,
            offset: int
    ) -> List[_T]:
        """Execute Process for to get Data"""
