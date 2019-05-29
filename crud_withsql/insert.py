import mysql.connector

myDB = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password',
    database = 'mydb'
)

mycursor = myDB.cursor()

sql = "INSERT INTO student1 (name, age) VALUES (%s, %s)"
val = ("John",  "21")
mycursor.execute(sql, val)
mycursor.execute('SELECT * FROM student1')
result = mycursor.fetchall()
for x in result:
    print(x)
myDB.commit()
print('raw inserted')