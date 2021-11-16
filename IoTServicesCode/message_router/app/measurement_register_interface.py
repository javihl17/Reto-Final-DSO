# insert IoT data into data store through REST API

import requests
from params import getParams
paramsConection=getParams()

def submit_data_to_store (data):
    r = requests.post('http://' + str(paramsConection["measurements_microservice_address"]) + ':' + str(paramsConection["measurements_microservice_port"]) + '/measurements/register', json=data)
