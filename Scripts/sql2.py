import sqlite3
conn= sqlite3.connect('mydatabase db')
cursor=conn.cursor()
cursor.executemany("INSERT INTO users(username,age,email),VALUES('Alice', 30, 'alice@gmail.com')")

#commit the transaction
conn.commit()
cursor.execute('SELECT * FROM users')
rows=cursor.fetchall()
for row in rows:
    print(row)

#retrive all datas:
cursor.execute('SELECT* FROM users')
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('SELECT* FROM users WHERE')

#update records:
cursor.execute("UPDATE users SET age=31 WHERE username='alice'")
conn.commit()

#Delete records:
cursor.execute("DELETE FROM users WHERE username='Bob'")
conn.commit()
