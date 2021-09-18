"""
Vectores/Listas

Como vimos en la parte teórica, los vectores son una estructura de dato organizada que nos permite 
almacenar información. Una de las implementaciones más utilizadas es Python son las listas (List). 

Nota: En Python hay algunas diferencias menores entre un arreglo (array) y una lista, 
pero por ahora vamos a asumir que son lo mismo.

Vamos a ver una definición de esta estructura en Python. Para crear una lista, utilizamos los corchetes 
y separamos los valores de nuestra estructura con una coma. 

Por ejemplo, en la siguiente instrucción estamos creando una lista llamada a con los valores 1, 3, 2, 5, 2.
"""

def ejemplo1():
    a = [1, 3, 2, 5, 2]
    print(a)

#ejemplo1()

#Las listas no necesariamente tienen que ser de números, también pueden ser de texto:
def ejemplo2():
    nombres = ["María", "Juan","Andrés"]
    print(nombres)

#ejemplo2()

#Aquí van algunas funciones útiles cuando trabajamos con listas.
#    append(x) - inserta un nuevo valor x al final de la lista
#    remove(x) - remueve el primer valor X de la lista
#    pop([i]) - remueve el valor en la posición i. pop() remueve el último valor de la lista
#    len(x) - permite calcular el tamaño de una lista
#
# Ahora, veamoslas en acción
def ejemplo3():
    nombres = ["María", "Juan","Andrés"]
    nombres.append("Jorge")
    print(nombres)
    print(len(nombres))

    nombres.remove("Juan")
    print(nombres)
    print(len(nombres))

    nombres.pop(2)
    print(nombres)
    print(len(nombres))
#ejemplo3()

#Actividad 1

# Usando el conocimiento de ciclos, crea una funcion numeros que tenga una lista con los numeros pares del 1 al 10 
# y usa un ciclo para que los imprima

def numeros():
    lista = [2,4,6,8,10]
    for i in range(len(lista)):
        print(lista[i])

#numeros()
#actividad1()

#Actividad 2
#
#Escribamos un programa que nos permita crear una lista de 6 números aleatorios entre 1 y 20 en Python, y 
#creemos dos funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos
import random
import numpy as np
def aleatorios():
    lista =list(np.arange(6))
    for i in range(6):
        lista[i] = random.randint(1,20)
    print(f'el numero mayor de {lista} es {mayor2(lista)}')
    print(f'los numeros primos de {lista} son {primos2(lista)}')
    
   
        
def mayor2(lista):
    numero_mayor = 0
    for i in range(len(lista)):
        if lista[i] > numero_mayor:
            numero_mayor = lista[i]
    return numero_mayor

def primos2(lista):
    num_primo = []
    for i in range(6):
        contador = 0
        for n in range(2,(lista[i])):
            if lista[i] % n == 0:
                
                contador += 1
                continue
                
        if contador == 0  and lista[i] != 1:
            num_primo.append(lista[i])
            #continue
    return num_primo
    
    
   


#aleatorios()


def mayor(lista):
    numero_mayor = lista[0]
    for i in range(1,len(lista)):
        if lista[i] >= numero_mayor:
            numero_mayor = lista[i]
    
    return numero_mayor

def primos(lista):
    lista_primos = []
    for i in range(len(lista)):
        es_primo = True
 
        for k in range(2, lista[i]):
            if lista[i] % k == 0:
                es_primo = False
                break
        
        if (es_primo): 
            lista_primos.append(lista[i])
    
    return lista_primos

def actividad2():
    lista_numeros = []
    for i in range(6):
        lista_numeros.append(random.randint(1,20))
    
    print(f"La lista generada es: {lista_numeros}")
    print(f"El número mayor de {lista_numeros} es {mayor(lista_numeros)}")
    print(f"Los elementos primos en la lista {lista_numeros} " + 
          f"son: {primos(lista_numeros)}")
          
actividad2()