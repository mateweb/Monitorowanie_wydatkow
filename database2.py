import sqlite3

db = sqlite3.connect('expenses.db')
cursor = db.cursor()

cursor.execute('''

    insert into expenses (id, value, category) values (1, 500, 'Sparkonto')

''')

db.commit()
db.close()
