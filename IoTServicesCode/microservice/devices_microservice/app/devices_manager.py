import time

import mysql.connector, json
from params import getParams
paramsConection = getParams()

def connect_database ():
    mydb = mysql.connector.connect(
        host = paramsConection["dbhost"],
        user = paramsConection["dbuser"],
        password = paramsConection["dbpassword"],
        database = paramsConection["dbdatabase"]
    )
    return mydb

def devices_retriever():
    mydb = connect_database()
    r = []
    with mydb.cursor() as mycursor:
        mycursor.execute("SELECT device_id, status, latitude, longitude, time_stamp FROM devices ORDER BY id DESC;")
        myresult = mycursor.fetchall()
        for device_id, status, latitude, longitude, time_stamp in myresult:
            location = str(latitude)+"; "+str(longitude)
            r.append({"device_id": device_id, "status":status, "location": location, "time_stamp":time_stamp})
        mydb.commit()
    return json.dumps(r)

def devices_regiter(params):
    print("Se registra un nuevo device:")
    print(params["device_id"])
    mydb = connect_database()
    with mydb.cursor() as mycursor:
        sql = "SELECT * FROM devices WHERE device_id = %s ;"

        try:
            mycursor.execute(sql, (params["device_id"],))
            mycursor.fetchall()
            if (mycursor.rowcount == 0):
                firstInsert (params)
            else:
                updateDevice(params)
            mydb.commit()
        except:
            print("Something went wrong, please, try again.")

    updateDevice(params)

def firstInsert (params):
    mydb = connect_database()
    with mydb.cursor() as mycursor:
        sql = "INSERT INTO devices (device_id, time_stamp, latitude, longitude) VALUES (%s, %s, %s, %s) ;"
        device_data = (params["device_id"],params["time_stamp"], params["latitude"], params["longitude"])
        try:
            mycursor.execute(sql, device_data)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except:
            print("Error inserting the device")

def updateDevice(params):
    mydb = connect_database()
    print("Se update un device:")
    print(params["device_id"])
    with mydb.cursor() as mycursor:
        sql = "UPDATE devices SET status = 'activo', time_stamp = %s, latitude = %s, longitude = %s WHERE device_id = %s;"
        try:
            mycursor.execute(sql, (params["time_stamp"], params["latitude"], params["longitude"], params["device_id"]))
            mydb.commit()
            print(mycursor.rowcount, "record updated.")
        except:
            print("Error inserting the device")

def device_retriever_by_id(id):
    mydb = connect_database()
    r = []
    with mydb.cursor() as mycursor:
        mycursor.execute("SELECT device_id, status, latitude, longitude FROM devices WHERE device_id='" + str(id) + "';")
        myresult = mycursor.fetchall()
        for device_id, status, latitude, longitude in myresult:
            location = str(latitude) + "; " + str(longitude)
            r.append({"device_id": device_id, "status":status, "location": location })
        mydb.commit()
    return json.dumps(r)


def device_disconnecter(params):
    mydb = connect_database()
    print("Parametros: ")
    print(params)
    with mydb.cursor() as mycursor:
        timestamp = time.time()
        sql = "UPDATE devices SET status = %s, time_stamp = "+str(timestamp)+" WHERE device_id = %s;"
        print(sql)
        try:
            mycursor.execute(sql, ('inactivo', params["device_id"]))
            mydb.commit()
            print(mycursor.rowcount, "record updated.")
        except:
            print("Error disconnecting the device")
