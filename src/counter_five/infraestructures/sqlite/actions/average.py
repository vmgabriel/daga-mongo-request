#!/usr/bin/python3

"""Average of SQLite Measure"""

# Develop: vmgabriel

# Libraries
from datetime import datetime
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
        self.query += 'AVG(gr2), AVG(gr3), AVG(gr4), nameController, '
        self.query += 'nameReader FROM measureFive  WHERE idReader={} '
        self.query += "AND idController={} AND typeMeasure='{}';"

    def execute(self, **datas) -> MeasureFive:
        """Execute Average"""
        query = self.to_query(**datas)
        conn = self.__database.get_cursor()
        conn.execute(query)
        output = conn.fetchone()
        print('datas to save - {}'.format(query))
        print('output value - {}'.format(output))

        return MeasureFive(
            0,
            datetime.now(),
            output[0] if output[0] else 0,
            output[1] if output[1] else 0,
            output[2] if output[2] else 0,
            output[3] if output[3] else 0,
            output[4] if output[4] else 0,
            output[5] if output[5] else 0,
            output[6] if output[6] else 0,
            datas['idReader'],
            output[7] if output[7] else '',
            datas['idController'],
            output[8] if output[8] else '',
            datetime.now(),
            datetime.now(),
            None)

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
