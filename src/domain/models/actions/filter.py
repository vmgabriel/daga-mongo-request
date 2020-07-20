"""Abstract Filter Module"""

# Develop: Vmgabriel

# Libraries
from typing import TypeVar, Generic, Any, List
from abc import ABC, abstractmethod

# Interfaces
from src.domain.models.filter_interface import Filter_Interface, Attribute_Filter, Column_Filter

_T = TypeVar('T')


class Filter(ABC, Generic[_T]):
    """Abstract Filter Class"""
    @abstractmethod
    def execute(
            self,
            filters: Filter_Interface,
            attributes: List[Attribute_Filter],
            joins: Any,
            limit: int,
            offset: int
    ) -> (List[_T], str):
        """Module for execute data filter and get this data of database"""

    @abstractmethod
    def convert_column(self, column_filter: Column_Filter) -> str:
        """Convert Data Column into Column"""

    @abstractmethod
    def convert_filter(self, filters: Filter_Interface) -> str:
        """Convert Filter Data into Filter Valid into Database"""

    @abstractmethod
    def convert_attributes(
            self,
            attributes: List[Attribute_Filter],
            is_count: bool = False
    ) -> str:
        """Convert attributes for Database"""

    @abstractmethod
    def convert_joins(self, joins: Any) -> str:
        """Convert Joins into a based in a based to database"""

    @abstractmethod
    def definitor(self) -> str:
        """Definitor Process query"""
