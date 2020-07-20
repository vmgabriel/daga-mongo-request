# Develop: vmgabriel

"""Delete Module Action for Sqlite"""

# Structure
from src.counter_five.domain.measure_five import MeasureFive

from src.domain.models.database_interface import Database_Interface

# Abstract Action Domain
from src.domain.models.actions.delete import Delete

class DeleteSQLiteMeasure(Delete[MeasureFive]):
    """Delete SQLITE Measure data"""
    def __init__(self, name_table: str, database: Database_Interface):
        self.name_table = name_table
        self.__database = database
        self.query = "DELETE FROM {} WHERE idReader={} "
        self.query += "AND idController={} AND typeMeasure='{}'"

    def execute(
            self,
            idReader: int,
            idController: int,
            typeMeasure: str
    ) -> bool:
        """Define Execute process into database"""
        conn = self.__database.get_cursor()
        _db = self.__database.get_connection()
        query = self.to_query(idReader, idController, typeMeasure)
        _ = conn.execute(query)
        _db.commit()
        return True

    def to_query(
            self,
            idReader: int,
            idController: int,
            typeMeasure: str
    ) -> str:
        """Convert to query a order"""
        return self.query.format(
            self.name_table,
            idReader,
            idController,
            typeMeasure
        )
