""" Module For Class Measure One Hour """

# Develop: vmgabriel

# Libraries
from datetime import datetime
from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class MeasureOneHour:
    """Measure for Control Data in One Hour"""
    _id: int
    took_time: datetime
    min: float
    max: float
    counter: int
    gr1: float
    gr2: float
    gr3: float
    gr4: float
    id_reader: int
    name_reader: str
    id_controller: int
    name_controller: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

    def __str__(self):
        """Convert to str - get data attributes"""
        _x = 'min,max,counter,gr1,gr2,gr3,gr4,idReader,nameReader,'
        _x += 'nameController,createdAt,updatedAt'
        return _x

    @staticmethod
    def define_type(type_val: str) -> str:
        """Define Type of each of name of the attributes of the class"""
        if type_val in ('min', 'max', 'gr1', 'gr2', 'gr3', 'gr4'):
            return 'float'
        return ''
