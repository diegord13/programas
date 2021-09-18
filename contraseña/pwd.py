from tkinter import *
from sqlite3 import *
from tkinter import ttk 
import numpy as np

ventana = Tk()
ventana.title("pwd")
ventana.geometry("400x400")
ventana.resizable(False,False)
ventana.configure(background="black")

#funciones

def borrar():
#   global operacion
#   global resultado
#  operacion = ""
    pantalla.delete(0,END)


    
def consultar():
    conexion = connect("pwd.db")
    cursor = conexion.cursor()
    informacion = combo.get()
    
    cursor.execute('SELECT contraseña FROM TABLA WHERE aplicativo=?', (informacion,))
    data=cursor.fetchall()
    for x in data:
            pantalla.delete(0,END)
            pantalla.insert(0,str(x))

       

            
def ingresar():
    aplicativo_data = aplicativo.get()
    username_data = username.get()
    password_data = password.get()
    conexion = connect("pwd.db")
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO TABLA VALUES (?, ?, ?)',(aplicativo_data, username_data, password_data,))
    pantalla.delete(0,END)
    pantalla.insert(0,'INGRESADO')
    pantalla_app.delete(0,END)
    pantalla_user.delete(0,END)
    pantalla_pd.delete(0,END)
    conexion.commit()


#display resultados
pantalla = Entry(ventana,font=("arial",20,"bold"),borderwidth=2)
pantalla.grid(row=0,column=0,columnspan=3,pady=10,padx=5)

#display usuario y contraseña
aplicativo = StringVar()
username = StringVar()
password = StringVar()


username_label = Label(text="Aplicativo")
username_label.place(x=20,y=105)

pantalla_app = Entry(textvariable = aplicativo,font=("arial",20,"bold"),borderwidth=2)
pantalla_app.grid(row=4,column=0,columnspan=3,pady=10,padx=5)

username_label = Label(text="Username")
username_label.place(x=20,y=165)

pantalla_user = Entry(textvariable = username,font=("arial",20,"bold"),borderwidth=2)
pantalla_user.grid(row=5,column=0,columnspan=3,pady=10,padx=5)

username_label = Label(text="Password")
username_label.place(x=20,y=225)

pantalla_pd = Entry(textvariable = password, font=("arial",20,"bold"),borderwidth=2,show="*")
pantalla_pd.grid(row=6,column=0,columnspan=3,pady=10,padx=5)


#Boton de reiniciar operacion
boton_reset = Button(ventana,text="BORRAR",width=8,height=2,command=lambda:borrar())
boton_reset.grid(row=0,column=3,pady=10,padx=5)

#Botones de la primera fila
ancho = 20
alto = 3

boton1 = Button(ventana,text="ingresar",width=ancho,height=alto,command=ingresar)
boton1.grid(row=7,column=0,pady=10,padx=5)

#boton2 = Button(ventana,text="valores",width=ancho,height=alto,command=valores)
#boton2.grid(row=7,column=1,pady=10,padx=5)

#def valores():
conexion = connect("pwd.db")
cursor = conexion.cursor()
cursor.execute('SELECT aplicativo FROM TABLA')
data = cursor.fetchall()
i = 0
lista=[]
for valores in data:
    lista.append(valores)
    i=i+1
    


#Generacion del combobox

texto = StringVar()
combo = ttk.Combobox(ventana,values=lista)
combo.grid(column=0, row=2)
combo.current(0)
boton_combo = Button(ventana,text='Consultar',width=ancho,height=alto,command=consultar)
boton_combo.grid(row=2,column=1)
etiqueta = Label(ventana,textvariable = texto)





ventana.mainloop()