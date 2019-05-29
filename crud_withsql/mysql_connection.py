import mysql.connector

myDB = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'password'
)

mycursor = myDB.cursor()
try:
    mycursor.execute('SHOW DATABASES')
except:
    mycursor.execute('CREATE DATABASE mydb')
else:
    for x in mycursor:
        print(x)