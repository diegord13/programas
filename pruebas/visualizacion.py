import numpy as np

def tablero():

    tablero = [[str(i) for i in range(j,(j)*2)] for j in range(5)]


    for num in tablero:
        print(num)

#tablero()


def tablero2():

    tablero = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]


    for num in tablero:
        print(num)

#tablero2()

def tablero3():

    numero = 10
    for i in range(numero):
        
        print(' ' * (numero - i ) + "*" *(2*i+1))

#tablero3()

def tablero4():

    numero = 10
    for i in range(numero):
        
        print(' ' * (i ) + "_" *(2*(numero - i)))

#tablero4()

def tablero5():
    numero = 10
    serie = 100
    dato = 1
    serie_fin = 0
    for i in range(2,numero,2):
        
        serie = serie / (dato)
        dato = dato + dato
        serie_fin = serie + serie_fin
        print(serie_fin)
def tablero6():
    numero = 5
    serie = 100
    dato = 0
    for n in range(1,numero):
        serie = (100 / n) 
        dato = dato + serie 
        
        print(dato)
tablero5()