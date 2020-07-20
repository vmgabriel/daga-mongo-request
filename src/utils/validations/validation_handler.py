# Develop: vmgabriel

"""Definition Module Functional for Validation Data"""

# Libraries
import re
import functools
from typing import List, Any

from src.config.server import configuration as conf


class Validate_Handler:
    """Validation Handler for all data input of infraestructure"""
    def __init__(self):
        pass

    def compose(self, *functions):
        """Compose functions, recursive way for solve problems."""
        return functools.reduce(
            lambda f, g: lambda x: f(g(x)),
            functions,
            lambda x: x
        )

    def compose_and(self, *functions):
        """Compose And Comparators"""
        def define(_x):
            compositor = True
            for func in functions:
                compositor = func(_x) and compositor
            return compositor
        return define

    def compose_or(self, *functions):
        """Compose Or Comparators"""
        def define(_x):
            compositor = False
            for func in functions:
                compositor = func(_x) or compositor
            return compositor
        return define

    def exist(self):
        """Verify if data exist"""
        return lambda x: x is not None if not isinstance(x, bool) else True

    def min(self, data: Any):
        """Return function for compare data min"""
        return lambda x: x > data if (isinstance(x, (int, float))) \
            else len(x) > data if x else False

    def max(self, data: Any):
        """Return function for compare data max"""
        return lambda x: x < data if (isinstance(x, (int, float))) \
            else len(x) < data if x else False

    def max_eq(self, data: Any):
        """Return function for compare data max or equal value"""
        return lambda x: x <= data if (isinstance(x, (int, float))) \
            else len(x) <= data if x else False

    def min_eq(self, data: Any):
        """Return function for compare data min or equal value"""
        return lambda x: x >= data if (isinstance(x, (int, float))) \
            else len(x) >= data if x else False

    def regex(self, data: str):
        """Return function for compare data for regex datas"""
        return lambda x: bool(re.search(data, x)) if (x) else False

    def max_data(self):
        """With the default max data"""
        return self.max(conf['limit_max'])

    def min_eq_data(self):
        """With Min Or Equal data verify data by default"""
        return self.min_eq(conf['limit_min'])

    def email(self):
        """Verify if data is email"""
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        return self.regex(regex)

    def url(self):
        """Url of data to Verify"""
        regex = '^http[s]?:\/\/[a-zA-Z0-9:]\S+.\w\S{2,}$'
        return self.regex(regex)

    def data_order_validate(self, data: str):
        """Order of data to verify"""
        if len(data[1:]) <= 1:
            return 'no valid order'
        return 'ok'

    def data_filter_content(self, limit: int, offset: int) -> str:
        """Filter data Content"""
        if self.compose(self.max_data, self.min_eq_data)(limit):
            return 'limit no valid'
        return 'ok'

    def data_order_content(self, order: List[str]) -> bool:
        """Filter Ordern data Content"""
        if len(order) == 1:
            return self.data_order_validate(order[0]) == 'ok'
        return self.data_order_validate(order[0]) == 'ok' and \
            self.data_order_content(order[1:])
