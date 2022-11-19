import sqlite3

db = sqlite3.connect('expenses_and_incomes.db')
cursor = db.cursor()
cursor2 = db.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS expenses(
	id integer PRIMARY KEY NOT NULL,
	value integer,
    category string,
    date DATETIME DEFAULT CURRENT_TIMESTAMP);
    
''')

cursor2.execute('''

    CREATE TABLE IF NOT EXISTS incomes(
	id integer PRIMARY KEY NOT NULL,
	value integer,
    category string,
    date DATETIME DEFAULT CURRENT_TIMESTAMP);

''')



db.commit()
db.close()
