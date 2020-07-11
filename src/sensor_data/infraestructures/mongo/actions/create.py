# Develop: vmgabriel

# Libraries
import inject
from typing import List, TypeVar, Generic, Any, Tuple

# Interfaces
from sensor_data.domain.sensor_data import SensorData
from domain.models.db_connection import Db_Connection
from domain.models.db.entity_conversor import Conversor_Type

# Validator for conver to Object
from sensor_data.applications.validate import SensorDataValidate

# Super Class
from domain.models.actions.create import Create

# Environment
from config.server import configuration as conf

class Create_SensorData(Create[SensorData]):
    def __init__(self, name_table: str, database: Db_Connection):
        self.name_table = name_table
        self.__database = database
        self.sensor_validate = SensorDataValidate()


    def execute(self, data: SensorData) -> SensorData:
        conn = self.__database.get_cursor()
        data_entity = data.to_dict()
        del data_entity["_id"]
        sensors_data = conn.sensorData
        sensor_new_id = sensors_data.insert_one(data_entity).inserted_id
        data_entity['_id'] = str(sensor_new_id)
        (_, sensor_new) = self.sensor_validate.validate_object(data_entity)
        return sensor_new

    def to_entity(self, data: SensorData) -> (str, str):
        return ('', '')

    def to_query(self, data: SensorData) -> str:
        return ''

