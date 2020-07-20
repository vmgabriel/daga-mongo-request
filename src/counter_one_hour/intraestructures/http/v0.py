"""Connection for HTTP Protocol"""

# Develop: vmgabriel

# Libraries
from flask import Blueprint, jsonify, request

# Interfaces
from src.domain.protocols.http import HttpProtocol
from src.domain.models.database_interface import Database_Interface

# Fachade Comunication
from src.counter_five.infraestructures.database_measure \
    import Database_Measure_Five

# Validation
from src.counter_one_hour.application.validate import MeasureOneHourValidate

class MeasureOneHourV0(HttpProtocol):
    """Define Measure One Hour Data Class for Use of Http"""
    def __init__(
            self,
            database_interface: Database_Interface,
            measure_five: Database_Measure_Five
    ):
        self.name_table = 'measureonehour'
        self.database_measure = database_interface
        self.measure_five_minutes = measure_five
        self.validation = MeasureOneHourValidate()

    def get_blueprint(self) -> Blueprint:
        """Return the Router BluePrint of Module"""
        mod = Blueprint(self.name_table, __name__)

        @mod.route(
            '/{}/<string:data>'.format(self.name_table),
            methods=['POST'])
        def save_data(data: str):
            """Create Content of Measure in One Hour Into Database"""
            if not request.is_json:
                return jsonify({'code': 400, 'error': 'Data not found'}), 400

            base = request.get_json(force=True)

            print('data table - ', data)
            print('data base - ', base)

            if not (
                    'idReader' in base and
                    'idController' in base
            ):
                return jsonify({'message': 'Data not found'}), 400

            process_data = self.measure_five_minutes.average_content(**{
                'typeMeasure': data,
                'idReader': base['idReader'],
                'idController': base['idController']
            })

            (is_valid, valid_data) = self.validation.validate_object(
                process_data.to_dict()
            )
            if is_valid != 'done correctly':
                return jsonify({'message': 'Data not Valid'}), 400

            self.database_measure.put_odd_table(data.lower())
            new_measure = self.database_measure.create(valid_data)

            self.measure_five_minutes.delete_with_content(
                new_measure.id_reader,
                new_measure.id_controller,
                data
            )

            return jsonify({
                'message': 'Done Correctly',
                'data': new_measure.to_dict()
            }), 200

        return mod
