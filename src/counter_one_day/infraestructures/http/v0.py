# Develop: vmgabriel

"""Module for V0 to protocol HTTP"""

# Libraries
from flask import Blueprint, jsonify, request

# Interfaces
from src.domain.protocols.http import HttpProtocol
from src.domain.models.database_interface import Database_Interface

# Fachade Comunication
from src.counter_one_hour.intraestructures.database_measure_one_hour \
    import DatabaseMeasureOneHour

# Validation
from src.counter_one_day.application.validate import MeasureOneDayValidate

class MeasureOneDayV0(HttpProtocol):
    """Define Measure One Day Data Class For Use of Http"""
    def __init__(
            self,
            database_interface: Database_Interface,
            measure_one_hour: DatabaseMeasureOneHour
    ):
        self.name_table = 'measureoneday'
        self.database_measure = database_interface
        self.mesure_one_hour = measure_one_hour
        self.validation = MeasureOneDayValidate()

    def get_blueprint(self) -> Blueprint:
        """Return the Router BluePrint of Measure One Day"""
        mod = Blueprint(self.name_table, __name__)

        @mod.route(
            '/{}/<string:data>'.format(self.name_table),
            methods=['POST'])
        def save_data(data: str):
            """Create Content of Measure in One Day Into Database"""
            if not request.is_json:
                return jsonify({'code': 400, 'error': 'Data Not Found'}), 400

            base = request.get_json(force=True)

            print('data table - ', data)
            print('data base - ', base)

            if not (
                    'idReader' in base and
                    'idController' in base and
                    'date' in base
            ):
                return jsonify({'message': 'Data Not Found'}), 400

            self.mesure_one_hour.put_odd_table(data)
            output = self.mesure_one_hour.average_reader_one_hour(base)
            print('output - {}'.format(output.to_dict()))

            (is_ok, new_data) = self.validation.validate_object(
                output.to_dict()
            )

            if is_ok != 'done correctly':
                return jsonify({
                    'code': 400, 'error': 'Data is not Valid'
                }), 400

            self.database_measure.put_odd_table(data)
            new_measure = self.database_measure.create(new_data)

            return jsonify({
                'message': 'Done Correcly', 'data': new_measure.to_dict()
            }), 200

        return mod
