import moduloficheros2

nombre_fichero = "ficherodetexto.texto"
fichero = modulofichero2.Fichero(nombre_fichero)

texto = "Esto es lo que va a llevar el fichero"
fichero.grabar_fichero(texto)
