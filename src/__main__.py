# Develop vmgabriel

# Libraries
from flask import Flask, jsonify
from flask_jwt import JWT
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)

from config.server import configuration as conf

# Connection
from sensor_data.infraestructures.mongo.database_sensor_data import Database_SensorData
from sensor_data_processed.infraestructures.mongo.database_sensor_data import Database_SensorData as DbSensorProcessed
from counter_five.infraestructures.database_measure import Database_Measure_Five as DatabaseMeasureFive

# Routes
from protocols.http.v0.index import mod
from sensor_data.infraestructures.http.v0 import SensorDataV0Http
from sensor_data_processed.infraestructures.http.v0 import SensorDataV0Http as SensorProcessedV0Http
from counter_five.infraestructures.http.v0 import MeasureV0Http

persistency = conf['persistency']

sensorData_service = Database_SensorData(persistency)
sensorProcessedData_service = DbSensorProcessed(persistency)
measureFive_service = DatabaseMeasureFive(persistency)

list_routes = [
    SensorDataV0Http(sensorData_service),
    SensorProcessedV0Http(sensorProcessedData_service),
    MeasureV0Http(measureFive_service)
]

app = Flask(__name__)

app.config['JWT_TOKEN_LOCATION'] = conf['jwt_location']
app.config['JWT_SECRET_KEY'] = conf['jwt_secret']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

jwt = JWTManager(app)

app.register_blueprint(mod, url_prefix='/api')
for route in list_routes:
    app.register_blueprint(route.get_blueprint(), url_prefix='/api/v0')

if __name__ == '__main__':
    app.run (
        host=conf['host'],
        debug=conf['debug'],
        port=conf['port']
    )


