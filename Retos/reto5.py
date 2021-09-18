import csv
import numpy as np
import statistics

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



def nueva_matrix(lista, i):
    contador_hombres = 0
    contador_mujeres = 0
    lista_indice = []
    for n in range(len(i)):
        lista_indice.append(lista[i[n]])
        if lista[i[n]][2] == "f":
            contador_mujeres = contador_mujeres + 1
        else:
            contador_hombres = contador_hombres + 1
    total = contador_hombres + contador_mujeres
    return contador_hombres, contador_mujeres, total, lista_indice

def probabilidad(lista):
    lista_medicados = []
    contador_medicamento_medicados = 0
    for m in range(len(lista)):
        lista_medicados.append(int(lista[m][7]))
        contador_medicamento_medicados +=  int(lista[m][7])
    return lista_medicados, contador_medicamento_medicados

def condicional(nueva_lista_medicados):
    no_medicados = []
    for i in range(len(nueva_lista_medicados)):
        
        if  nueva_lista_medicados[i][8] != '0'  or nueva_lista_medicados[i][9] != '0':

            presion_sistolica = int(nueva_lista_medicados[i][8])
            presion_diastolica = int(nueva_lista_medicados[i][9])
            

            if presion_sistolica < 89 and presion_diastolica < 53:
                no_medicados.append(i)
                
            elif (89 <= presion_sistolica < 101) and (53 <= presion_diastolica < 71):
                pacientes = 0
                
            elif (101 <= presion_sistolica < 139) and (71 <= presion_diastolica < 88):     
                pacientes = 0
                
            elif (139 <= presion_sistolica < 156) and (88 <= presion_diastolica < 105):
                no_medicados.append(i)
                    
            elif (156 <= presion_sistolica < 172) and (105 <= presion_diastolica < 124):
                no_medicados.append(i)
            elif (172 <= presion_sistolica < 223) and (124 <= presion_diastolica < 143):
                no_medicados.append(i)
            elif (223 <= presion_sistolica)  and (143 <= presion_diastolica):
                no_medicados.append(i) 
            elif (presion_sistolica >= 142) and (presion_diastolica < 103):
                no_medicados.append(i)
    pacientes_medicados = nueva_matrix(nueva_lista_medicados,no_medicados)
    return pacientes_medicados
   
def testCSV():
    #entrada = entradas()
    entrada = []
    lista_entrada = input()
    entrada = lista_entrada.split()
    entrada = [int(x) for x in entrada]
    entrada.sort()
    entrada = [str(x) for x in entrada]
    
    

    for n in range(len(entrada)):
        archivo =  open('data.csv', mode='r', encoding='utf-8-sig' ) 
        lector = csv.reader(archivo) #Retorna un objeto con las filas del csv

        lista = []
        medicados = []
        no_medicados = []
        contador_medicamento_total = 0
        sexo = 0
        
        

        for fila in lector: #Este va a recorrer cada fila
            lista.append(fila)
            
         
        for i in range(1,len(lista)):
            if lista[i][5] == entrada[n]:
                valor = i
                medicados.append(i)
                contador_medicamento_total +=  int(lista[i][7])
                resultados = nueva_matrix(lista, medicados)

        nueva_lista_medicados = (resultados[3])
        
        resultados2 = probabilidad(nueva_lista_medicados)
        resultados3 = condicional(nueva_lista_medicados)
        resultados5 = resultados3[3]
        resultados4 = probabilidad(resultados3[3])
        
        res_menor = menor(resultados4[0])
        res_mayor = mayor(resultados4[0])
        
        

    

        print(f'{nueva_lista_medicados[0][5]} {nueva_lista_medicados[0][3]} {nueva_lista_medicados[0][4]}')
        print(f'patients')
        print(f'male {resultados[0]}\nfemale {resultados[1]}\ntotal {resultados[2]}\nmedicine quantity\nmean {np.mean(resultados2[0]):.2f}\nstd {statistics.stdev(resultados2[0]):.2f}')
        print(f'min {menor(resultados2[0])[1]}\nmax {mayor(resultados2[0])[1]}\ntotal {contador_medicamento_total}')
        print(f'scheduled patients\nmale {resultados3[0]}\nfemale {resultados3[1]}\ntotal {resultados3[2]}')
        print(f'scheduled medicine quantity\nmean {np.mean(resultados4[0]):.2f}\nstd {statistics.stdev(resultados4[0]):.2f}')
        print(f'min {res_menor[1]} {resultados5[res_menor[0]-1][0]} {resultados5[res_menor[0]-1][1]} {resultados5[res_menor[0]-1][2]} {resultados5[res_menor[0]-1][6]}')
        print(f'max {res_mayor[1]} {resultados5[res_mayor[0]-1][0]} {resultados5[res_mayor[0]-1][1]} {resultados5[res_mayor[0]-1][2]} {resultados5[res_mayor[0]-1][6]}')
        print(f'total {resultados4[1]}')
testCSV()


