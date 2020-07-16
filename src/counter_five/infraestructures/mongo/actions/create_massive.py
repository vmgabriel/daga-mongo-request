# Develop: vmgabriel

# Libraries
import inject
from typing import List, TypeVar, Generic, Any, Tuple

# Interfaces
from counter_five.domain.measure_five import MeasureFive

from domain.models.db_connection import Db_Connection
from domain.models.db.entity_conversor import Conversor_Type

# Super Class
from domain.models.actions.create_massive import CreateMassive

class CreateMassive_Measure(CreateMassive[MeasureFive]):
    """Create Massively Action for Measure"""
    def __init__(self, name_table: str, connection: Db_Connection):
        self.name_table = self.name_data = name_table
        self.connection = connection


    def execute(self, data: List[MeasureFive]) -> (List[str], int):
        """Execute Action"""
        conn = self.connection.get_cursor()
        entities = self.to_many_entities(data)
        SensorDatas = conn[self.name_table]
        result = SensorDatas.insert_many(entities)
        result_data_id = result.inserted_ids
        return ([ str(data_id) for data_id in result_data_id ], len(result_data_id))


    def to_entity(self, data: MeasureFive) -> Any:
        """Convert to Entity Database"""
        x = data.to_dict()
        del x["_id"]
        return x


    def to_many_entities(self, data: List[MeasureFive]) -> Any:
        """Convert All datas to entity database"""
        return list(map(lambda x: self.to_entity(x), data))


    def put_name_table(self, name_table: str) -> None:
        """Set Name table"""
        self.name_table = self.name_data + name_table
