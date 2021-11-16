from flask import Flask, request
from flask_cors import CORS
from measurements_manager import *
from params import getParams
paramsConection=getParams()

app = Flask(__name__)
CORS(app)

@app.route('/measurements/register/', methods=['POST'])
def set_measurement():
    params = request.get_json()
    measurements_register(params)
    return {"result":"record inserted"}, 201

@app.route('/measurements/retrieve')
def get_measurements():
    id = request.args.get('id')
    return measurements_retriever(id)

@app.route('/measurements/retrieve_date')
def get_measurements_date():
    start = request.args.get('start')
    end = request.args.get('end')
    id = request.args.get('id')
    return measurements_retriever_date(id, start, end)

app.run(host= paramsConection["host"], port=paramsConection["port"])
