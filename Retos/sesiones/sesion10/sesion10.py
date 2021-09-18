"""
Funciones

La verdad es que hemos venido trabajando con funciones desde que empezamos con archivos .py 
En Python, definimos una función con la siguiente estructura

def funcion(parametros)

Recuerda que los parametros son opcionales!
"""

def suma(a,b):
    
    print(a+b)

#suma(3,4)



#Actividad 1

def caja():
    total = 0
    continuar = 'S'
    while continuar == 'S':    
        nombre = input('Ingrese el nombre del producto ')
        precio = float(input('Ingrese el precio del producto '))
        total =  precio + total
        imprimaproducto(nombre,precio)
        continuar = input('tiene mas articulos para ingresar, marque S para si y N para no ')
    print('El total de la compra es ', total)
    
    

def imprimaproducto(nombre,precio):
    print('El nombre del producto es {} y el precio es {}'.format (nombre,precio))



#Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos de su cliente, su precio y calcular el total a pagar.
#
#Diseña un programa con las siguiente características:
#
#    1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
#    2. Una variable total que vaya sumando el precio de los artículos
#    3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
#        el precio de cada producto y los imprima.
#    4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    5. Si no hay más artículos, que imprima el total de la compra

#    Al final de tus funciones, puedes simplement llamar a la función caja para probar

#caja()

#Actividad 2
#
import random
def numALEATORIO():
    num = random.randint(100,130)
    while num == 110 or num == 115 or num == 120:
        num = random.randint(100,130)
    return num
     
    
    

    


def numeros():
    
    num = 0
    contador =1
    while contador < 10:
        num = numALEATORIO()
        if contador % 2 != 0:
            if num % 2 == 0:
                print('El numero {} es par'.format(num))
                contador += 1
        if contador % 2 == 0:
            if num % 2 != 0:
                print('El numero {} es impar '.format(num))
                contador += 1

        


    

     #   print(num)
#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120 .
#
#Adicionalmente, una función numeros que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.
#numALEATORIO()
numeros()
