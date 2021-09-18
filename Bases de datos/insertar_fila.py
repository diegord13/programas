import sqlite3

conexion = sqlite3.connect("pwd.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO TABLA VALUES ('netacad', 'diegoard13@gmail.com', ' Sashalanegra@12')")

conexion.commit()

conexion.close()
