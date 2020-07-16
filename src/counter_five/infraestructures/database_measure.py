# Develop vmgabriel

# Libraries
from typing import List, TypeVar, Generic, Any, Tuple

# Models
from counter_five.domain.measure_five import MeasureFive

# Interfaces
from domain.models.database_interface import Database_Interface
from domain.models.db_connection import Db_Connection
from domain.models.db.entity_conversor import Conversor_Type
from domain.models.filter_interface import Attribute_Filter, Filter_Interface

## Interfaces of Actions
from domain.models.actions.create import Create
from domain.models.actions.create_massive import CreateMassive

# Connections
from utils.db.mongo.mongo import Mongo_Connection
from utils.db.mongo.mongo_type import Mongo_Type

# Validation
from counter_five.applications.validate import MeasureFiveValidate

# Actions

## Mongo
from counter_five.infraestructures.mongo.actions.create import Create_Measure as CreateMongo
from counter_five.infraestructures.mongo.actions.create_massive import CreateMassive_Measure as CreateMassiveMongo

## Schema

class Database_Measure_Five(Database_Interface[MeasureFive]):
    """Measure Data Five"""
    def __init__(self, type_data: str):
        self.name_table = 'measureFive'
        self.odd_table = ''
        self.validation = MeasureFiveValidate()
        self.connection: Db_Connection = None
        self.conversor: Conversor_Type = None

        self.create_measure: Create = None
        self.create_massive_measure: CreateMassive = None

        self.builder(type_data)

    def put_odd_table(self, data: str) -> None:
        """Change odd_table"""
        self.odd_table = data

    def create(self, data: MeasureFive) -> MeasureFive:
        """Create Data into Database"""
        self.create_measure.put_name_table(self.odd_table)
        return self.create_measure.execute(data)


    def create_massive(self, data: List[MeasureFive]) -> List[str]:
        """Create Various Datas into Database"""
        self.create_massive_measure.put_name_table(self.odd_table)
        return self.create_massive_measure.execute(data)


    def builder(self, definition: str) -> None:
        """Builder for Select Database"""
        if (definition == 'postgres'):
            pass

        if (definition == 'mongo'):
            self.connection = Mongo_Connection()
            self.conversor = Mongo_Type()

            self.create_measure = CreateMongo(self.name_table, self.connection, self.validation)
            self.create_massive_measure = CreateMassiveMongo(self.name_table, self.connection)

        if (definition == 'schema'):
            pass

