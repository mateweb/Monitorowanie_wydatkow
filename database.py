import sqlite3

conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()
#cursor.execute("""CREATE TABLE expenses (
                #expense integer,
                #category text,
                #month integer
                #)""")    

cursor.execute("INSERT INTO expenses VALUES ('500', 'Sparkonto', '11'")

conn.commit()

conn.close()
