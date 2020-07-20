# Develop: vmgabriel

"""Module of database Measure One Hour Fachade"""

# Libraries
from typing import List


# Models
from src.counter_one_hour.domain.measure_one_hour import MeasureOneHour

# Interfaces
from src.domain.models.database_interface import Database_Interface
from src.domain.models.db_connection import Db_Connection
from src.domain.models.db.entity_conversor import Conversor_Type

# Interfaces of Actions
from src.domain.models.actions.create import Create

# Connections
from src.utils.db.mongo.mongo import Mongo_Connection
from src.utils.db.mongo.mongo_type import Mongo_Type

# Validation
from src.counter_one_hour.application.validate import MeasureOneHourValidate

# Actions
# Mongo
from src.counter_one_hour.intraestructures.mongo.actions.create \
    import CreateMeasureOneHour


class DatabaseMeasureOneHour(Database_Interface[MeasureOneHour]):
    """Database Class For Measure One Hour"""
    def __init__(self, type_data: str, other_data: str):
        self.name_table = 'measureOneHour'
        self.odd_table = ''
        self.connection: Db_Connection = None
        self.conversor: Conversor_Type = None
        self.validation = MeasureOneHourValidate()

        self.create_meassure: Create = None

        self.builder(type_data, other_data)

    def put_odd_table(self, data: str) -> None:
        """Change odd_table"""
        print('data - ', data)
        self.odd_table = data

    def create(self, data: MeasureOneHour) -> MeasureOneHour:
        """Create Data into Database"""
        self.create_meassure.put_name_table(self.odd_table)
        return self.create_meassure.execute(data)

    def create_massive(self, data: List[MeasureOneHour]) -> List[str]:
        """Create Massive Method"""
        return [str(x) for x in data]

    def builder(self, definition: str, other_definition: str = '') -> None:
        """Builder for Select Database"""
        if definition == 'postgres':
            print('postgres')

        if definition == 'mongo':
            self.connection = Mongo_Connection()
            self.conversor = Mongo_Type()

            self.create_meassure = CreateMeasureOneHour(
                self.name_table,
                self.connection,
                self.validation
            )

        if definition == 'schema':
            print('schema')
