# Developer : khom
# Date: Tuesday, April 13, 2021
# Backend

import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE stocks ( date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2020-01-05','BUY', 'RHAT', 100, 35.14)")

# Sace (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()


