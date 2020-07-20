# Develop vmgabriel

"""Module of Instance"""

# Libraries
from flask import Flask
from flask_jwt_extended import JWTManager

from src.config.server import configuration as conf

# Connection
from src.sensor_data.infraestructures.mongo.database_sensor_data \
    import Database_SensorData
from src.sensor_data_processed.infraestructures.mongo.database_sensor_data \
    import Database_SensorData as DbSensorProcessed
from src.counter_five.infraestructures.database_measure \
    import Database_Measure_Five as DatabaseMeasureFive

# Routes
from src.protocols.http.v0.index import mod
from src.sensor_data.infraestructures.http.v0 import SensorDataV0Http
from src.sensor_data_processed.infraestructures.http.v0 \
    import SensorDataV0Http as SensorProcessedV0Http
from src.counter_five.infraestructures.http.v0 import MeasureV0Http

PERSISTENCY = conf['persistency']
OTHER_PERSISTENCY = conf['persistency_secundary']

sensorData_service = Database_SensorData(PERSISTENCY)
sensorProcessedData_service = DbSensorProcessed(PERSISTENCY)
measureFive_service = DatabaseMeasureFive(PERSISTENCY, OTHER_PERSISTENCY)

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
