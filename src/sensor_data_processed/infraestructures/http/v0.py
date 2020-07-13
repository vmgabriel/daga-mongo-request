# Develop vmgabriel

# Interfaces
from domain.protocols.http import HttpProtocol
from domain.models.database_interface import Database_Interface
from sensor_data_processed.applications.validate import SensorDataValidate

from sensor_data_processed.domain.sensor_data import SensorData

# Libraries
import datetime
from flask import Blueprint, jsonify, request
from utils.middlewares.last_data_relation import get_data_relation, remove_datas

class SensorDataV0Http(HttpProtocol):
    """Define Sensor Data Relation Data Class for Use of HTTP, this extends HttpProtocol"""
    def __init__(self, database: Database_Interface):
        self.name_table = 'sensorprocess'
        self.validate = SensorDataValidate()
        self.database_sensor = database

    def get_blueprint(self) ->  Blueprint:
        mod = Blueprint(self.name_table, __name__)

        @mod.route('/{}/activate'.format(self.name_table), methods=['GET'])
        def activate_process():
            print('df - {}'.format(get_data_relation()))
            if (len(get_data_relation()) > 0):
                (saved_sensorsDatas, count_sensors) = self.database_sensor.create_massive(
                    get_data_relation()
                )
                remove_datas()

            return jsonify({
                'message': 'Done Correctly'
            }), 201

        return mod


