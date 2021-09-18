
def orden(lista1,lista2):
    porcentaje = []
    for i in range(len(lista1)):
        porcentaje.append(100-((lista2[i]*100)/(lista1[i])))
       

        print(f"{i + 1} {porcentaje[i]:.2f}%")


def mayor(lista):
    numero_mayor = lista[0]
    indice_mayor = 0
    for i in range(len(lista)):
        if lista[i] > numero_mayor:
            numero_mayor = lista[i]
            indice_mayor = i + 1
    
    return indice_mayor, numero_mayor



def menor(lista):
    numero_menor = lista[0]
    indice_menor = 0
    for i in range(len(lista)):
        if lista[i] <= numero_menor:
            numero_menor = lista[i]
            indice_menor = i + 1
    
    return indice_menor,numero_menor
	
def entradas():
       
    medicamento_sucursal = [] 
    cantidad_sucursales = 0
    cantidad_sucursales2 = 0
    ingreso_medicamento = 1

    while cantidad_sucursales  <= 0:
        cantidad_sucursal= input()
        cantidad_sucursales,pacientes = cantidad_sucursal.split()
        cantidad_sucursales = int(cantidad_sucursales)
        pacientes = int(pacientes)
        cantidad_sucursales2 = cantidad_sucursales

    while ingreso_medicamento >= 1 and cantidad_sucursales2 != 0:

        
        ingreso_medicamento = int(input())
        
        if ingreso_medicamento >= 1:
            medicamento_sucursal.append(ingreso_medicamento)
            cantidad_sucursales2 -= 1
            
        else:
            ingreso_medicamento = 1 
    #presiones(pacientes,medicamento_sucursal)
    
    

#def presiones(pacientes):

    paciente_sucursal = 0
    med_sucursal = medicamento_sucursal[:]
    pacientes_med1 = 0
    medicamento1 = 0
    
    for i in range(pacientes):
        entradas = input()
        paciente_sucursal, pres_sis,pres_dias = entradas.split()
        paciente_sucursal = int(paciente_sucursal)
        if paciente_sucursal > cantidad_sucursales:
        
            break
        
        #paciente_sucursal.append(input('ingrese en que sucursal va a ser atendido'))
        # pres_sis = input()
        # pres_dias = input()
        paciente_sucursal = paciente_sucursal - 1
        
    
        if  pres_dias == '0'  or pres_sis == '0':
            if pacientes == 0:
                
                porcentaje1 = pacientes * 100
                        
                break
            porcentaje1 = (pacientes_med1 * 100)/pacientes
            
            break
        else:
            presion_sistolica = int(pres_sis)
            presion_diastolica = int(pres_dias)
            pacientes = pacientes + 1

            if presion_sistolica < 89 and presion_diastolica < 53:
                med_sucursal[paciente_sucursal] = med_sucursal[paciente_sucursal] - 9
                pacientes_med1 = pacientes_med1 + 1
                
            elif (89 <= presion_sistolica < 101) and (53 <= presion_diastolica < 71):
                med_sucursal[paciente_sucursal] = med_sucursal[paciente_sucursal] - 0
                
            elif (101 <= presion_sistolica < 139) and (71 <= presion_diastolica < 88):
                med_sucursal[paciente_sucursal] = med_sucursal[paciente_sucursal] - 0
                
            elif (139 <= presion_sistolica < 156) and (88 <= presion_diastolica < 105):
                med_sucursal[paciente_sucursal] = med_sucursal[paciente_sucursal] - 2
                pacientes_med1 = pacientes_med1 + 1
                
                
            elif (156 <= presion_sistolica < 172) and (105 <= presion_diastolica < 124):
                med_sucursal[paciente_sucursal] = med_sucursal[paciente_sucursal] - 7
                pacientes_med1 = pacientes_med1 + 1
                
            elif (172 <= presion_sistolica < 223) and (124 <= presion_diastolica < 143):
                med_sucursal[paciente_sucursal] = med_sucursal[paciente_sucursal] - 13
                pacientes_med1 = pacientes_med1 + 1
                
            elif (223 <= presion_sistolica)  and (143 <= presion_diastolica):
                med_sucursal[paciente_sucursal] = med_sucursal[paciente_sucursal] - 25
                pacientes_med1 = pacientes_med1 + 1
                
            elif (presion_sistolica >= 142) and (presion_diastolica < 103):
                med_sucursal[paciente_sucursal] = med_sucursal[paciente_sucursal] - 16
                pacientes_med1 = pacientes_med1 + 1
                    
            porcentaje1 = (pacientes_med1 * 100)/pacientes
        


    #print (f'{pacientes}\n{pacientes_med1} {porcentaje1:.2f}%\n%')
    resultado_menor = menor(med_sucursal)
    resultado_mayor = mayor(med_sucursal)
    print(resultado_menor[0],resultado_menor[1])
    print(resultado_mayor[0],resultado_mayor[1])
    orden(medicamento_sucursal,med_sucursal)
    
entradas()







