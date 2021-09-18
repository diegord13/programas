"""
Cada ejemplo y actividad será definida como un bloque independiente.
Si-Sino-Finsi
Recuerda que los condicionales múltiples y anidados nos permiten evaluar múltiples casos. 
El condicional Si-Sino-Si-Finsi tiene la siguiente estructura:

    Si (condición) Entonces
        instrucción(es)
    Sino Si
        instrucción(es)
    Fin Si

En Python, esto se escribe un poco diferente y la estructura general depende de las tabulaciónes. 
Por ejemplo:
"""
def ejemplo1():
    x = int(input("Por favor ingresa un número: "))
    if x < 0:
        print('El número es Negativo')
    elif x > 0:
        print('El número es positivo')
    elif x == 0:
        print('El número es cero')
#ejemplo1()

def actividad1():
    print("actividad1")
    color = input('Ingrese el color del semaforo (Verde, Amarillo y Rojo) ')
    if color != 'Verde' and color != 'Amarillo' and color != 'Rojo':
        print('El color es invalido por favor ingrese (Verde, Amarillo o Rojo')
    else:
        if color == 'verde':
            print('Siga')
        elif color == 'Amarillo':
            print('Precaucion')
        else:
            print('Pare')

    #Escribe el código que imprima un comando dada la luz del semáforo
        #Verde = Siga
        #Amarillo = Precaución
        #Rojo = Pare

# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
#actividad1()

def actividad2():
    print("actividad2")
    #Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peaton o no (hayPeaton), imprima:
        #Verde -------- Si hay peaton - Pare, Sino - Siga
        #Amarillo ----------- Si hay peaton - Pare, Sino - Precaución
        #Rojo = Pare
    color = input('Ingrese el color del semaforo (Verde, Amarillo y Rojo) ')
    hay_peaton = input('Digite sí hay peaton o no 1 para si y 0 para no ')
    if color != 'Verde' and color != 'Amarillo' and color != 'Rojo':
        print('El color es invalido por favor ingrese (Verde, Amarillo o Rojo')
    else:
        if color == 'Verde' and hay_peaton == '0':
            print('siga')
        elif color == 'Amarillo' and hay_peaton == '0':
            print('Precaucion')
        else:
            print('Pare')
actividad2()

def actividad3():
    print("actividad3")
    #Escribe el código para dos numeros a y b, el usuario va a seleccionar una opcion: 
        #1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y 
        #retornar el resultado de la operación indicada.
    a = float(input('Ingrese el numero a '))
    b = float(input('Ingrese el numero b '))
    c = input('Ingrese la operacion, 1 para sumar, 2 para multiplicar, 3 para restar y 4 para dividir ')

    if c == '1':
        resultado = a + b
        print(resultado)
    elif c == '2':
        resultado = a * b
        print(resultado)
    elif c == '3':
        resultado = a - b
        print(resultado)
    elif c == '4':
        resultado = a / b

        print(resultado)
    else:
        print('Ingrese un valor correcto')

#actividad3()