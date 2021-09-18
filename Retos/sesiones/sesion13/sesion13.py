"""
Matrices o vectores bidimensionales

En Python podemos trabajar los arreglos bidimensionales como listas de listas, es decir, cada elemento de la lista es una lista.

Nota Existe una librería en Python que maneja tanto vectores como matrices llamada numpy. 
Esta librería está por fuera del alcance de este curso pero puedes investigarla.

Veamos un ejemplo:
"""
def ejemplo1():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    print(a)

#ejemplo1()

#O podemos recorrer todos los elementos e imprimir como una matriz
def ejemplo2():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

#ejemplo2()

#Actividad 1
#
#Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y 100
#aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.
import random


def actividad1():
    matriz = []
    for i in range(5):
        fila = []
        for j in range(10):
            fila.append(random.randint(1,100))
        matriz.append(fila)

    print(imprimirMatriz(matriz))

def imprimirMatriz(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end='\t')
        print()



#actividad1()
def mayor(A):
    numero_mayor = A[0][0]
    fila_mayor = 0
    columna_mayor = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > numero_mayor:
                numero_mayor = A[i][j]
                fila_mayor = i
                columna_mayor = j
           #    0       ,    1       ,    2
    return [numero_mayor, fila_mayor, columna_mayor]

def menor(A):
    numero_menor = A[0][0]
    fila_menor = 0
    columna_menor = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < numero_menor:
                numero_menor = A[i][j]
                fila_menor = i
                columna_menor = j
           #    0       ,    1       ,    2
    return [numero_menor, fila_menor, columna_menor]

#
#El producto escalar de un número real, x , y una matriz A es la matriz xA. 
#Cada elemento de la matriz xA es x veces su elemento correspondiente en A.
#
#Diseñemos una funcion escalar(matriz, escalar) que dada matriz[n][m] y un escalar, 
#imprima el producto escalar de la matriz.

def actividad2():
    matriz = []
    for i in range(5):
        fila = []
        for j in range(10):
            fila.append(random.randint(1,100))
        matriz.append(fila)

    print(imprimirMatriz(matriz))
    return matriz

def escalar():
    a = 2
    matriz = actividad2()
    for i in range(5):
         
         for j in range (10):
            matriz[i][j] = a* matriz[i][j]
        
    print(imprimirMatriz(matriz))
        

        
escalar()



# def llenarMatrizAleatoria(N,M, num_inicial, num_final):
#     A = []
#     for i in range(N):
#         lf = []
#         for j in range(M):
#             lf.append(random.randint(num_inicial, num_final))
        
#         A.append(lf)
    
#     return A


def producto_escalar(A,x):
    matriz_producto = []
    for i in range(len(A)):
        fila_producto = []
        for j in range(len(A[i])):
            fila_producto.append(A[i][j] * x)
        
        matriz_producto.append(fila_producto)
    
    return matriz_producto


def actividad2():
    dimension = str(input("Digite la cantidad de filas y columnas (NxM): "))
    l_dimension = dimension.split("x")
    matriz_aleatoria = llenarMatrizAleatoria(int(l_dimension[0]), int(l_dimension[1]),1,1000)
    print("***********************************************")
    print("************    MATRIZ GENERADA    ************")
    print("***********************************************")
    imprimirMatriz(matriz_aleatoria)
    print("***********************************************\n")
    valor_escalar = float(input("Digite el valor escalar a multiplicar: "))


#actividad2()