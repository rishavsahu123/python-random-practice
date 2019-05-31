import mysql.connector
from mysql.connector import Error
id = 1
try:
    print('1')
    myDB = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='password',
        database='his'
    )
except:
    print('2')
    print('oops test database is not available!, creating DB & user table...')
    myDB = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='password'
    )
    mycursor = myDB.cursor()
    mycursor.execute('CREATE DATABASE his')
    myDB = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='password',
        database='his'
    )
    mycursor.execute(
        'CREATE TABLE user (id INT AUTO_INCREAMENT PRIMARY KEY, name VARCHAR(30), password VARCHAR(50), email VARCHAR(50))')
else:
    print('3')
    mycursor = myDB.cursor()
    try:
        print('4')
        mycursor.execute("SELECT * FROM user")
    except:
        print('5')
        mycursor.execute(
            'CREATE TABLE user (id INT AUTO_INCREAMENT PRIMARY KEY, name VARCHAR(30), password VARCHAR(50), email VARCHAR(50))')
