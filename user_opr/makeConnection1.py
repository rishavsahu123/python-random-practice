import mysql.connector

myDB = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='password',
    database='mydb'
)

mycursor = myDB.cursor()
try:
    mycursor.execute(
        'CREATE TABLE user(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(20))')
except:
    print('table already created')
else:
    print('table created successfully')
    