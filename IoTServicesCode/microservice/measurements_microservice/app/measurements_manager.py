import json

import mysql.connector
from params import getParams
paramsConection=getParams()

def connect_database ():

    mydb = mysql.connector.connect(
        host = paramsConection["dbhost"],
        user = paramsConection["dbuser"],
        password = paramsConection["dbpassword"],
        database = paramsConection["dbdatabase"]
    )
    return mydb

def measurements_retriever(id):
    mydb = connect_database()
    r = []
    with mydb.cursor() as mycursor:
        mycursor.execute("SELECT temperature, humidity, time_stamp FROM sensor_data WHERE device_id='"+str(id)+"';")
        myresult = mycursor.fetchall()
        for temperature, humidity, time_stamp in myresult:
            r.append({"temperature": temperature, "humidity": humidity, "time_stamp": time_stamp})
        mydb.commit()
    return json.dumps(r)

def measurements_retriever_date(id, start, end):
    mydb = connect_database()
    r = []
    with mydb.cursor() as mycursor:
        mycursor.execute("SELECT temperature, humidity, time_stamp FROM sensor_data WHERE device_id='"+str(id)+"' and time_stamp>="+str(start)+" and time_stamp<="+str(end)+";")
        myresult = mycursor.fetchall()
        for temperature, humidity, time_stamp in myresult:
            r.append({"temperature": temperature, "humidity": humidity, "time_stamp": time_stamp})
        mydb.commit()
    return json.dumps(r)

def measurements_register(params):
    mydb = connect_database()
    with mydb.cursor() as mycursor:
        sql = "INSERT INTO sensor_data (device_id, temperature, humidity, time_stamp) VALUES (%s, %s, %s, %s)"
        val = (params["device_id"], params["temperature"], params["humidity"], params["time_stamp"])
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
