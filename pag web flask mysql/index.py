from types import MethodDescriptorType
from flask import Flask, render_template, request, redirect, url_for, flash
from flask.globals import request
from flask_mysqldb import MySQL

app = Flask(__name__)

#Mysql conexion datos de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacto'
mysql = MySQL(app)

#Para mantener la sesion
app.secret_key = 'mysecretkey' 

@app.route('/')
def home():

    #Mostrar el listado de los datos, sacando la informacion en la variable data y enviandolas al html

    cur  = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    #para enviar a la plantilla html
    return render_template('index.html', contactos = data)

#Agregar datos enviados desde el formulario de html y guardarlos en la base de datos, es necesario la funcion request
@app.route('/add', methods=['POST'])
def add_contact():
    if request.method=='POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (nombre, telefono, email) VALUES (%s, %s, %s)',(nombre,telefono,email))
        mysql.connection.commit()
        flash('contacto agregado satisfactoriamente')
        return redirect(url_for('home'))
    return 'add contact'

#Se realiza una conexion para verificar el id del parametro que queremos actulizar, enviandolo al
#formulario ubicado en edit_contact.html, el cual despues enviara los parametros ingresados en el formulario
#a la ruta update del archivo index.py
@app.route('/edit/<id>')
def get_contact(id):
    cur  = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit_contact.html', contact=data[0])

#Actualizando contactos provenientes del formulario de edit_contact
@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        cur  = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts 
            SET nombre = %s, 
                telefono = %s, 
                email = %s 
            WHERE id = %s
        """, (nombre, telefono, email,id))
        mysql.connection.commit()
        flash ('contacto actualizado')
        return redirect(url_for('home'))


#Eliminar un registro con el ingreso de un parametro id proveniente desde index.html
@app.route('/delete/<string:id>')
def delete_contact(id):
    cur  = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Usuario eliminado')
    return redirect(url_for('home'))

    
if __name__=='__main__':
    app.run(port = 3000,debug = True)