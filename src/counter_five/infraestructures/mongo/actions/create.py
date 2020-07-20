# Develop: vmgabriel

"""Module for Create Measure"""

# Libraries
from src.counter_five.domain.measure_five import MeasureFive

# Interfaces
from src.domain.models.db_connection import Db_Connection

from src.domain.models.validation_interface import Validate_Interface
# Super Class
from src.domain.models.actions.create import Create


class Create_Measure(Create[MeasureFive]):
    """Create Action Measure"""
    def __init__(
            self,
            name_table: str,
            database: Db_Connection,
            validation: Validate_Interface
    ):
        self.name_data = self.name_table = name_table
        self.__database = database
        self.measure_validate = validation

    def execute(self, data: MeasureFive) -> MeasureFive:
        """Execute query"""
        conn = self.__database.get_cursor()
        data_entity = data.to_dict()
        del data_entity["_id"]
        measures_data = conn[self.name_table]
        measure_new_id = measures_data.insert_one(data_entity).inserted_id
        data_entity['_id'] = str(measure_new_id)
        (_, measure_new) = self.measure_validate.validate_object(data_entity)
        return measure_new

    def to_entity(self, data: MeasureFive) -> (str, str):
        """Convert to entity data based into database"""
        return ('', str(data))

    def to_query(self, data: MeasureFive) -> str:
        """Get Query into execute procedure"""
        return str(data)

    def put_name_table(self, name_table: str) -> None:
        """Set Name table"""
        self.name_table = self.name_data + name_table
