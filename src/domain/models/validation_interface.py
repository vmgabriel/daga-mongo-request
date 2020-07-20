"""Validate Entity Interface"""

# Develop vmgabriel

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any

_t = TypeVar('T')


class Validate_Interface(ABC, Generic[_t]):
    """Abstract Validation Interface"""

    @abstractmethod
    def validate_object(self, data: Any) -> (str, _t):
        """Definition for validate create object"""

    @abstractmethod
    def validate_object_update(self, data: Any) -> (str, _t):
        """Definition for validate update object"""
