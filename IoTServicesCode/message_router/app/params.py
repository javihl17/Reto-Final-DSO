import os

def getParams ():
    dict = {
    "broker_address":os.getenv('BROKER_ADDRESS'),
    "broker_port":int(os.getenv('BROKER_PORT')),
    "broker_keep_alive":int(os.getenv('BROKER_KEEP_ALIVE')),
    "broker_user":os.getenv('BROKER_USER'),
    "broker_pwd":os.getenv('BROKER_PWD'),
    "measurements_microservice_address":os.getenv('MEASUREMENTS_MICROSERVICE_ADDRESS'),
    "measurements_microservice_port":int(os.getenv('MEASUREMENTS_MICROSERVICE_PORT')),
    "devices_microservice_address":os.getenv('DEVICES_MICROSERVICE_ADDRESS'),
    "devices_microservice_port":int(os.getenv('DEVICES_MICROSERVICE_PORT'))
    }
    return dict