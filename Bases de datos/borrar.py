import sqlite3

conexion = sqlite3.connect("pwd.db")

cursor = conexion.cursor()

cursor.execute("DROP TABLE TABLA ")

conexion.commit()

conexion.close()