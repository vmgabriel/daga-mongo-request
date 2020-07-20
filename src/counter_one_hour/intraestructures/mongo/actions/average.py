# Develop: vmgabriel

"""Module for Average in data"""

# Libraries
from datetime import datetime
from typing import Any

# Interfaces
from src.domain.models.actions.average import Average
from src.domain.models.db_connection import Db_Connection

# Structure
from src.counter_one_hour.domain.measure_one_hour import MeasureOneHour


class AverageMongoMeasureOneHour(Average[MeasureOneHour]):
    """Average of Measure One Hour for Mongo"""
    def __init__(self, name_table: str, database: Db_Connection):
        self.name_data = self.name_table = name_table
        self.__database = database
        self.query = {
            '$group': {
                '_id': '$idReader',
                'counter': {'$sum': '$counter'},
                'min': {'$avg': '$min'},
                'max': {'$avg': '$max'},
                'gr1': {'$avg': '$gr1'},
                'gr2': {'$avg': '$gr2'},
                'gr3': {'$avg': '$gr3'},
                'gr4': {'$avg': '$gr4'},
                'name_controller': {'$last': '$nameController'},
                'name_reader': {'$last': '$nameReader'},
                'id_controller': {'$last': '$idController'},
            }
        }

    def put_name_table(self, name_table: str) -> None:
        """Set Name table"""
        self.name_table = self.name_data + name_table

    def execute(self, datas) -> MeasureOneHour:
        """Execute Average for One Hour"""
        query = self.to_query(**datas)
        print('query - {}'.format(query))
        conn = self.__database.get_cursor()
        measure_one_hours = conn[self.name_table]
        data_output = list(measure_one_hours.aggregate(query))
        if len(data_output) == 1:
            data_output = data_output[0]
            data_output['id_reader'] = data_output['_id']
            data_output['created_at'] = \
                data_output['updated_at'] = \
                data_output['took_time'] = datetime.now()
            data_output['deleted_at'] = None
            return MeasureOneHour(**data_output)
        return None

    def to_query(self, **datas) -> Any:
        """Get Query"""
        print('data - {}'.format(datas))
        if (
                'idReader' in datas and
                'idController' in datas and
                'date' in datas
        ):
            date = datetime.strptime(datas['date'], '%Y-%m-%dT%H:%M:%SZ')
            first_data = datetime(date.year, date.month, date.day, 0, 0, 0)
            last_data = datetime(date.year, date.month, date.day + 1, 0, 0, 0)
            query = {
                '$match': {
                    "idController": datas['idController'],
                    "idReader": datas['idReader'],
                    "tookTime": {
                        '$gte': first_data,
                        '$lt': last_data
                    }
                }
            }
            return [query, self.query]
        return []
