import serial
import string
import pynmea2

port = "/dev/ttyAMA0"

def get_coordinates():
    while(True):
        ser = serial.Serial(port, baudrate=9600)
        dataout = pynmea2.NMEAStreamReader()
        newdata = ser.readline()

        if newdata[0:6] == b'$GPRMC':
            newmsg = pynmea2.parse(newdata.decode('utf-8'))
            lat = newmsg.latitude
            lng = newmsg.longitude
            return tuple((lat, lng))