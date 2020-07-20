"""Abstract Protocol for Valid Communication into HTTP"""

# Develop Vmgabriel

# Libraries
from abc import ABC, abstractmethod
from flask import Blueprint


class HttpProtocol(ABC):
    """Abstract Class for Http Protocol"""
    @abstractmethod
    def get_blueprint(self) -> Blueprint:
        """Get Blueprint data for Http protocol"""
