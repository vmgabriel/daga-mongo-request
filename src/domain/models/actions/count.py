# Develop: Vmgabriel

"""Count Abstract Module"""

# Libraries
from abc import ABC, abstractmethod


class Count(ABC):
    """Count Class Abstract"""
    @abstractmethod
    def execute(self, query: str) -> int:
        """Execute Process"""
