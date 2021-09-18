"""
Funciones con listas

Aquí van algunas funciones útiles cuando trabajamos con listas.

    remove(x) - remueve el primer valor X de la lista
    pop([i]) - remueve el valor en la posición i. pop() remueve el último valor de la lista
    len(x) - permite calcular el tamaño de una lista
"""
def ejemplo1():
    nombres = ["María", "Juan","Andrés"]
    nombres.append("Jorge")
    print(nombres)
    print(len(nombres))

    nombres.remove("Juan")
    print(nombres)
    print(len(nombres))

    nombres.pop(1)
    print(nombres)
    print(len(nombres))
#ejemplo1()

"""
Como vemos, append(x) inserta el valor x al final de la lista.

Pero también existe la función insert(pos, x) que nos permite insertar x en la posición pos. 

Veamos un ejemplo
"""
def ejemplo2():
    a = [1, 3, 2, 5, 2]
    a.insert(4,8)
    print(a)
    a.sort()
    print(a)

ejemplo2()

#Actividad 1

#Escribamos un programa que nos permita crear con una lista de 6 números aleatorios entre 1 y 20, 
#y luego creemos tres funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos
#    orden(x) - Una función que ordene los datos de una lista x ascendentemente y la imprima en orden

import random

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

def orden(lista):
    return sorted(lista)

def actividad1():
    lista_numeros = []
    for i in range(6):
        lista_numeros.append(random.randint(1,20))
    
    print(f"La lista generada es: {lista_numeros}")
    print(f"El número mayor de {lista_numeros} es {mayor(lista_numeros)}")
    print(f"Los elementos primos en la lista {lista_numeros} " + 
          f"son: {primos(lista_numeros)}")
    print(f"Los elementos primos ordenados son {orden(lista_numeros)}")


    
          
actividad1()

#actividad1()
