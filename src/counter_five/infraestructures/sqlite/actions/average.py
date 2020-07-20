#!/usr/bin/python3

"""Average of SQLite Measure"""

# Develop: vmgabriel

# Libraries
from typing import List

# Interface
from src.domain.models.actions.average import Average
from src.domain.models.db_connection import Db_Connection

# Structure
from src.counter_five.domain.measure_five import MeasureFive


class AverageSQLite(Average[MeasureFive]):
    """Averave of Measure for Sqlite"""
    def __init__(self, name_table: str, database: Db_Connection):
        self.name_table = name_table
        self.__database = database
        self.query = 'SELECT AVG(min), AVG(max), SUM(counter), AVG(gr1), '
        self.query += 'AVG(gr2), AVG(gr3), AVG(gr4) FROM measureFive '
        self.query += 'WHERE idReader={} AND idController={} '
        self.query += "AND typeMeasure='{}';"

    def execute(self, **datas) -> List[MeasureFive]:
        """Execute Average"""
        print('datas execute - ', datas)
        print('datas to save - {}'.format(self.to_query(**datas)))
        return []

    def to_query(self, **datas) -> str:
        """Get Query"""
        print('datas - ', datas)
        if (
                'idReader' in datas and
                'idController' in datas and
                'typeMeasure' in datas
        ):
            return self.query.format(
                datas['idReader'],
                datas['idController'],
                datas['typeMeasure']
            )
        return ''
