from datetime import date

def calcular_edad(nacimiento):
	fecha_actual = date.today()
	resultado = fecha_actual.year - nacimiento.year
	años = ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
	print(años)
	#mes = fecha_actual.month - nacimiento.month

	return resultado

date_entry = input('Ingrese una fecha con el siguiente formato YYYY-MM-DD ')
year, month, day = map(int, date_entry.split('-'))
fecha_nacimiento = date(year, month, day)
#print(ing_fecha)
#fecha_nacimiento=date(ing_fecha)
edad = calcular_edad(fecha_nacimiento)
print(f'la edad es {edad}.')