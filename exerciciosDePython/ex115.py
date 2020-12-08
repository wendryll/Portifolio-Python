from SGBD_config import *
import mysql.connector

db = mysql.connector.connect(host=HOST,
                    user=USERNAME,
                    password=PASSWORD,
                    database=DBNAME)

cursor = db.cursor()
"""print('-'*40)

cursor.execute('SELECT * FROM Fabricante')
fabricantes = cursor.fetchall()
for fabricante in fabricantes:
    print(fabricante)

cursor.execute("desc Fabricante")
print(cursor.fetchall())

cursor.execute('UPDATE Fabricante SET razão_social_fabricante = "Volkswagen Group AG" WHERE id_fabricante = "15"')

cursor.execute("INSERT INTO Fabricante VALUES (default,'FCA (Fiat Chrysler Automobiles)')")

db.commit() """

cursor.execute('SELECT * FROM Fabricante')
fabricantes = cursor.fetchall()
for fabricante in fabricantes:
    print(fabricante)