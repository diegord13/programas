# Diseñar 3 opciones:
#
#   1. Leer un número de 4 dígitos, mostrar el dígito mayor e 
#      informar si es par o impar.
#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
#      con el mayor del primero y el menor del segundo.
#   3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.
#   
# Luego crea un menú con las tres opciones.

def funcion1():
    
    numero1 = input('Ingresa un numero de 4 digitos ')
    
    longitud = len(numero1)
    a = int(numero1[0])
    b = int(numero1[1])
    c = int(numero1[2])
    d = int(numero1[3])
    if longitud == 4:
        if  a >= b and a >= c and a >= d:
            digito_mayor = a
            
        elif b >= a and b >= c and b >= d:
            digito_mayor = b
           
        elif c >= a and c >= b and c >= d:
            digito_mayor = c
            
        else:
            digito_mayor = d
            
    if digito_mayor % 2 == 0:
        print('El digito es par')  
    else:
        print('El digito no es par')

    print("El mayor dígito es {}". format(digito_mayor) ) 

def funcion2():
    
    a = input('Ingrese un numero de 3 digitos ')
    b = input('Ingrese otro numero de 3 digitos ')
    nuevo_num=10
    
    longitud_a = len(a)
    longitud_b = len(b)
    dig_a = int(a[0])
    dig_b = int(a[1])
    dig_c = int(a[2])


    dig_1 = int(b[0])
    dig_2 = int(b[1])
    dig_3 = int(b[2])

    if longitud_a == 3 and longitud_b == 3:
        if  dig_a >= dig_b and dig_a >= dig_c:
            digito_mayor = dig_a
            
        elif dig_b >= dig_a and dig_b >= dig_c:
            digito_mayor = dig_b
        
        else:
            digito_mayor = dig_c

    
        if  dig_1 <= dig_2 and dig_1 <= dig_3:
            digito_menor = dig_1
            
        elif dig_2 <= dig_1 and dig_2 <= dig_3:
            digito_menor = dig_2
        
        else:
            digito_menor = dig_3
    nuevo_num = digito_mayor * 10
    nuevo_num = nuevo_num + digito_menor
    print(nuevo_num)


def funcion3():
    #Escribe el código de la tercera opción aquí
       #3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.
    numero1 = input('Ingrese un numero de 3 digitos ')
    longitud = len(numero1)
    #nuevo_num = 100
    a = int(numero1[0])
    b = int(numero1[1])
    c = int(numero1[2])
   
    if longitud == 3:
        if  a >= b and a >= c:
            digito_mayor = a

            if  b <= a and b <= c:
                digito_menor = b
                digito_medio = c

            elif c <= a and c <= b:
                digito_menor = c
                digito_medio = b
            
        elif b >= a and b >= c:
            digito_mayor = b

            if  a <= b and a <= c:
                digito_menor = a
                digito_medio = c

            elif c <= a and c <= b:
                digito_menor = c
                digito_medio = a
           
        else:
            digito_mayor = c
            if  a <= b and a <= c:
                digito_menor = a
                digito_medio = b
            
            elif b <= a and b <= c:
                digito_menor = b 
                digito_medio = a

    


    
    nuevo_num = digito_mayor * 100
    digito_medio = digito_medio * 10
    nuevo_num = nuevo_num + digito_menor + digito_medio
    print("El nuevo numero es {}". format(nuevo_num) ) 

if __name__ == "__main__":
    
    ingresar = int(input('Ingrese que funcion quiere utilizar,1 , 2 o 3 '))
    
    if ingresar == 1:
        funcion1()
    elif ingresar == 2:
        funcion2()
    else:
        funcion3()