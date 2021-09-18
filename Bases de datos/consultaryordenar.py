import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")

lista = cursor.fetchall()

for persona in lista:
	print(persona)


conexion.close()