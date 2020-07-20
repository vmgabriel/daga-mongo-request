# Develop vmgabriel

"""Definition Use of Http"""

# Libraries
from flask import Blueprint, jsonify, request

# Interfaces
from src.domain.protocols.http import HttpProtocol
from src.domain.models.database_interface import Database_Interface

# Validation Data
from src.counter_five.applications.validate import MeasureFiveValidate


class MeasureV0Http(HttpProtocol):
    """Define Sensor Data Class for Use of HTTP, this extends HttpProtocol"""
    def __init__(self, database: Database_Interface):
        self.name_table = 'measurefive'
        self.validate = MeasureFiveValidate()
        self.database_measure = database

    def get_blueprint(self) -> Blueprint:
        """Return the Router Blueprint of Module"""
        mod = Blueprint(self.name_table, __name__)

        @mod.route(
            '/{}/<string:data>'.format(self.name_table),
            methods=['POST']
        )
        def create(data: str):
            """Create content into db"""
            if not request.is_json:
                return jsonify({'code': 400, 'error': 'Data not found'}), 400

            base = request.get_json(force=True)

            (errors, new_measure) = self.validate.validate_object(base)
            if errors != 'done correctly':
                return jsonify({'error': errors, 'code': 400}), 400
            self.database_measure.put_odd_table(data.lower())
            saved_measure = self.database_measure.create(new_measure)

            return jsonify({
                'message': 'Created Correcly', 'data': saved_measure.to_dict()
            }), 201

        @mod.route(
            '/{}/<string:data>/massive'.format(self.name_table),
            methods=['POST']
        )
        def create_massive(data: str):
            """Create massively various data"""
            if not request.is_json:
                return jsonify({'code': 400, 'error': 'Data not found'}), 400

            base = request.get_json(force=True)

            if not isinstance(base, list):
                return jsonify({
                    'code': 400, 'error': 'Data is not Array'
                }), 400

            definitions = list(map(self.validate.validate_object, base))
            datas = []

            for line, (message, obj) in enumerate(definitions):
                if message == 'done correctly':
                    datas.append(obj)
                else:
                    return jsonify({
                        'message': """Error saving Measure Five data in object:
                          {}""".format(line),
                        'error': message
                    }), 400

            self.database_measure.put_odd_table(data.lower())
            (saved_measure,count_measure) = self.database_measure.create_massive(datas)

            return jsonify({
                'message': 'Created Massive Correcly',
                'data': saved_measure,
                'count_document': count_measure
            }), 201

        return mod
