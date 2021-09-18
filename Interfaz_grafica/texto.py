import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos el componente texto

entrada = tkinter.Text(raiz)
entrada.config(width=20,height=10, font=("Verdana",15), padx=5,pady=5, fg="green",selectbackground="lightgrey")
entrada.pack()





raiz.mainloop()