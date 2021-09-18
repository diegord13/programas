import sqlite3

conexion =sqlite3.connect("pwd.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM TABLA ")

personas = cursor.fetchall()

for persona in personas:
	print(persona)

conexion.close()