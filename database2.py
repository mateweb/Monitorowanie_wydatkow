import sqlite3

db2 = sqlite3.connect('incomes.db')
cursor = db2.cursor()

cursor.execute('''

    CREATE TABLE incomes (
        value integer,
        category string,
        date integer)

''')

db2.commit()
db2.close()
