
presion_sistolica = int(input('Ingresa el valor de la presion sistolica ' ))
presion_diastolica = int(input('Ingresa el valor de la presion diastolica ' ))


#def presion(presion_sistolica,presion_diastolica):

if presion_sistolica < 89 and presion_diastolica < 53:
	print('Hipotension Alerta Amarilla')
elif (89 <= presion_sistolica < 101) and (53 <= presion_diastolica < 71):
	print('Ideal Alerta Verde')
elif (101 <= presion_sistolica < 139) and (71 <= presion_diastolica < 88):
	print('Comun Alerta Verde')
elif (139 <= presion_sistolica < 156) and (88 <= presion_diastolica < 105):
	print('Comun-alta Alerta Amarilla')
elif (156 <= presion_sistolica < 172) and (105 <= presion_diastolica < 124):
	print('HTAG1 Alerta Naranja')
elif (172 <= presion_sistolica < 223) and (124 <= presion_diastolica < 143):
	print('HTAG2 Alerta Naranja')
elif (156 <= presion_sistolica)  and (143 <= presion_diastolica):
	print('HTAG3 Alerta Roja')
elif (presion_sistolica >= 142) and (presion_diastolica < 103):
	print('HTASA Alerta Roja')
else:
	print('No se puede determinar la categoria Alerta Gris')




