# Develop: vmgabriel

# Libraries
import inject
from typing import List, TypeVar, Generic, Any, Tuple

# Interfaces
from sensor_data_processed.domain.sensor_data import SensorData
from domain.models.db_connection import Db_Connection
from domain.models.db.entity_conversor import Conversor_Type

# Validator for conver to Object
from sensor_data_processed.applications.validate import SensorDataValidate

# Super Class
from domain.models.actions.create import Create

# Environment
from config.server import configuration as conf

class Create_SensorData(Create[SensorData]):
    def __init__(self, name_table: str, database: Db_Connection):
        self.name_table = name_table
        self.__database = database
        self.sensor_validate = SensorDataValidate()

        self.counter = 2.5
        self.add_counter = 2.5

    def data_sensor_time(self, data: SensorData) -> SensorData:
        self.counter += self.add_counter
        five_step = 5
        ten_step = 10
        twenty_step = 20
        thirty_step = 30
        hour_step = 60
        two_hour_step = 120
        five_hour_step = 300
        one_day_step = 1440
        five_day_step = 7200
        month_step = 43200
        if (self.counter % five_step == 0):
            data.isFive = True
        if (self.counter % ten_step == 0):
            data.isTen = True
        if (self.counter % twenty_step == 0):
            data.isTwenty = True
        if (self.counter % thirty_step == 0):
            data.isThirty = True
        if (self.counter % hour_step == 0):
            data.isHour = True
        if (self.counter % two_hour_step == 0):
            data.isTwoHour = True
        if (self.counter % five_hour_step == 0):
            data.isFiveHour = True
        if (self.counter % one_day_step == 0):
            data.isDay = True
        if (self.counter % five_day_step == 0):
            data.isFiveDay = True
        if (self.counter % month_step == 0):
            data.isMonth = True
            self.counter = self.add_counter
        return data


    def execute(self, data: SensorData) -> SensorData:
        conn = self.__database.get_cursor()
        data_with_sensor = self.data_sensor_time(data)
        data_entity = data_with_sensor.to_dict()
        del data_entity["_id"]
        sensors_data = conn.sensorProcessed
        sensor_new_id = sensors_data.insert_one(data_entity).inserted_id
        data_entity['_id'] = str(sensor_new_id)
        (_, sensor_new) = self.sensor_validate.validate_object(data_entity)
        return sensor_new

    def to_entity(self, data: SensorData) -> (str, str):
        return ('', '')

    def to_query(self, data: SensorData) -> str:
        return ''

