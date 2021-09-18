import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

#creamos una ventana para preguntar o confirmar

def preguntar():
	resultado = tkinter.messagebox.askquestion("Titulo de la pregunta", "Quieres borrar este fichero")
	if (resultado == "yes"):
		print("Si, quiero borrar el fichero")
	else:
		print("No, no quiero borrar el fichero")


boton = tkinter.Button(raiz,text = "Pulsar para preguntar", command=preguntar)
boton.pack()



raiz.mainloop()