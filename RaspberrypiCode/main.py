import time
import I2C_LCD_driver
import RPi.GPIO as GPIO
import threading
import uuid
import adafruit_dht as dht
import signal
import datetime
from datetime import date
#from openpyxl import load_workbook
from publisher import *
from board import *
from GPS import *

BUTTON_GPIO = 12
mylcd = I2C_LCD_driver.lcd()
worker = False

id = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                  for ele in range(0,8*6,8)][::-1])

def weatherSensor():
    make_connection(id)
    print(id)
    #send_id(id+" -Raspberry 1")

def measureToSend():

    DHT_PIN = D4
    dht11 = dht.DHT11(DHT_PIN, use_pulseio=False)
    newtemperature = 0
    timestamp_measures = 0
    timestamp_location = 0

    while True:
        # Manda el dispositivo con su localización al inicio y cada 1 hora
        if time.time()-timestamp_location>3600:
            timestamp_location = time.time()
            location = get_coordinates()
            print(location)
            send_id(id,time.time(), location[0], location[1])

        # Registra y manda las medidas al inicio y cada 1 minuto
        temperature = None
        humidity = None
        try:
            dht11.measure()
            temperature = dht11.temperature
            humidity = dht11.humidity
        except:
            print("Error measuring")

        if temperature is not None and humidity is not None:
            if(newtemperature != temperature or (time.time()-timestamp_measures)>60):
                newtemperature = temperature
                timestamp_measures = time.time()
                send_measures(id, newtemperature, humidity, timestamp_measures)
                print("Temp: {0:0.1f}C ".format(temperature))
                print("Hum: {0:0.1f}% ".format(humidity))
                print("Timestamp: "+str(timestamp_measures))
        else:
            print("Sensor failure. Check wiring")


def show_temperature():
    DHT_PIN = D4
    dht11 = dht.DHT11(DHT_PIN, use_pulseio=False)

    newhumidity = 0

    humidity = None

    try:
        dht11.measure()
        humidity = dht11.humidity
    except:
        mylcd.lcd_display_string("Error measuring the humidity")
        time.sleep(3)
        mylcd.lcd_clear()

    if humidity is not None:
        if (newhumidity != humidity):
            newhumidity = humidity
            mylcd.lcd_display_string("Humidity: " + str(humidity))
            time.sleep(1)
            mylcd.lcd_clear()
            # send_humidity(humidity)
    else:
        mylcd.lcd_display_string("Sensor failure. Check wiring")
        time.sleep(3)
        mylcd.lcd_clear()

def show_humidity():
    DHT_PIN = D4
    dht11 = dht.DHT11(DHT_PIN, use_pulseio=False)

    newtemperature = 0

    temperature = None

    try:
        dht11.measure()
        temperature = dht11.temperature
    except:
        mylcd.lcd_display_string("Error measuring the temperature")
        time.sleep(3)
        mylcd.lcd_clear()

    if temperature is not None:
        if (newtemperature != temperature):
            newtemperature = temperature
            mylcd.lcd_display_string("Temperature: " + str(temperature))
            time.sleep(1)
            mylcd.lcd_clear()
            # send_temperature(temperature)
    else:
        mylcd.lcd_display_string("Sensor failure. Check wiring")
        time.sleep(3)
        mylcd.lcd_clear()

def manager_callback(channel):
    global worker
    print("Has cambiado de modo")
    if worker:
        worker = False
    else:
        worker = True

def signal_handler(sig, frame):
    GPIO.cleanup()
    mylcd.lcd_clear()
    sys.exit(0)

def show():
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, callback=manager_callback, bouncetime=200)
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        if worker:
            show_humidity()
        else:
            show_temperature()


if __name__ == "__main__":


    sending_thread = threading.Thread(target=measureToSend, daemon=True, name = "s_thread")
    weatherSensor()
    sending_thread.start()
    show()
    sending_thread.join()

    # Cear threads para la toma de temperatura y humedad
    '''humidity = threading.Thread(target=humiditySensor, daemon=True, name = "h_thread")
    temperature = threading.Thread(target=temperatureSensor, name = "t_thread")
    humidity.start()
    temperature.start()
    humidity.join()
    temperature.join()'''
