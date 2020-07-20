# Develop: vmgabriel

"""Definition for Create Sensor Data"""

# Interfaces
from src.sensor_data_processed.domain.sensor_data import SensorData
from src.domain.models.db_connection import Db_Connection

# Validator for conver to Object
from src.sensor_data_processed.applications.validate import SensorDataValidate

# Super Class
from src.domain.models.actions.create import Create


class Create_SensorData(Create[SensorData]):
    """Create Sensor Data For Mongo Processed"""
    def __init__(self, name_table: str, database: Db_Connection):
        self.name_table = name_table
        self.__database = database
        self.sensor_validate = SensorDataValidate()

        self.counter = 2.5
        self.add_counter = 2.5

    def data_sensor_time(self, data: SensorData) -> dict:
        """Data Sensor Time Validate"""
        self.counter += self.add_counter
        definition = data.to_dict()
        five_step = 5
        ten_step = 10
        twenty_step = 20
        thirty_step = 30
        hour_step = 60
        two_hour_step = 120
        five_hour_step = 300
        one_day_step = 1440
        five_day_step = 7200
        month_step = 43200

        definition['isFive'] = self.counter % five_step == 0
        definition['isTen'] = self.counter % ten_step == 0
        definition['isTwenty'] = self.counter % twenty_step == 0
        definition['isThirty'] = self.counter % thirty_step == 0
        definition['isHour'] = self.counter % hour_step == 0
        definition['isTwoHour'] = self.counter % two_hour_step == 0
        definition['isFiveHour'] = self.counter % five_hour_step == 0
        definition['isDay'] = self.counter % one_day_step == 0
        definition['isFiveDay'] = self.counter % five_day_step == 0
        definition['isMonth'] = self.counter % month_step == 0
        if self.counter % month_step == 0:
            self.counter = self.add_counter
        return definition

    def execute(self, data: SensorData) -> SensorData:
        """Execute Process for Create Sensor Processed"""
        conn = self.__database.get_cursor()
        data_with_sensor = self.data_sensor_time(data)
        del data_with_sensor["_id"]
        sensors_data = conn.sensorProcessed
        sensor_new_id = sensors_data.insert_one(data_with_sensor).inserted_id
        data_with_sensor['_id'] = str(sensor_new_id)
        (_, sensor_new) = self.sensor_validate.validate_object(data_with_sensor)
        return sensor_new

    def to_entity(self, data: SensorData) -> (str, str):
        """Get Entity data"""
        return ('', str(data))

    def to_query(self, data: SensorData) -> str:
        """Get to Query Data"""
        return str(data)
