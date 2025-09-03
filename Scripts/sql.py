import sqlite3

#connect to a data base(creates a new database)
conn=sqlite3.connect('mydatabase.db')

#create a cursor object to execute SQL commands:

cursor= conn.cursor()


#define table structure:

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE 
    )
    """)
cursor.execute('DELETE FROM users')

cursor.execute("INSERT INTO users (username, age, email) VALUES('alice', 30, 'alice123@gmail.com')")
users=[
    ('bob',25,'bob123@gmail.com'),
    ('sh',80,'sh123@gmail.com'),
    ('cat',1,'cat456@gmail.com')
]
cursor.executemany("INSERT INTO users (username,age,email) VALUES(?,?,?)",users)
cursor.execute( 'SELECT* FROM users')
rows=cursor.fetchall()


print('users in database:')
for row in rows:
    print(row)


conn.commit()
conn.close()

   