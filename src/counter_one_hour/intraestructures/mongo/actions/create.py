# Develop: vmgabriel

"""Module of Create Data into Mongo Db"""

# Libraries
from src.counter_one_hour.domain.measure_one_hour import MeasureOneHour

# Interfaces
from src.domain.models.db_connection import Db_Connection
from src.domain.models.validation_interface import Validate_Interface

# Super Class
from src.domain.models.actions.create import Create


class CreateMeasureOneHour(Create[MeasureOneHour]):
    """Class for Create Measure by One Hour"""
    def __init__(
            self,
            name_table: str,
            database: Db_Connection,
            validation: Validate_Interface
    ):
        self.name_data = self.name_table = name_table
        self.__database = database
        self.validation = validation

    def execute(self, data: MeasureOneHour) -> MeasureOneHour:
        """Execute Query Data"""
        conn = self.__database.get_cursor()
        data_entity = data.to_dict()
        del data_entity['_id']
        measures_data = conn[self.name_table]
        measure_new_id = measures_data.insert_one(data_entity).inserted_id
        data_entity['_id'] = str(measure_new_id)
        (_, measure_new) = self.validation.validate_object(data_entity)
        return measure_new

    def to_entity(self, data: MeasureOneHour) -> (str, str):
        """Convert to Entity data based into database"""
        return ('', str(data))

    def to_query(self, data: MeasureOneHour) -> str:
        """Get Query Into Execute Procedure"""
        return str(data)

    def put_name_table(self, name_table: str) -> None:
        """Set Name Table"""
        self.name_table = self.name_data + name_table
