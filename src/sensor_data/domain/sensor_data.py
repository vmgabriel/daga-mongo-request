"""Module of SensorData"""

# Develop: vmgabriel

from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class SensorData:
    """Definition of SensorData"""
    _id: int
    tookTime: datetime
    gas: float
    carbon: float
    humedity: float
    temperature: float
    lightUV: float
    soilMoisture: float
    idReader: int
    nameReader: str
    idController: int
    nameController: str
    createdAt: datetime
    updatedAt: datetime
    deletedAt: datetime

    def __str__(self):
        """Get name of Attributes"""
        _x = 'tookTime,gas,carbon,humedity,temperature,lightUV'
        _x += ',soilMoisture,idReader,nameReader,idController'
        _x += ',nameController,createdAt,updatedAt'
        return _x

    @staticmethod
    def define_type(type_val):
        """Define Types"""
        if type_val in (
                'gas', 'carbon', 'humedity',
                'temperature', 'lightUV', 'soilMoisture'
        ):
            return 'float'
        if type_val in ('createdAt', 'updatedAt', 'deletedAt', 'tookTime'):
            return 'datetime'
        if type_val in ('id', 'idReader', 'idController'):
            return 'int'
        if type_val in ('nameReader', 'nameController'):
            return 'str'
        return ''

    @staticmethod
    def id_name():
        """Get Id Name of Entity"""
        return 'id'

    @staticmethod
    def validation_name():
        """Get Validation Name of Entity"""
        return ''

    @staticmethod
    def delete_date_name():
        """Get name attribute of Date Delete At"""
        return 'deletedAt'
