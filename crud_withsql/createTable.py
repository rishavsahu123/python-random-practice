import mysql.connector
myDB = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password',
    database = 'mydb'
)

mycursor = myDB.cursor()
try:
    mycursor.execute('CREATE TABLE student1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)')
except:
    print('error')