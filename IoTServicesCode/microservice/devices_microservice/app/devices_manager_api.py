from flask import Flask, request
from flask_cors import CORS
from devices_manager import *
from params import getParams
paramsConection = getParams()

app = Flask(__name__)
CORS(app)

@app.route('/devices/register/', methods=['POST'])
def save_deviceinfo():
    params = request.get_json()
    devices_regiter(params)
    return {"result": "record inserted"}, 201

@app.route('/devices/retrieve/')
def retrieve_devices():
    return devices_retriever()

@app.route('/devices/retrieve_by_id')
def retrieve_by_id():
    id = request.args.get('id')
    return device_retriever_by_id(id)

@app.route('/devices/disconnect', methods=['POST'])
def disconnect_device():
    params = request.get_json()
    device_disconnecter(params)
    return {"result": "device disconnected"}, 201

app.run(host= paramsConection["host"], port=paramsConection["port"])
