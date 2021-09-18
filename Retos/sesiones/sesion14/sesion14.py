"""
Matrices o vectores bidimensionales

Vamos a continuar con el trabajo de matrices usando lista de listas. 
Como vimos en la sesión anterior, las operaciones de este tipo de matrices se pueden realizar con ciclos anidados.
"""
def imprimirMatriz(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end='\t')
        print()
#Actividad 1

#Escribe una función actividad1(x) que imprima la diagonal principal de una matriz x. 
#Asegúrate de validar si la matriz es cuadrada, sino devuelve un mensaje, "La matriz no es cuadrada"


#actividad1([[1,1],[2,7,2],[3,3,3]])

#Actividad 2

def actividad2():
    x = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(int(input()))
        x.append(fila)    
        
    print(f'{x[0][:]}')
    print(f'{x[0][0]} {x[1][0]} {x[2][0]} ')
    print(x[0][0])
        
    imprimirMatriz(x)
    


#
#Creemos ahora una función actividad2() que reciba los elementos de una matriz 3x3 e imprima:
#
#   - La primera fila
#   - La primera columna
#   - Accede al elemento en la fila 1, columna 1.
#
#Los valores son ingresados por filas [0][1], [0][2], [0][3], [1][0], etc


#actividad2()




def actividad1(X):

    print("La matriz ingresada es:")
    imprimirMatriz(X)

    es_cuadrada = True
    for i in range(len(X)):
        if len(X) != len(X[i]):
            es_cuadrada = False
            break
    
    if es_cuadrada:
        print("La diagonal principal de la matriz es:")
        for i in range(len(X)):
            print(X[i][i], end=' ')

    else:
        print("La matriz no es cuadrada.")


#actividad1([[1,1,2],
            # [2,7,2],
            # [3,3,3]])





import os

from numpy.core.fromnumeric import reshape, resize
def limpiarPantalla():
    os.system("cls")
# Actividad 4: Cree un programa que genere un vector de n elementos aleatorios entre 1 y 1000. 
# Luego cree funciones para búsqueda y ordenamiento del vector. En su programa coloque un menú 
# para que el usuario pueda usar cualquiera de las dos funciones hasta que elija una opción de salir.
def llenarVectorAleatorio(tamano, num_inicial, num_final):
    vector = []
    for i in range(tamano):
        vector.append(random.randint(num_inicial, num_final))
    
    return vector

def busquedaVector(V, elemento):
    for i in range(len(V)):
        if V[i] == elemento:
            return True
    
    return False

def ordenarVectorAscendente(V):
    return sorted(V) #sorted(V, reverse=True) ordena descendentemente

def imprimeMenu():
    print("******************************************************************")
    print("******************************************************************")
    print("************         1. Busqueda                     *************")
    print("************         2. Ordenamiento                 *************")
    print("************         3. Salida                       *************")
    print("******************************************************************")
    print("******************************************************************")

def actividad4(): 
    N = int(input("Digite la cantidad de elemntos del vector: "))
    lista = llenarVectorAleatorio(N, 1, 1000)
    print("El vector generado es: ", lista)

    opcion_menu = 0
    while opcion_menu != 3:
        imprimeMenu()
        opcion_menu = int(input("Digite la opción que desea ejecutar: "))
        if opcion_menu == 1:
            #Ejecutamos la busqueda
            elemento_a_buscar = int(input("Digite el elemento a buscar: "))
            if busquedaVector(lista, elemento_a_buscar):
                print("ELEMENTO ENCONTRADO!!!!")
            else:
                print("ELEMENTO NO ENCONTRADO")

        elif opcion_menu == 2:
            
            #Ejecutamos el ordenamiento
            print("Ordenando el vector...")
            lista_ordenada = ordenarVectorAscendente(lista)
            print("La lista ordenada es: ", lista_ordenada)

        elif opcion_menu != 3:
            print("La opción ingresada no es válida.")
        
        input("Presione una tecla para continuar...")
        limpiarPantalla()


# Actividad 5: Cree un programa que genere una lista aleatoria de n elementos y luego calcule 
# una nueva lista con la factorial de cada uno de los elementos de la lista original.
import random
def lista(m):
    lista = []
    for i in range(m):
        lista.append(random.randint(0,10))
    return lista

def factorial():
    list1 = lista(10)
    factorial = 1
    aleatoria = []
    for i  in range(len(list1)):
        factorial = 1
        for j in range(1,list1[i]+1):
            
            factorial = factorial * j
        aleatoria.append(factorial)
    print(aleatoria)



#factorial()


# Actividad 6: dada una matriz de 6 x 5 con los siguientes valores:
# hola	    papa	casa	carro	agua
# saludo	tomate	tomar	lugar	pizza
# billar	futbol	perro	gato	miel
# pollo	    vaca	cama	pieza	motor
# zapato	carro	foca	brazo	ala
# xilofono	yate	tronco	risa	uno

# Cree un programa que brinde tres opciones de búsqueda: 
# 1.	Palabras que empiecen por la letra…
# 2.	Palabras que contengan…
# 3.	Palabras que finalicen con la letra …
# El usuario, después de elegir que opción desea, deberá ingresar la letra y seguidamente el programa debe imprimir una lista con las palabras de la matriz que cumplan con la condición dada.
import re
matriz = ([['hola','papa','casa','carro','agua'],
['saludo','tomate','tomar','lugar','pizza'],
['billar','futbol','perro','gato','miel'],
['pollo','vaca','cama','pieza','motor'],
['zapato','carro','foca','brazo','ala'],
['xilofono','yate','tronco','risa','uno']])

def buscarprimera():
    x = input()
    for i in range(4):
        for j in range(5):
            resultado = re.search(f'^{x}',matriz[i][j])
            if resultado != None:
                print(matriz[i][j])

def buscarultima():
    x = input()
    for i in range(4):
        for j in range(5):
            resultado = re.search(f'{x}$',matriz[i][j])
            if resultado != None:
                print(matriz[i][j])


def buscarinter():
    x = input()
    for i in range(4):
        for j in range(5):
            resultado = re.search(f'{x}',matriz[i][j])
            if resultado != None:
                print(matriz[i][j])
def actividad6():
    entrada = int(input('Opciones 1: Buscar la primera letra, 2: Buscar la ultima letra, 3: palabras q contengan la letra '))
    if entrada == 1:
        buscarprimera()
    elif entrada == 2:
        buscarultima()
    elif entrada == 3:
        buscarinter()
    else:
        print('dato ingresado incorrecto')
    
actividad6()





# Actividad 7
# Utilizando la misma matriz de la actividad 6, cree un programa para el juego del ahorcado. 
# El programa debe seleccionar al azar una palabra y luego debe mostrar la cantidad de 
# letras de la palabra seleccionada. El usuario deberá ingresar las letras que el cree 
# pertenecen a la palabra y podrá fallar solo 6 veces. El usuario gana cuando se adivinan 
# todas las letras de la palabra. Pierde cuando falla más de 6 veces sin adivinar 
# la palabra completa.
