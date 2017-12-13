# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:26:41 2017

@author: poaa
"""
import sqlite3
conn = sqlite3.connect(r'C:\Users\poaa\AppData\Local\Continuum\anaconda3\Library\bin\test.db')
c = conn.cursor()
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

