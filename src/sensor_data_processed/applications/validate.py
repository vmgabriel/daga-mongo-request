"""Module Definition for Sensor Data Process"""

# Develop: vmgabriel

# Libraries
from typing import List, Any

# Domains
from src.domain.models.validation_interface import Validate_Interface
from src.utils.validations.validation_handler import Validate_Handler

from src.sensor_data_processed.domain.sensor_data import SensorData


class SensorDataValidate(Validate_Interface[SensorData]):
    """Validation for Sensor Data Processed"""
    def __init__(self):
        self.v = Validate_Handler()
        self.not_verify = lambda x: True

    def validate_object(self, data: Any) -> (str, SensorData):
        """Create Validate Object"""
        datas = []
        datas.append(data['_id'] if ('_id' in data) else None)
        datas.append(data['tookTime'] if ('tookTime' in data) else None)
        datas.append(data['gas'] if ('gas' in data) else None)
        datas.append(data['carbon'] if ('carbon' in data) else None)
        datas.append(data['humedity'] if ('humedity' in data) else None)
        datas.append(data['temperature'] if ('temperature' in data) else None)
        datas.append(data['lightUV'] if ('lightUV' in data) else None)
        datas.append(
            data['soilMoisture'] if ('soilMoisture' in data) else None
        )
        datas.append(data['idReader'] if ('idReader' in data) else None)
        datas.append(data['nameReader'] if ('nameReader' in data) else None)
        datas.append(
            data['idController'] if ('idController' in data) else None
        )
        datas.append(
            data['nameController'] if ('nameController' in data) else None
        )
        for _ in range(10):
            datas.append(False)
        datas.append(data['createdAt'] if ('createdAt' in data) else None)
        datas.append(data['updatedAt'] if ('updatedAt' in data) else None)
        datas.append(data['deletedAt'] if ('deletedAt' in data) else None)

        message = ''
        if not self.not_verify(datas[1]):
            message = 'tookTime not valid'
        if not self.not_verify(datas[2]):
            message = 'gas not valid'
        if not self.not_verify(datas[3]):
            message = 'carbon not valid'
        if not self.not_verify(datas[4]):
            message = 'Humedity not valid'
        if not self.not_verify(datas[5]):
            message = 'temperature not valid'
        if not self.not_verify(datas[6]):
            message = 'lightUV not valid'
        if not self.not_verify(datas[7]):
            message = 'soilMoisture not valid'
        if not self.not_verify(datas[8]):
            message = 'idReader not valid'
        if not self.not_verify(datas[9]):
            message = 'nameReader not valid'
        if not self.not_verify(datas[10]):
            message = 'idController not valid'
        if not self.not_verify(datas[11]):
            message = 'nameController not valid'
        if not self.not_verify(datas[12]):
            message = 'created at not valid'
        if not self.not_verify(datas[13]):
            message = 'updated at not valid'

        if len(message) > 0:
            return (message, {})
        return ('done correctly', SensorData(*tuple(datas)))

    def validate_object_update(self, data: Any) -> (str, SensorData):
        """Validate Object Update"""
        datas = []
        datas.append(data['_id'] if ('_id' in data) else None)
        datas.append(data['tookTime'] if ('tookTime' in data) else None)
        datas.append(data['gas'] if ('gas' in data) else None)
        datas.append(data['carbon'] if ('carbon' in data) else None)
        datas.append(data['humedity'] if ('humedity' in data) else None)
        datas.append(data['temperature'] if ('temperature' in data) else None)
        datas.append(data['lightUV'] if ('lightUV' in data) else None)
        datas.append(
            data['soilMoisture'] if ('soilMoisture' in data) else None
        )
        datas.append(data['idReader'] if ('idReader' in data) else None)
        datas.append(data['nameReader'] if ('nameReader' in data) else None)
        datas.append(
            data['idController'] if ('idController' in data) else None
        )
        datas.append(
            data['nameController'] if ('nameController' in data) else None
        )
        for _ in range(10):
            datas.append(False)
        datas.append(data['createdAt'] if ('createdAt' in data) else None)
        datas.append(data['updatedAt'] if ('updatedAt' in data) else None)
        datas.append(data['deletedAt'] if ('deletedAt' in data) else None)

        message = ''
        if not self.not_verify(datas[1]):
            message = 'tookTime not valid'
        if not self.not_verify(datas[2]):
            message = 'gas not valid'
        if not self.not_verify(datas[3]):
            message = 'carbon not valid'
        if not self.not_verify(datas[4]):
            message = 'Humedity not valid'
        if not self.not_verify(datas[5]):
            message = 'temperature not valid'
        if not self.not_verify(datas[6]):
            message = 'lightUV not valid'
        if not self.not_verify(datas[7]):
            message = 'soilMoisture not valid'
        if not self.not_verify(datas[8]):
            message = 'idReader not valid'
        if not self.not_verify(datas[9]):
            message = 'nameReader not valid'
        if not self.not_verify(datas[10]):
            message = 'idController not valid'
        if not self.not_verify(datas[11]):
            message = 'nameController not valid'
        if not self.not_verify(datas[12]):
            message = 'created at not valid'
        if not self.not_verify(datas[13]):
            message = 'updated at not valid'

        if len(message) > 0:
            return (message, {})
        return ('done correctly', SensorData(*tuple(datas)))

    def data_filter_content(self, limit: int, offset: int) -> str:
        """Datta Filter Content Convertor"""
        return self.validation_base.data_filter_content(limit, offset)

    def data_order_content(self, order: List[str]) -> bool:
        """Data Order Content Convertor"""
        return self.validation_base.data_order_content(order)
