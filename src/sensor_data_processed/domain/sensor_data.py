"""Module for Sensor Data With data Process"""
# Develop: vmgbriel

from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class SensorData:
    """Sensor Data Class for Entity Sensor Data Processed"""
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
    isFive: bool
    isTen: bool
    isTwenty: bool
    isThirty: bool
    isHour: bool
    isTwoHour: bool
    isFiveHour: bool
    isDay: bool
    isFiveDay: bool
    isMonth: bool
    createdAt: datetime
    updatedAt: datetime
    deletedAt: datetime

    def __str__(self):
        _x = 'tookTime,gas,carbon,humedity,temperature,lightUV'
        _x += ',soilMoisture,idReader,nameReader,idController'
        _x += ',nameController,createdAt,updatedAt'
        return _x

    def define_type(self, type_val):
        """Define type of each of attributes based in name"""
        if type_val in ('gas', 'carbon', 'humedity',
                        'temperature', 'lightUV', 'soilMoisture'):
            return 'float'
        if type_val in ('createdAt', 'updatedAt', 'deletedAt', 'tookTime'):
            return 'datetime'
        if type_val in ('id', 'idReader', 'idController'):
            return 'int'
        if type_val in ('nameReader', 'nameController'):
            return 'str'
        if type_val in ('isFive', 'isTen', 'isTwenty', 'isThirty', 'isHour',
                        'isTwoHour', 'isFiveDay', 'isDay', 'isFiveDay',
                        'isMonth'):
            return 'bool'
        return ''

    def id_name(self):
        """Module for Id Name"""
        return 'id'

    def validation_name(self):
        """Module for Validation name"""
        return ''

    def delete_date_name(self):
        """Module for Delete Date Name"""
        return 'deletedAt'
