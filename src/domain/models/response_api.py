"""Module For Response Data"""

# Develop vmgabriel

# DataClass
from typing import Any, List
from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Response_Api:
    """Response Database"""
    code: int
    message: str
    error: str
    row: List[Any]
