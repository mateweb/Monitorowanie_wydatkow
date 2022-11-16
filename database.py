import sqlite3

db = sqlite3.connect('expenses3.db')
cursor = db.cursor()

cursor.execute('''

    CREATE TABLE expenses3 (
        id integer PRIMARY KEY NOT NULL,
        value integer,
        category string,
        date integer)

''')

db.commit()
db.close()
