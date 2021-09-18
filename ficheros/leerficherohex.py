import pickle

fichero = open("fichero_colores.pckl","rb")
lista_leido_fichero = pickle.load(fichero)

print(lista_leido_fichero)
