"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

Por ejemplo:
"""

# def ejemplo1():
#     i = 1
#     while i < 6:
#         print(i)
#         i += 1
# ejemplo1()

def actividad1():
    numero = int(input('Ingrese un numero '))
    pares = 0
    contador = 1
    while contador <= numero:
        if contador % 2 == 0:
            print ('numero par {}'.format(contador))
        contador = contador + 1
    
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número. 

# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
#actividad1()

def actividad2():
    numero = int(input('Ingrese un numero '))
    contador = 0
    while numero > 0:
        #print (numero % 10)
        contador = contador + 1
        numero = numero // 10
    print (contador)

    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.

#actividad2()    
    

def actividad3():
    numero = 0
    contador = 0
    resultados = 0
    total = 0
    while numero != -1:
        numero = float(input('ingrese un numero '))
        if numero == -1:
            break
        else:   
            contador = contador + 1
            resultados = numero + resultados
            total = resultados / contador
    print (total)
       
        
# if __name__ == "__main__":
    
#     ingresar = int(input('Ingrese que funcion quiere utilizar,1 , 2 o 3 '))
    
#     if ingresar == 1:
#         actividad1()
#     elif ingresar == 2:
#         actividad2()
#     else:
#         actividad3()
    #Escribe el código que solicite números al usuario hasta que éste ingrese -1.
    #Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).

#actividad3()