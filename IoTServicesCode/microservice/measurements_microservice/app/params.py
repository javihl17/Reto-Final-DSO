import os

def getParams ():
    dict = {
    "host":os.getenv('HOST'),
    "port":os.getenv('PORT'),
    "dbhost":os.getenv('DBHOST'),
    "dbuser":os.getenv('DBUSER'),
    "dbpassword":os.getenv('DBPASSWORD'),
    "dbdatabase":os.getenv('DBDATABASE')
}
    return dict