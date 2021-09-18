"""

Para

El ciclo Para o For en Python nos ayuda a ejecutar dentro dentro de un rango determinado de iteraciones. 


En la semana uno exploramos el tipo de dato string (una cadena de caracteres). 
Los caracteres dentro de este tipo de dato en Python puede ser recorridos con la posicion en la que se encuentran dentro de la cadena. Veamos un ejemplo:
"""

def ejemplo1():
    palabra = "Prueba"
    longitud = len(palabra)

    print("Primer ciclo")
    for i in range(longitud):
        print(palabra[i])

    print("Segundo ciclo")
    for x in "Prueba":
        print(x)

#ejemplo1()



def actividad1():
    print("actividad1")
    # Vamos a realizar un algoritmo que nos calcule la serie de Fibonacci.
    # La serie o secuencia de Fibonacci comienza con los números 0 y 1 y 1, y a partir de allí es posible calcular el siguiente valor como la suma de los dos valores anteriores. 
    # Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc. Así, los primeros números de la secuencia son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    # Creemos un programa que a partir de un número N ingresado, imprima los primeros N números de la serie de Fibonacci.
    n = int(input('numeros a mostrar '))
    a = 0
    b = 1
    print(a)
    if n >=1:
        for numero in range(n):
            resultado = a + b
            b = a
            a = resultado
            print (resultado)
    else:
        print('numero invalido')
#actividad1()

def actividad2():
    print("actividad2")
    #Escribe el código usando break que reciba una palabra e imprima el número de letras que tiene y las letras hasta que, o bien termine la palabra o encuentre la letra a. .
    letra = input('Ingrese una palabra ')
    longitud = len(letra)
    contador = 1
    for let in range(longitud):
        if letra[let] == 'a':
            let = let -1
            break

        print(letra[let])
        contador += 1
    print(let + 1)
#actividad2()

def actividad3():
    #print("actividad3")
    contador_pos = 0
    contador_neg = 0
    contador_neu = 0
    for numero in range(10):
        n= int(input('ingrese el numero '))
        if n > 0:
            contador_pos += 1
            
        elif n < 0:
            contador_neg += 1
            
        else:
            contador_neu += 1
    print('la cantidad de numeros positivos es {}, de negativos {} y neutros {}'.format(contador_pos,contador_neg,contador_neu))
    #Escribe un algoritmo que lea 10 números e imprima cuantos son positivos, cuantos negativos y cuantos neutros(0).

#actividad3()

def actividad4():
    #print("actividad4")
    n = 1
    resultado = 1
    while n != -1:
        if n >= 0:
            for numero in range(n):
                resultado = resultado * (numero + 1)
            print('el factorial de {} es {}'.format(n,resultado))
            resultado  = 1
            n = int(input())
        else:
            print('El numero ingresado no se puede calcular')
            n = int(input())
        

        

    #Usando tanto while como for, escribe el codigo que pida números al usuario hasta que este ingrese -1 y que retorne el factorial de cada número ingresado usando un ciclo Para (For).
    
actividad4()