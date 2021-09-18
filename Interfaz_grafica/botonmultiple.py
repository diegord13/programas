import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos los radiobutton
def seleccionar():
	print("La opcion seleccionada es {}".format(opcion.get()))

opcion = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(raiz,text="Opcion 1", variable=opcion, value=1,command=seleccionar)
radiobutton1.pack()

radiobutton2 = tkinter.Radiobutton(raiz,text="Opcion 2", variable=opcion, value=2,command=seleccionar)
radiobutton2.pack()

radiobutton3 = tkinter.Radiobutton(raiz,text="Opcion 3", variable=opcion, value=3,command=seleccionar)
radiobutton3.pack()

raiz.mainloop()