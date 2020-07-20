# Develop vmgabriel

"""Module of database Measure Fachade"""

# Libraries
from typing import List

# Models
from src.counter_five.domain.measure_five import MeasureFive

# Interfaces
from src.domain.models.database_interface import Database_Interface
from src.domain.models.db_connection import Db_Connection
from src.domain.models.db.entity_conversor import Conversor_Type

# Interfaces of Actions
from src.domain.models.actions.create import Create
from src.domain.models.actions.create_massive import CreateMassive
from src.domain.models.actions.average import Average
from src.domain.models.actions.delete import Delete

# Connections
from src.utils.db.mongo.mongo import Mongo_Connection
from src.utils.db.mongo.mongo_type import Mongo_Type
from src.utils.db.sqlite.sqlite import SQLiteConnection
from src.utils.db.sqlite.sqlite_type import SQLiteType

# Validation
from src.counter_five.applications.validate import MeasureFiveValidate

# Actions
# Sqlite
from src.counter_five.infraestructures.sqlite.actions.create \
    import Create_Measure as createSQLite
from src.counter_five.infraestructures.sqlite.actions.average \
    import AverageSQLite
from src.counter_five.infraestructures.sqlite.actions.delete \
    import DeleteSQLiteMeasure

# Mongo
from src.counter_five.infraestructures.mongo.actions.create \
    import Create_Measure as CreateMongo
from src.counter_five.infraestructures.mongo.actions.create_massive \
    import CreateMassive_Measure as CreateMassiveMongo


class Database_Measure_Five(Database_Interface[MeasureFive]):
    """Measure Data Five"""
    def __init__(self, type_data: str, fastly_data: str):
        self.name_table = 'measureFive'
        self.odd_table = ''
        self.validation = MeasureFiveValidate()
        self.connection: Db_Connection = None
        self.other_connection: Db_Connection = None
        self.conversor: Conversor_Type = None
        self.other_conversor: Conversor_Type = None

        self.create_measure: Create = None
        self.create_measure_secundary: Create = None
        self.create_massive_measure: CreateMassive = None
        self.average: Average = None
        self.delete: Delete = None

        self.builder(type_data, fastly_data)

    def put_odd_table(self, data: str) -> None:
        """Change odd_table"""
        self.odd_table = data

    def create(self, data: MeasureFive) -> MeasureFive:
        """Create Data into Database"""
        self.create_measure.put_name_table(self.odd_table)
        self.create_measure_secundary.put_name_table(self.odd_table)
        output = self.create_measure_secundary.execute(data)
        print('create output - ', output)
        return self.create_measure.execute(data)

    def create_massive(self, data: List[MeasureFive]) -> List[str]:
        """Create Various Datas into Database"""
        self.create_massive_measure.put_name_table(self.odd_table)
        for definition in data:
            output = self.create(definition)
            print('output massive - ', output)
        return self.create_massive_measure.execute(data)

    def average_content(self, **data) -> MeasureFive:
        """Average data based"""
        return self.average.execute(**data)

    def delete_with_content(
            self,
            idReader: int,
            idController: int,
            typeMeasure: str
    ) -> bool:
        return self.delete.execute(idReader, idController, typeMeasure)

    def builder(self, definition: str, other_definition: str = '') -> None:
        """Builder for Select Database"""
        if definition == 'postgres':
            print('postgres')

        if definition == 'mongo':
            self.connection = Mongo_Connection()
            self.conversor = Mongo_Type()

            self.create_measure = CreateMongo(
                self.name_table,
                self.connection,
                self.validation
            )
            self.create_massive_measure = CreateMassiveMongo(
                self.name_table,
                self.connection
            )

        if definition == 'schema':
            print('schema')

        if other_definition == 'sqlite':
            self.other_connection = SQLiteConnection()
            self.other_conversor = SQLiteType()

            self.create_measure_secundary = createSQLite(
                self.name_table,
                self.other_connection,
                self.other_conversor
            )
            self.average = AverageSQLite(
                self.name_table,
                self.other_connection
            )
            self.delete = DeleteSQLiteMeasure(
                self.name_table,
                self.other_connection
            )
