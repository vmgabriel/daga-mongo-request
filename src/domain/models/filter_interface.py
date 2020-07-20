"""Abstract Filter interface"""

# Develop: vmgabriel

# Develop vmgabriel

# DataClass
from typing import Any
from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Filter_Interface:
    """Filter Interface for Convert this in a query of database"""
    and_data: Any
    or_data: Any
    default: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Column_Filter:
    """Column Filter for Convert this in a query of database"""
    column: str
    op: str
    value: Any
    type_data: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Attribute_Filter:
    """Attribute Filter for Convert this in a query of database"""
    column: str
    as_name: str
