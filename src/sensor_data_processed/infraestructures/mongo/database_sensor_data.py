# Develop vmgabriel

"""Definition for Database Sensor"""

# Libraries
from typing import List

# Models
from src.sensor_data_processed.domain.sensor_data import SensorData

# Interfaces
from src.domain.models.database_interface import Database_Interface
from src.domain.models.db_connection import Db_Connection
from src.domain.models.db.entity_conversor import Conversor_Type

# Interfaces of Actions
from src.domain.models.actions.create import Create
from src.domain.models.actions.create_massive import CreateMassive

# Connections
from src.utils.db.mongo.mongo import Mongo_Connection
from src.utils.db.mongo.mongo_type import Mongo_Type

# Actions

# Mongo
from src.sensor_data_processed.infraestructures.mongo.actions.create \
    import Create_SensorData as Create_Mongo
from src.sensor_data_processed.infraestructures.mongo.actions.create_massive \
    import CreateMassive_SensorData as CreateMassive_Mongo

# Schema


class Database_SensorData(Database_Interface[SensorData]):
    """Database Sensor Processed Fachade"""
    def __init__(self, type_data: str):
        self.name_table = 'sensorProcesed'
        self.connection: Db_Connection = None
        self.conversor: Conversor_Type = None

        self.create_sensor_data: Create = None
        self.create_massive_sensor_data: CreateMassive = None

        self.builder(type_data)

    def create(self, data: SensorData) -> SensorData:
        """Create Method for Fachade for Sensor Data"""
        return self.create_sensor_data.execute(data)

    def create_massive(self, data: List[SensorData]) -> List[str]:
        """Create Massive Method for Fachade for Sensor Data"""
        return self.create_massive_sensor_data.execute(data)

    def builder(self, definition: str, other_definition: str = '') -> None:
        """Define the Classes that it going to use"""
        if definition == 'postgres':
            pass

        if definition == 'mongo':
            self.connection = Mongo_Connection()
            self.conversor = Mongo_Type()

            self.create_sensor_data = Create_Mongo(
                self.name_table,
                self.connection
            )
            self.create_massive_sensor_data = CreateMassive_Mongo(
                self.name_table,
                self.connection
            )

        if definition == 'schema':
            pass
