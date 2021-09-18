import sqlite3

conexion = sqlite3.connect("pwd.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE TABLA(aplicativo TEXT, usuario TEXT, contraseña text)")

conexion.commit()

conexion.close()