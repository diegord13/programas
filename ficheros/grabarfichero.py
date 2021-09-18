#Grabar un fichero de texto

fichero = open("fichero_para_grabar.txt","wt")

texto_de_fichero = "Hola, esta es la linea que vamos a grabar en el fichero de texto"
fichero.write(texto_de_fichero)

fichero.close()