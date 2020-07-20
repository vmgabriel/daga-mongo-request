"""Module For Entity Conversor"""

# Develop: vmgabriel

# Libraries
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List, TypeVar, Any

_T = TypeVar('T')


class Conversor_Type(ABC):
    """Abstract Convert Type of Database"""
    @abstractmethod
    def str_to(self, data: str) -> str:
        """Convert data str to a valid attribute of database"""

    @abstractmethod
    def int_to(self, data: int) -> str:
        """Convert data int to a valid attribute of database"""

    @abstractmethod
    def float_to(self, data: float) -> str:
        """Convert data float to a valid attribute of database"""

    @abstractmethod
    def datetime_to(self, data: datetime) -> str:
        """Convert data datetime to a valid attribute of database"""

    @abstractmethod
    def bool_to(self, data: bool) -> str:
        """Convert data bool to a valid attribute of database"""

    @abstractmethod
    def list_to(self, data: List[Any]) -> str:
        """Convert data list to a valid attribute of database"""

    @abstractmethod
    def keyword_to(self, data: str) -> str:
        """Convert data keyword to a valid attribute of database"""

    @abstractmethod
    def to_entity(self, type_str: str, data: Any) -> str:
        """Having type and data get data valid"""
