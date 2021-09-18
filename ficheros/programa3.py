import moduloficheros2

nombre_fichero = "ficherodetexto.txt"
fichero = moduloficheros2.Fichero(nombre_fichero)

texto = "Esto es lo que va a llevar el fichero"
fichero.grabar_fichero(texto)

texto = input()

fichero.incluir_fichero(texto)

texto_leido = fichero.Leer_fichero()
print(texto_leido)