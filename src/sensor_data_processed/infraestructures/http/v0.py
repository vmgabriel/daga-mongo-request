"""Module For Use Http Procol"""

# Develop vmgabriel

# Libraries
from flask import Blueprint, jsonify
from src.utils.middlewares.last_data_relation import get_data_relation, remove_datas

# Interfaces
from src.domain.protocols.http import HttpProtocol
from src.domain.models.database_interface import Database_Interface
from src.sensor_data_processed.applications.validate import SensorDataValidate


class SensorDataV0Http(HttpProtocol):
    """Define Sensor Data Relation Data Class for Use of HTTP,
    this extends HttpProtocol"""
    def __init__(self, database: Database_Interface):
        self.name_table = 'sensorprocess'
        self.validate = SensorDataValidate()
        self.database_sensor = database

    def get_blueprint(self) -> Blueprint:
        """Definition of Blueprint for Protocol Http"""
        mod = Blueprint(self.name_table, __name__)

        @mod.route('/{}/activate'.format(self.name_table), methods=['GET'])
        def activate_process():
            """Define Activate Process"""
            print('get_data_relation - {}'.format(get_data_relation()))
            if len(get_data_relation()) > 0:
                _ = self.database_sensor.create_massive(
                    get_data_relation()
                )
                remove_datas()

            return jsonify({
                'message': 'Done Correctly'
            }), 201

        return mod
