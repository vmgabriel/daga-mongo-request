# Develop: vmgabriel

"""Module for sqlite type"""

# Libraries
from typing import List, Any
from datetime import datetime

# Interface
from src.domain.models.db.entity_conversor import Conversor_Type

# Configurations
from src.config.server import configuration as conf


class SQLiteType(Conversor_Type):
    """SQlite Class for Convert Data"""
    def __init__(self):
        self.format_datetime = '%Y-%m-%d %H:%M:%S'

    def str_to(self, data: str) -> str:
        """Convert to Str"""
        return "'{}'".format(data)

    def int_to(self, data: int) -> str:
        """Convert to Int"""
        return "{}".format(data)

    def float_to(self, data: float) -> str:
        """Convert to Float"""
        return "{}".format(data)

    def datetime_to(self, data: datetime.date) -> str:
        """Convert to Datetime"""
        return "'{}'".format(data.strftime(self.format_datetime))

    def bool_to(self, data: bool) -> str:
        """Convert to bool"""
        return "{}".format('TRUE' if (data) else 'FALSE')

    def list_to(self, data: List[Any]) -> str:
        """Convert to List"""
        return str(data)

    def keyword_to(self, data: str) -> str:
        """Convert to Keyboard"""
        return '{}'.format(data)

    def to_entity(self, type_str: str, data: Any) -> str:
        """Take type and convert data"""
        if type_str == 'str':
            return self.str_to(data)
        if type_str == 'float':
            return self.float_to(data)
        if type_str == 'int':
            return self.int_to(data)
        if type_str == 'datetime':
            return self.datetime_to(data)
        if type_str == 'bool':
            return self.bool_to(data)
        if type_str == 'list':
            return self.list_to(data)
        if type_str == 'keyword':
            return self.keyword_to(data)
        return ''
