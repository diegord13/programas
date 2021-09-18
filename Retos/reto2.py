
medicamento1 = int(input())
medicamento2 = int(input())
pacientes = 0
pacientes_med1 = 0
pacientes_med2 = 0



while medicamento1 >= 0 and medicamento2 >= 0:
	
	if medicamento1 == 0 or medicamento2==0:
		if pacientes == 0:
		
			porcentaje1 = pacientes * 100
			porcentaje2 = pacientes * 100	
			break
		else:
			break	
		
	pres_sis = input()

	pres_dias = input()

	if  pres_dias == '0'  or pres_sis == '0':
		if pacientes == 0:
			
			porcentaje1 = pacientes * 100
			porcentaje2 = pacientes * 100			
			break
		porcentaje1 = (pacientes_med1 * 100)/pacientes
		porcentaje2 = (pacientes_med2 * 100)/pacientes	
		break
	else:
		presion_sistolica = int(pres_sis)
		presion_diastolica = int(pres_dias)
		pacientes = pacientes + 1

		if presion_sistolica < 89 and presion_diastolica < 53:
			medicamento2 = medicamento2 - 9
			pacientes_med2 = pacientes_med2 + 1
			
		elif (89 <= presion_sistolica < 101) and (53 <= presion_diastolica < 71):
			medicamento1 = medicamento1 - 0
			
		elif (101 <= presion_sistolica < 139) and (71 <= presion_diastolica < 88):
			medicamento1 = medicamento1 - 0
			
		elif (139 <= presion_sistolica < 156) and (88 <= presion_diastolica < 105):
			medicamento1 = medicamento1 - 2
			pacientes_med1 = pacientes_med1 + 1
			
			
		elif (156 <= presion_sistolica < 172) and (105 <= presion_diastolica < 124):
			medicamento1 = medicamento1 - 7
			pacientes_med1 = pacientes_med1 + 1
			
		elif (172 <= presion_sistolica < 223) and (124 <= presion_diastolica < 143):
			medicamento1 = medicamento1 - 13
			pacientes_med1 = pacientes_med1 + 1
			
		elif (156 <= presion_sistolica)  and (143 <= presion_diastolica):
			medicamento1 = medicamento1 - 25
			pacientes_med1 = pacientes_med1 + 1
			
		elif (presion_sistolica >= 142) and (presion_diastolica < 103):
			medicamento1 = medicamento1 - 16
			pacientes_med1 = pacientes_med1 + 1
				
		porcentaje1 = (pacientes_med1 * 100)/pacientes
		porcentaje2 = (pacientes_med2 * 100)/pacientes	

print (f'{pacientes}\n{pacientes_med1} {porcentaje1:.2f}%\n{pacientes_med2} {porcentaje2:.2f}%')




	
