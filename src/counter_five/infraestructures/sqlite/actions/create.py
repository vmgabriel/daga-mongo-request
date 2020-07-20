# Develop: vmgabriel

"""Create Measure Counter Five"""


from src.counter_five.domain.measure_five import MeasureFive

# Interfaces
from src.domain.models.db_connection import Db_Connection
from src.domain.models.db.entity_conversor import Conversor_Type
# Super Class
from src.domain.models.actions.create import Create


class Create_Measure(Create[MeasureFive]):
    """Create Action Measure"""
    def __init__(
            self, name_table: str,
            database: Db_Connection,
            conversor: Conversor_Type
    ):
        self.name_data = self.name_table = name_table
        self.__database = database
        self.conversor = conversor
        self.query = 'INSERT INTO {} '.format(name_table)

    def execute(self, data: MeasureFive) -> MeasureFive:
        """Execute query"""
        conn = self.__database.get_cursor()
        d_b = self.__database.get_connection()
        query = self.query + self.to_query(data)
        _ = conn.execute(query)
        d_b.commit()
        return data

    def to_entity(self, data: MeasureFive) -> (str, str):
        """Convert to entity data based into database"""
        datas = str(data)
        query = definitions = ''

        for i in datas.split(','):
            temp = data.to_dict().get(i.strip())
            if temp:
                type_data = data.define_type(i.strip())
                query += self.conversor.to_entity(type_data, temp)
                definitions += i.strip()
                query += ','
                definitions += ','

        query += "'{}'".format(self.name_table)
        definitions += 'typeMeasure'
        return (query, definitions)

    def to_query(self, data: MeasureFive) -> str:
        """Get Query into execute procedure"""
        (datas, values) = self.to_entity(data)
        query = '({}) VALUES ({});'.format(values, datas)
        return query

    def put_name_table(self, name_table: str) -> None:
        """Set Name table"""
        self.name_table = name_table
