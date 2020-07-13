# Develop: vmgabriel

# Libraries
import inject
from typing import List, TypeVar, Generic, Any, Tuple

# Interfaces
from sensor_data_processed.domain.sensor_data import SensorData

from domain.models.db_connection import Db_Connection
from domain.models.db.entity_conversor import Conversor_Type

# Super Class
from domain.models.actions.create_massive import CreateMassive

class CreateMassive_SensorData(CreateMassive[SensorData]):
    def __init__(self, name_table: str, connection: Db_Connection):
        self.name_table = name_table
        self.connection = connection

        self.counter = 2.5
        self.add_counter = 2.5

    def data_sensor_time(self, data: dict) -> dict:
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
            data['isFive'] = True
        if (self.counter % ten_step == 0):
            data['isTen'] = True
        if (self.counter % twenty_step == 0):
            data['isTwenty'] = True
        if (self.counter % thirty_step == 0):
            data['isThirty'] = True
        if (self.counter % hour_step == 0):
            data['isHour'] = True
        if (self.counter % two_hour_step == 0):
            data['isTwoHour'] = True
        if (self.counter % five_hour_step == 0):
            data['isFiveHour'] = True
        if (self.counter % one_day_step == 0):
            data['isDay'] = True
        if (self.counter % five_day_step == 0):
            data['isFiveDay'] = True
        if (self.counter % month_step == 0):
            data['isMonth'] = True
            self.counter = self.add_counter
        return data

    def execute(self, data: List[SensorData]) -> (List[str], int):
        self.counter += self.add_counter
        conn = self.connection.get_cursor()
        entities = self.to_many_entities(data)
        SensorDatas = conn.sensorProccessed
        result = SensorDatas.insert_many(entities)
        result_data_id = result.inserted_ids
        return ([ str(data_id) for data_id in result_data_id ], len(result_data_id))


    def to_entity(self, data: SensorData) -> Any:
        x = data.to_dict()
        x = self.data_sensor_time(x)
        del x["_id"]
        return x


    def to_many_entities(self, data: List[SensorData]) -> Any:
        return list(map(lambda x: self.to_entity(x), data))
