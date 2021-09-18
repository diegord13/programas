import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos el componente entry (entrada de datos)

entrada = tkinter.Entry(raiz)
entrada.config(justify="center", show="*")
entrada.pack()


raiz.mainloop()