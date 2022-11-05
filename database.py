import sqlite3

db = sqlite3.connect('expenses.db')
cursor = db.cursor()

cursor.execute('''

    CREATE TABLE expenses (
        id integer,
        value integer,
        category string)

''')

db.commit()
db.close()
