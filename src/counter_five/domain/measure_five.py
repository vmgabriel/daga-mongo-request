"""Measure Five"""

# Libraries
from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class MeasureFive:
    """Measure for Control of Data"""
    _id: int
    tookTime: datetime
    min: float
    max: float
    counter: int
    gr1: float
    gr2: float
    gr3: float
    gr4: float
    idReader: int
    nameReader: str
    idController: int
    nameController: str
    createdAt: datetime
    updatedAt: datetime
    deletedAt: datetime

    def __str__(self):
        """Convert to str get data attributes"""
        _x = 'min,max,counter,gr1,gr2,gr3,gr4,idReader,nameReader,'
        _x += 'idController,nameController,typeMeasure'
        return _x

    @staticmethod
    def define_type(type_val: str) -> str:
        """Define Type of each of name of attribute"""
        if type_val in ('min', 'max', 'gr1', 'gr2', 'gr3', 'gr4'):
            return 'float'
        if type_val in ('createdAt', 'updatedAt', 'deletedAt', 'tookTime'):
            return 'datetime'
        if type_val in ('_id', 'idReader', 'idController', 'counter'):
            return 'int'
        if type_val in ('nameReader', 'nameController', 'typeMeasure'):
            return 'str'
        return ''

    @staticmethod
    def id_name() -> str:
        """Return the name of id table(scheme/struct)"""
        return 'id'

    @staticmethod
    def validation_name() -> str:
        """Return the name of attribute of state"""
        return ''

    @staticmethod
    def delete_date_name() -> str:
        """Return the name of attribute of date Delete"""
        return 'deletedAt'
