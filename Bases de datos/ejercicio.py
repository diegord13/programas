import sqlite3

conexion = sqlite3.connect("basededatos.db")

cursor =  conexion.cursor()

#cursor.execute("CREATE TABLE productos(id integer, nombre text, precio integer)")

#datos_productos = [(1,'Impresora',300),(2,'Raton',20),(3,'Ordenador', 600)]
#cursor.executemany("INSERT INTO productos VALUES(?,?,?)", datos_productos)
cursor.execute("SELECT * FROM productos ")
datos = cursor.fetchall()
for dato in datos:
	print(datos)

#conexion.commit()
conexion.close()