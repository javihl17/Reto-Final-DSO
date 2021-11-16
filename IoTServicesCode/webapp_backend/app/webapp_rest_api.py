from flask import Flask, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route('/dso/measurements')
def get_sensor_data():
    id = request.args.get('id')
    measurements_microservice_server = os.getenv('MEASUREMENTS_MICROSERVICE_ADDRESS')
    measurements_microservice_port =  os.getenv('MEASUREMENTS_MICROSERVICE_PORT')
    response = requests.get('http://' + measurements_microservice_server + ':' + measurements_microservice_port + '/measurements/retrieve?id='+str(id))
    return response.content

@app.route('/dso/measurements_date')
def get_sensor_data_date():
    id = request.args.get('id')
    start = request.args.get('start')
    end = request.args.get('end')
    measurements_microservice_server = os.getenv('MEASUREMENTS_MICROSERVICE_ADDRESS')
    measurements_microservice_port =  os.getenv('MEASUREMENTS_MICROSERVICE_PORT')
    response = requests.get('http://' + measurements_microservice_server + ':' + measurements_microservice_port + '/measurements/retrieve_date?id='+str(id)+'&start='+str(start)+'&end='+str(end))
    return response.content

@app.route('/dso/devices/')
def get_device_list():
    devices_microservice_server = os.getenv('DEVICES_MICROSERVICE_ADDRESS')
    devices_microservice_port =  os.getenv('DEVICES_MICROSERVICE_PORT')
    response = requests.get('http://' + devices_microservice_server + ':' + devices_microservice_port + '/devices/retrieve/')
    return response.content

@app.route('/dso/device_info')
def get_device_info():
    id = request.args.get('id')
    devices_microservice_server = os.getenv('DEVICES_MICROSERVICE_ADDRESS')
    devices_microservice_port = os.getenv('DEVICES_MICROSERVICE_PORT')
    response = requests.get('http://' + devices_microservice_server + ':' + devices_microservice_port + '/devices/retrieve_by_id?id='+str(id))
    return response.content

app.run(host= os.getenv('HOST'), port=os.getenv('PORT'))
