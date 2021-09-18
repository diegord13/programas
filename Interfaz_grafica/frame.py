import tkinter

raiz = tkinter.Tk()
raiz.title(	"Mi programa")

#Crear el componente frame

frame = tkinter.Frame(raiz)
frame.config(bg="blue",width=400,height=300)
frame.pack()

raiz.mainloop()