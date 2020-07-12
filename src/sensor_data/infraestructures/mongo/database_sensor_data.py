# Develop vmgabriel

# Libraries
from typing import List, TypeVar, Generic, Any, Tuple

# Models
from sensor_data.domain.sensor_data import SensorData

# Interfaces
from domain.models.database_interface import Database_Interface
from domain.models.db_connection import Db_Connection
from domain.models.db.entity_conversor import Conversor_Type
from domain.models.filter_interface import Attribute_Filter, Filter_Interface

## Interfaces of Actions
from domain.models.actions.count import Count
from domain.models.actions.create import Create
from domain.models.actions.create_massive import CreateMassive

# Connections
from utils.db.mongo.mongo import Mongo_Connection
from utils.db.mongo.mongo_type import Mongo_Type

# Actions

## Mongo
from sensor_data.infraestructures.mongo.actions.create import Create_SensorData as Create_Mongo
from sensor_data.infraestructures.mongo.actions.create_massive import CreateMassive_SensorData as CreateMassive_Mongo

## Schema

class Database_SensorData(Database_Interface[SensorData]):
    def __init__(self, type_data: str):
        self.name_table = 'sensorData'
        self.connection: Db_Connection = None
        self.conversor: Conversor_Type = None

        self.count_sensorData: Count = None
        self.create_sensorData: Create = None
        self.create_massive_sensorData: CreateMassive = None

        self.builder(type_data)


    def create(self, data: SensorData) -> SensorData:
        return self.create_sensorData.execute(data)


    def create_massive(self, data: List[SensorData]) -> List[str]:
        return self.create_massive_sensorData.execute(data)


    def builder(self, definition: str) -> None:
        if (definition == 'postgres'):
            pass

        if (definition == 'mongo'):
            self.connection = Mongo_Connection()
            self.conversor = Mongo_Type()

            self.create_sensorData = Create_Mongo(self.name_table, self.connection)
            self.create_massive_sensorData = CreateMassive_Mongo(self.name_table, self.connection)

        if (definition == 'schema'):
            pass

