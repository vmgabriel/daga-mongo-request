"""Module for DB_Connection"""

# Develop vmgabriel

from abc import ABC, abstractmethod
from typing import Any


class Db_Connection(ABC):
    """Db Connector for use Into Databse"""
    @abstractmethod
    def get_connection(self) -> Any:
        """Get Connection Database"""

    @abstractmethod
    def get_cursor(self) -> Any:
        """Get Cursor of Database a valid pool of connection"""

    @abstractmethod
    def migrations(self) -> None:
        """Migrate into Definitions to database"""

    @abstractmethod
    def disconnect(self) -> None:
        """Disconnect the database"""

    @abstractmethod
    def connector(self) -> str:
        """Generate a Uri for connector"""
