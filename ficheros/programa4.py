import prueba_dic

nombre_archivo = "diccionario.txt"
fichero = prueba_dic.diccionario(nombre_archivo)

texto = input()
strtexto = str(texto)
fichero.grabar_fichero(strtexto)

