import sqlite3

db2 = sqlite3.connect('incomes.db')
cursor2 = db2.cursor()

cursor2.execute('''

    CREATE TABLE incomes (
        id2 integer PRIMARY KEY NOT NULL,
        value integer,
        category string,
        date integer)

''')

db2.commit()
db2.close()
