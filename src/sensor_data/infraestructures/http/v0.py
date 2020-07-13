# Develop vmgabriel

# Interfaces
from domain.protocols.http import HttpProtocol
from domain.models.database_interface import Database_Interface
from sensor_data.applications.validate import SensorDataValidate

from sensor_data.domain.sensor_data import SensorData

# Libraries
import datetime
from flask import Blueprint, jsonify, request
from utils.middlewares.last_data_relation import verify_datas, get_data_relation

class SensorDataV0Http(HttpProtocol):
    """Define Sensor Data Class for Use of HTTP, this extends HttpProtocol"""
    def __init__(self, database: Database_Interface):
        self.name_table = 'sensordatas'
        self.validate = SensorDataValidate()
        self.database_sensor = database

    def get_blueprint(self) ->  Blueprint:
        mod = Blueprint(self.name_table, __name__)

        @mod.route('/{}'.format(self.name_table), methods=['POST'])
        def create():
            if not request.is_json:
                return jsonify({ 'code': 400,'error': 'Data no Valid' }), 400

            data = request.get_json(force=True)
            data['createdAt'] = data['updatedAt'] = datetime.datetime.now()

            (errors, new_sensorData) = self.validate.validate_object(data)


            if not (errors == 'done correctly'):
                return jsonify({ 'error': errors, 'code': 400 }), 400

            saved_sensorData = self.database_sensor.create(new_sensorData)
            verify_datas(saved_sensorData)

            return jsonify({ 'message': 'Created Correcly', 'data': saved_sensorData.to_dict() }), 201

        @mod.route('/{}/massive'.format(self.name_table), methods=['POST'])
        def create_massive():
            if not request.is_json:
                return jsonify({ 'code': 400,'error': 'Data no Valid' }), 400

            data = request.get_json(force=True)

            if not(type(data) == list):
                return jsonify({ 'code': 400,'error': 'Data is not Array' }), 400

            definitions = list(map(lambda x: self.validate.validate_object(x), data))
            datas = []

            for line, (message, obj) in enumerate(definitions):
                if (message == 'done correctly'):
                    datas.append(obj)
                else:
                    return jsonify({
                        'message': 'Error saving sensor data in object {}'.format(line),
                        'error': message
                    }), 400
            verify_datas(datas)

            (saved_sensorsDatas, count_sensors) = self.database_sensor.create_massive(datas)

            return jsonify({
                'message': 'Created Massive Correcly',
                'data': saved_sensorsDatas,
                'count_document': count_sensors
            }), 201

        return mod


