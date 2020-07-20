"""Create Sensor Data"""

# Develop: vmgabriel

# Libraries

# Interfaces
from src.sensor_data.domain.sensor_data import SensorData
from src.domain.models.db_connection import Db_Connection

# Validator for conver to Object
from src.sensor_data.applications.validate import SensorDataValidate

# Super Class
from src.domain.models.actions.create import Create


class Create_SensorData(Create[SensorData]):
    """Create Sensor Data Action Mongo"""
    def __init__(self, name_table: str, database: Db_Connection):
        self.name_table = name_table
        self.__database = database
        self.sensor_validate = SensorDataValidate()

    def execute(self, data: SensorData) -> SensorData:
        """Execute Create In Mongo"""
        conn = self.__database.get_cursor()
        data_entity = data.to_dict()
        del data_entity["_id"]
        sensors_data = conn.sensorData
        sensor_new_id = sensors_data.insert_one(data_entity).inserted_id
        data_entity['_id'] = str(sensor_new_id)
        (_, sensor_new) = self.sensor_validate.validate_object(data_entity)
        return sensor_new

    def to_entity(self, data: SensorData) -> (str, str):
        """Convert to Entity"""
        return (str(data), '')

    def to_query(self, data: SensorData) -> str:
        """Convert to Query"""
        return str(data)
