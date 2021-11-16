import json

import paho.mqtt.client as paho
from measurement_register_interface import *
from device_register_interface import *
import sys
from params import getParams
paramsConection = getParams()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
        client.subscribe("/measures")
        client.subscribe("/lastwill")
        client.subscribe("/devices")
    else:
        print("Connected fail with code", {rc})


# define mqtt callback
def on_message(client, userdata, message):

    print("received message =", str(message.payload.decode("utf-8")))
    if message.topic == "/measures":
        measures = json.loads(message.payload.decode("utf-8"))
        submit_data_to_store(measures)
    if message.topic == "/devices":
        r = json.loads(message.payload.decode("utf-8"))
        submit_device_info_to_store(r)
        print(r)
    if message.topic == "/lastwill":
        r = json.loads(message.payload.decode("utf-8"))
        print(r)
        disconnect_device(r)



# Create client object client1.on_publish = on_publish #assign function to callback client1.connect(paramsConection[broker],paramsConection[port]) #establish connection client1.publish("house/bulb1","on")

client=paho.Client()
client.username_pw_set(username=paramsConection["broker_user"], password=paramsConection["broker_pwd"])
client.on_connect = on_connect
# Bind function to callback
client.on_message=on_message
# Initializate cursor instance
print("connecting to broker ",paramsConection["broker_address"])
client.connect(paramsConection["broker_address"], paramsConection["broker_port"], paramsConection["broker_keep_alive"] ) # connect
# Start loop to process received messages
client.loop_forever()
