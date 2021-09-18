import pickle

lista_colores = ["azul", "verde", "rojo", "amarillo"]

fichero = open("fichero_colores.pckl","wb")

pickle.dump(lista_colores,fichero)

fichero.close()