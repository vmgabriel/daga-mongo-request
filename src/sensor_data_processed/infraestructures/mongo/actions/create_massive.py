# Develop: vmgabriel

"""Create Massive Module for Mongo"""

# Libraries
from typing import List, Any

# Interfaces
from src.sensor_data_processed.domain.sensor_data import SensorData

from src.domain.models.db_connection import Db_Connection

# Super Class
from src.domain.models.actions.create_massive import CreateMassive


class CreateMassive_SensorData(CreateMassive[SensorData]):
    """Create massive class Sensor Data Processed Into Database Mongo"""
    def __init__(self, name_table: str, connection: Db_Connection):
        self.name_table = name_table
        self.connection = connection

        self.counter = 2.5
        self.add_counter = 2.5

    def data_sensor_time(self, data: SensorData) -> dict:
        """Data Sensor Time Validate"""
        self.counter += self.add_counter
        definition = data.to_dict()
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

        definition['isFive'] = self.counter % five_step == 0
        definition['isTen'] = self.counter % ten_step == 0
        definition['isTwenty'] = self.counter % twenty_step == 0
        definition['isThirty'] = self.counter % thirty_step == 0
        definition['isHour'] = self.counter % hour_step == 0
        definition['isTwoHour'] = self.counter % two_hour_step == 0
        definition['isFiveHour'] = self.counter % five_hour_step == 0
        definition['isDay'] = self.counter % one_day_step == 0
        definition['isFiveDay'] = self.counter % five_day_step == 0
        definition['isMonth'] = self.counter % month_step == 0
        if self.counter % month_step == 0:
            self.counter = self.add_counter
        return definition

    def execute(self, data: List[SensorData]) -> (List[str], int):
        """Execute Load Mssive for Data Sensor"""
        self.counter += self.add_counter
        conn = self.connection.get_cursor()
        entities = self.to_many_entities(data)
        sensor_datas = conn.sensorProccessed
        result = sensor_datas.insert_many(entities)
        result_data_id = result.inserted_ids
        return (
            [str(data_id) for data_id in result_data_id],
            len(result_data_id)
        )

    def to_entity(self, data: SensorData) -> Any:
        """Convert to Entity"""
        _x = self.data_sensor_time(data)
        del _x["_id"]
        return _x

    def to_many_entities(self, data: List[SensorData]) -> Any:
        """Convert all Sensor Data into entities"""
        return list(map(self.to_entity, data))
