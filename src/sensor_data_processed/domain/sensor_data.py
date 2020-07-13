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
        x = 'tookTime,gas,carbon,humedity,temperature,lightUV'
        x += ',soilMoisture,idReader,nameReader,idController'
        x+= ',nameController,createdAt,updatedAt'
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
        if (
                type_val == 'id' or
                type_val == 'idReader' or
                type_val == 'idController'
        ):
            return 'int'
        if (
                type_val == 'nameReader' or
                type_val == 'nameController'
        ):
            return 'str'
        if (
                type_val == 'isFive' or
                type_val == 'isTen' or
                type_val == 'isTwenty' or
                type_val == 'isThirty' or
                type_val == 'isHour' or
                type_val == 'isTwoHour' or
                type_val == 'isFiveHour' or
                type_val == 'isDay' or
                type_val == 'isFiveDay' or
                type_val == 'isMonth'
        ):
            return 'bool'
        return ''


    def id_name(self):
        return 'id'


    def validation_name(self):
        return ''


    def delete_date_name(self):
        return 'deletedAt'
