import sqlite3
db = sqlite3.connect('test.db')
sql = ' SELECT * FROM student'
cur = db.cursor()
cur.execute(sql)
print(cur.fetchone())

db.close()