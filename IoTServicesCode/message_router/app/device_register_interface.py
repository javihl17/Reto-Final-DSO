import requests
from params import getParams
paramsConection=getParams()

def submit_device_info_to_store (data):
    print("host y puerto:")
    print(paramsConection["devices_microservice_address"])
    print(paramsConection["devices_microservice_port"])
    r = requests.post('http://' + str(paramsConection["devices_microservice_address"]) + ':' + str(paramsConection["devices_microservice_port"]) + '/devices/register', json=data)

def disconnect_device(data):
    print("host y puerto:")
    print(paramsConection["devices_microservice_address"])
    print(paramsConection["devices_microservice_port"])
    r = requests.post('http://' + str(paramsConection["devices_microservice_address"]) + ':' + str(paramsConection["devices_microservice_port"]) + '/devices/disconnect', json=data)
