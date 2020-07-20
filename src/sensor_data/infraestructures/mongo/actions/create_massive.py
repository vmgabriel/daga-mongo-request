"""Create Mssive Data Mongo Module"""

# Develop: vmgabriel

# Libraries
from typing import List, Any

# Interfaces
from src.sensor_data.domain.sensor_data import SensorData

from src.domain.models.db_connection import Db_Connection

# Super Class
from src.domain.models.actions.create_massive import CreateMassive


class CreateMassive_SensorData(CreateMassive[SensorData]):
    """Create Mssive Class For Sensor Data into mongo"""
    def __init__(self, name_table: str, connection: Db_Connection):
        self.name_table = name_table
        self.connection = connection

    def execute(self, data: List[SensorData]) -> (List[str], int):
        """Execute Create Massively"""
        conn = self.connection.get_cursor()
        entities = self.to_many_entities(data)
        sensor_datas = conn.sensorData
        result = sensor_datas.insert_many(entities)
        result_data_id = result.inserted_ids
        return (
            [str(data_id) for data_id in result_data_id],
            len(result_data_id)
        )

    def to_entity(self, data: SensorData) -> Any:
        """Convert to Entity Data Valid"""
        _x = data.to_dict()
        del _x["_id"]
        return _x

    def to_many_entities(self, data: List[SensorData]) -> Any:
        """Convert Each to Entity"""
        return list(map(self.to_entity, data))
