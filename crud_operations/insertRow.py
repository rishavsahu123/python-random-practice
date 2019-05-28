import sqlite3
db = sqlite3.connect('test.db')
qry = 'insert into Student (name, age, marks) values ("Rishav", 25, 70);'
try:
    cur = db.cursor()
    cur.execute(qry)
    db.commit()
    print('one record added successfully')
except:
    print('error in operation')
    db.rollback()
db.close()