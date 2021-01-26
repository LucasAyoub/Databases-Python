import sqlite3
import pandas as pd
query = """
CREATE TABLE TESTE
(Cidade VARCHAR(20), 
 Estado VARCHAR(20),
 taxa REAL,        
 Impostos INTEGER
);"""
con = sqlite3.connect('Python.db')
con.execute(query)
con.commit()

data = [('Natal', 'Rio Grande do Norte', 1.25, 6),
        ('Recife', 'Pernambuco', 2.6, 3),
        ('Londrina', 'Paraná', 1.7, 5)]
stmt = "INSERT INTO TESTE VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()

cursor = con.execute('select * from TESTE')
rows = cursor.fetchall()
rows

cursor.description
pd.DataFrame(rows, columns=[x[0] for x in cursor.description])