# Develi

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
        """Convert to str - get data attributes"""
        x  = 'tookTime,min,max,counter,gr1,gr2,gr3,gr4,idReader,nameReader'
        x += ',idController,nameController,createdAt,updatedAt'
        return x


    def define_type(self, type_val: str) -> str:
        """Define Type of each of name of attribute"""
        if (
                type_val == 'min' or
                type_val == 'max' or
                type_val == 'gr1' or
                type_val == 'gr2' or
                type_val == 'gr3' or
                type_val == 'gr4'
        ):
            return 'float'
        if (
                type_val == 'createdAt' or
                type_val == 'updatedAt' or
                type_val == 'deletedAt' or
                type_val == 'tookTime'
        ):
            return 'datetime'
        if (
                type_val == '_id' or
                type_val == 'idReader' or
                type_val == 'idController' or
                type_val == 'counter'
        ):
            return 'int'
        if (
                type_val == 'nameReader' or
                type_val == 'nameController'
        ):
            return 'str'
        return ''


    def id_name(self) -> str:
        """Return the name of id table(scheme/struct)"""
        return '_id'


    def validation_name(self) -> str:
        """Return the name of attribute of state"""
        return ''


    def delete_date_name(self) -> str:
        """Return the name of attribute of date Delete"""
        return 'deletedAt'

