
def orden(lista1,lista2):
    porcentaje = []
    for i in range(len(lista1)):
        porcentaje.append(100-((lista2[i]*100)/(lista1[i])))
       

        print(f"{i + 1} {porcentaje[i]:.2f}%")

def mayor(lista):
    numero_mayor = lista[0]
    indice_mayor = 1
    for i in range(len(lista)):
        
        if lista[i] > numero_mayor:
            indice_mayor = i + 1
            numero_mayor = lista[i]
    
            
    
    return indice_mayor, numero_mayor

def menor(lista):

    
    numero_menor = lista[0]
    indice_menor = 1
    for i in range(len(lista)):
        if lista[i] < numero_menor:
            numero_menor = lista[i]
            indice_menor = i + 1
    
    return indice_menor,numero_menor

def promedio(lista1,lista2,a):
    resultado = []
    for i in range(a):
        resultado.append(lista1[i]-lista2[i])
        
    return resultado

def suma(x,a):
    suma = 0
    for i in range(a):
        suma += x[i]
    return suma
        
def ultimo(lista1, lista2):
    resultado = 0
    resultado2 = 0
    matriz1 =[]
    matriz2 =[]
    total = []
    for i in range(len(lista1)):
        resultado = 0
        resultado2 = 0
        
        resultado += lista1[i][0]
        resultado2 += lista2[i][0]
        matriz1.append(resultado)
        matriz2.append(resultado2)
        total.append(matriz2[i]-matriz1[i])
    return total
    


import copy

def entradas():
    # n cantidad de sucursales
    # k tipos de medicamento
    # cantidad de pacientes
    cantidad_sucursales = 0
    tipos_medicamentos = 0


    while cantidad_sucursales  <= 0 or tipos_medicamentos <1:
        entradas= input()
        cantidad_sucursales,tipos_medicamentos,pacientes = entradas.split()
        cantidad_sucursales = int(cantidad_sucursales)
        pacientes = int(pacientes)
        tipos_medicamentos = int(tipos_medicamentos)
        
    
    # medicamento sucursal es la matriz de tipos de medicamento por sucursal
    medicamento_sucursal = []
    med_sucursal = []
    for i in range(cantidad_sucursales):
    
      
        ingreso = input()
        ingreso = ingreso.split()
        medicamento_sucursal.append(ingreso)
        
        
        

    # volver enteros la matriz de tipos de medicamento por sucursal
    
    for i in range(cantidad_sucursales):
        for j in range(tipos_medicamentos):
            medicamento_sucursal[i][j]= int(medicamento_sucursal[i][j])
            med_sucursal = copy.deepcopy(medicamento_sucursal)
        
    
    # med_sucursal sera la matriz del tipo de medicamento ingresado original
    #med_sucursal = medicamento_sucursal
        
    # Entradas de paciente por sucursal, tipo de medicamento solicitado y cantidad de medicamento
    pac_sucursal_contador = []
    for i in range(pacientes):
        entradas2 = input()
        paciente_sucursal, tipo_med_solicitado, med_necesarias, pres_sis, pres_dias = entradas2.split()
        paciente_sucursal = int(paciente_sucursal) - 1
        tipo_med_solicitado = int(tipo_med_solicitado) - 1
        med_necesarias = int(med_necesarias)
        
        pac_sucursal_contador.append(paciente_sucursal+1)
   
# ----------------------------------------------------------------------------------------------
    pacientes_med1 = 0
    contador_paciente_sucursal = 0
    if  pres_dias == '0'  or pres_sis == '0':
        if pacientes == 0:
            porcentaje1 = pacientes * 100
        porcentaje1 = (pacientes_med1 * 100)/pacientes    
    else:
        presion_sistolica = int(pres_sis)
        presion_diastolica = int(pres_dias)
        pacientes = pacientes + 1

        if presion_sistolica < 89 and presion_diastolica < 53:
            medicamento_sucursal[paciente_sucursal][tipo_med_solicitado]  -= med_necesarias
                
        elif (89 <= presion_sistolica < 101) and (53 <= presion_diastolica < 71):
            medicamento_sucursal[paciente_sucursal][tipo_med_solicitado]  -= 0
                
        elif (101 <= presion_sistolica < 139) and (71 <= presion_diastolica < 88):     
            medicamento_sucursal[paciente_sucursal][tipo_med_solicitado]  -= 0
            
        elif (139 <= presion_sistolica < 156) and (88 <= presion_diastolica < 105):
            medicamento_sucursal[paciente_sucursal][tipo_med_solicitado]  -= med_necesarias
                    
        elif (156 <= presion_sistolica < 172) and (105 <= presion_diastolica < 124):
            medicamento_sucursal[paciente_sucursal][tipo_med_solicitado]  -= med_necesarias
                
        elif (172 <= presion_sistolica < 223) and (124 <= presion_diastolica < 143):
            medicamento_sucursal[paciente_sucursal][tipo_med_solicitado]  -= med_necesarias
                
        elif (223 <= presion_sistolica)  and (143 <= presion_diastolica):
            medicamento_sucursal[paciente_sucursal][tipo_med_solicitado]  -= med_necesarias
                
        elif (presion_sistolica >= 142) and (presion_diastolica < 103):
            medicamento_sucursal[paciente_sucursal][tipo_med_solicitado]  -= med_necesarias                
    
    
porcentaje1 = (pacientes_med1 * 100)/pacientes

return medicamento_sucursal,med_sucursal, cantidad_sucursales,pac_sucursal_contador,tipos_medicamentos


def principal():
    x,y,z,pac,a = entradas()
   
    
    for i in range(z):
        lista =[]
        lista2 = []
        print(i+1)
        contador = 0
        lista3 =[]
        for j in range(a):
            lista.append(x[i][j])
            lista2.append(y[i][j])
        for k in range(len(pac)):
            if pac[k] == i+1:
                contador += 1
        if contador == 0 or contador == 1:
            contador = 1
        
    
           
            
        men = menor(lista)
        may = mayor(lista)
        resultado = promedio(lista2,lista,a)
        
        ver_menor = menor(resultado)
        ver_mayor = mayor(resultado)
        prom = suma(resultado,a)/a
        
        
        print(f'{men[0]} {men[1]}\n{may[0]} {may[1]}\n{ver_menor[1]:.2f} {prom:.2f} {ver_mayor[1]:.2f}')
        print(f'{suma(resultado,a)/contador:.2f}')
        total = ultimo(x,y)
        total_men = menor(total)
        total_may = mayor(total)
    print(f'{total_men[0]} {total_men[1]}\n{total_may[0]} {total_may[1]}')
    
        
principal()


#

# #print (f'{pacientes}\n{pacientes_med1} {porcentaje1:.2f}%\n%')
# resultado_menor = menor(med_sucursal)
# resultado_mayor = mayor(med_sucursal)
# print(resultado_menor[0],resultado_menor[1])
# print(resultado_mayor[0],resultado_mayor[1])
# orden(medicamento_sucursal,med_sucursal)









