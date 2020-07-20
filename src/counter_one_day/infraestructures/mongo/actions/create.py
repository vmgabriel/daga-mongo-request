# Develop: vmgabriel

"""Create Module for Measure One Day"""

# Libraries
from src.counter_one_day.domain.measure_one_day import MeasureOneDay

# Interfaces
from src.domain.models.db_connection import Db_Connection
from src.domain.models.validation_interface import Validate_Interface

# Super Class
from src.domain.models.actions.create import Create


class CreateMeasureOneDay(Create[MeasureOneDay]):
    """Class for Create Measure By One Day"""
    def __init__(
            self,
            name_table: str,
            database: Db_Connection,
            validation: Validate_Interface
    ):
        self.name_data = self.name_table = name_table
        self.__database = database
        self.validation = validation

    def execute(self, data: MeasureOneDay) -> MeasureOneDay:
        """Execute Query Data"""
        conn = self.__database.get_cursor()
        data_entity = data.to_dict()
        del data_entity['_id']
        measures_data = conn[self.name_table]
        meassure_new_id = measures_data.insert_one(data_entity).inserted_id
        data_entity['_id'] = str(meassure_new_id)
        (_, meassure_new) = self.validation.validate_object(data_entity)
        return meassure_new

    def to_entity(self, data: MeasureOneDay) -> str:
        """Convert to Entity data Based into Database"""
        return ('', str(data))

    def to_query(self, data: MeasureOneDay) -> str:
        """Get Query Into Execute procedure"""
        return str(data)

    def put_name_table(self, name_table: str) -> None:
        """Set Name Table"""
        self.name_table = self.name_data + name_table
