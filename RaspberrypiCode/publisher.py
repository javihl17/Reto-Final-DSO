import json
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected succes")
    else:
        print("Connected fail with code", {rc})

client = mqtt.Client()
def make_connection(id):
    client.username_pw_set(username="dso_server_jj", password="dso_password_jj")
    client.on_connect = on_connect
    data = {"device_id": id}
    data = json.dumps(data)
    client.will_set("/lastwill", payload=data, qos=0, retain=False)
    client.connect("34.107.40.116", 1883, 60)

def send_measures(id, temperature, humidity, timestamp):
    data = {"device_id": id, "temperature":temperature, "humidity":humidity, "time_stamp":timestamp}
    data = json.dumps(data)
    client.publish('/measures', payload=data, qos=0, retain=False)

'''def send_location(id, latitude, longitude):
    data = {"device_id":id, "latitude":latitude, "longitude":longitude}
    data = json.dumps(data)
    client.publish('/locations', payload=data, qos=0, retain=False)'''

def send_id(id, timestamp, longitude, latitude):
    data = {"device_id":id, "time_stamp":timestamp, "latitude":latitude, "longitude":longitude}
    data = json.dumps(data)
    client.publish('/devices', payload=data, qos=0, retain=False)
