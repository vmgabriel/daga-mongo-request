# Develi

from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class SensorData:
    _id: int
    tookTime: datetime
    gas: float
    carbon: float
    humedity: float
    temperature: float
    lightUV: float
    soilMoisture: float
    createdAt: datetime
    updatedAt: datetime
    deletedAt: datetime

    def __str__(self):
        x = 'tookTime,gas,carbon,humedity,temperature,lightUV'
        x += ',soilMoisture,createdAt,updatedAt'
        return x

    def define_type(self, type_val):
        if (
                type_val == 'gas' or
                type_val == 'carbon' or
                type_val == 'humedity' or
                type_val == 'temperature' or
                type_val == 'lightUV' or
                type_val == 'soilMoisture'
        ):
            return 'float'
        if (
                type_val == 'createdAt' or
                type_val == 'updatedAt' or
                type_val == 'deletedAt' or
                type_val == 'tookTime'
        ):
            return 'datetime'
        if (type_val == 'id'):
            return 'int'
        return ''

    def id_name(self):
        return 'id'

    def validation_name(self):
        return ''

    def delete_date_name(self):
        return 'deletedAt'
