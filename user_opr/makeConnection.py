import mysql.connector
from mysql.connector import Error
id = 1
try:
    print('1')
    myDB = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='password',
        database='test5'
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
    mycursor.execute('CREATE DATABASE test5')
    myDBs = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='password',
        database='test5'
    )
    mycursors = myDBs.cursor()
    import pdb;pdb.set_trace()
    mycursors.execute('CREATE TABLE student1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)')
   # mycursor.execute(
   #     'CREATE TABLE spa (id INT AUTO_INCREAMENT PRIMARY KEY, name VARCHAR(30))')
else:
    print('3')
    mycursor = myDB.cursor()
    try:
        print('4')
        mycursor.execute("SELECT * FROM user")
    except:
        print('5')
        mycursor.execute(
            'CREATE TABLE spa (id INT AUTO_INCREAMENT PRIMARY KEY, name VARCHAR(30), password VARCHAR(50), email VARCHAR(50))')
