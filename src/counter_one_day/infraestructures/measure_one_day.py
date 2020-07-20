# Develop: vmgabriel

"""Module of Measure One Day Data"""

# Libraries
from typing import List

# Models
from src.counter_one_day.domain.measure_one_day import MeasureOneDay

# Interfaces
from src.domain.models.database_interface import Database_Interface
from src.domain.models.db_connection import Db_Connection
from src.domain.models.db.entity_conversor import Conversor_Type

# Interface of Actions
from src.domain.models.actions.create import Create

# Connections
from src.utils.db.mongo.mongo import Mongo_Connection
from src.utils.db.mongo.mongo_type import Mongo_Type

# Validation
from src.counter_one_day.application.validate import MeasureOneDayValidate

# Actions
# Mongo
from src.counter_one_day.infraestructures.mongo.actions.create \
    import CreateMeasureOneDay


class DatabaseMeasureOneDay(Database_Interface[MeasureOneDay]):
    """Database Class For Measure One Day"""
    def __init__(self, type_data: str, other_data: str):
        self.name_table = 'measureOneDay'
        self.odd_table = ''
        self.connection: Db_Connection = None
        self.conversor: Conversor_Type = None
        self.validation = MeasureOneDayValidate()

        self.create_measure: Create = None

        self.builder(type_data, other_data)

    def put_odd_table(self, data: str) -> None:
        """Change odd_table"""
        self.odd_table = data

    def create(self, data: MeasureOneDay) -> MeasureOneDay:
        """Create Data into Database"""
        self.create_measure.put_name_table(self.odd_table)
        return self.create_measure.execute(data)

    def create_massive(self, data: List[MeasureOneDay]) -> List[str]:
        """Create Massive Method"""
        return [str(x) for x in data]

    def builder(self, definition: str, other_definition: str = '') -> None:
        """Builder for Select Database"""
        if definition == 'postgres':
            print('postgres')

        if definition == 'mongo':
            self.connection = Mongo_Connection()
            self.conversor = Mongo_Type()

            self.create_measure = CreateMeasureOneDay(
                self.name_table,
                self.connection,
                self.validation
            )

        if definition == 'schema':
            print('schema')
