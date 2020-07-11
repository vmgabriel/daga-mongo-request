# Develop: vmgabriel

# Libraries
import inject
from typing import List, TypeVar, Generic, Any, Tuple

# Interfaces
from sensor_data.domain.sensor_data import SensorData

from domain.models.db_connection import Db_Connection
from domain.models.db.entity_conversor import Conversor_Type

# Super Class
from domain.models.actions.create_massive import CreateMassive

class CreateMassive_SensorData(CreateMassive[SensorData]):
    def __init__(self, name_table: str, connection: Db_Connection):
        self.name_table = name_table
        self.connection = connection

    def execute(self, data: List[SensorData]) -> (List[str], int):
        conn = self.connection.get_cursor()
        entities = self.to_many_entities(data)
        SensorDatas = conn.sensorData
        result = SensorDatas.insert_many(entities)
        result_data_id = result.inserted_ids
        return ([ str(data_id) for data_id in result_data_id ], len(result_data_id))


    def to_entity(self, data: SensorData) -> Any:
        x = data.to_dict()
        del x["_id"]
        return x


    def to_many_entities(self, data: List[SensorData]) -> Any:
        return list(map(lambda x: self.to_entity(x), data))
