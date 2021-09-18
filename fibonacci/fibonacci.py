n = int(input('numeros a mostrar '))
contador = 1

a = 0
b = 1

while contador <= n:

    resultado = a + b
    a = b
    b = resultado 
    contador = contador +1
    
    print (resultado)

