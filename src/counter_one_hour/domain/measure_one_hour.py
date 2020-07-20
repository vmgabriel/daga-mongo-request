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
        data = ''
        if type_val in ('min', 'max', 'gr1', 'gr2', 'gr3', 'gr4'):
            data = 'float'
        if type_val in ('took_time', 'created_at', 'updated_at', 'deleted_at'):
            data = 'datetime'
        if type_val in ('counter', 'id_reader', 'id_controller'):
            data = 'int'
        if type_val in ('name_reader', 'name_controller'):
            data = 'str'
        return data

    @staticmethod
    def id_name() -> str:
        """Return the name of id table(scheme/struct)"""
        return '_id'

    @staticmethod
    def validation_name() -> str:
        """Return the name of attribute of state"""
        return ''

    @staticmethod
    def delete_date_name() -> str:
        """Return the name of attribute of date Delete"""
        return 'deletedAt'
