import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos el componente boton

def accion():
	print("Hola mundo")

boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="green")
boton.pack()



raiz.mainloop()