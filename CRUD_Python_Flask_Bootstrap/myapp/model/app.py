from flask import Flask, render_template, request, url_for, redirect
import os
import sys
from datetime import datetime
sys.path.append('controller/')
from database import Database

class MyApp(Flask):
    def __init__(self, import_name, template_dir, database):
        super().__init__(import_name, template_folder=template_dir)
        self.database = database

    def get_users(self):
        cursor = self.database.connection.cursor()
        cursor.execute("SELECT * FROM GUIAS")
        myresult = cursor.fetchall()
        cursor.close()
        column_names = [column[0] for column in cursor.description]
        insert_object = [dict(zip(column_names, record)) for record in myresult]
        return insert_object


    def add_user(self, cedula_guia, nombre, apellido, disponibilidad, grupo):
        if cedula_guia and nombre and apellido and disponibilidad and grupo:
            cursor = self.database.connection.cursor()
            sql = "INSERT INTO GUIAS (cedula_guia, nombre, apellido, disponibilidad, grupo, fecha) VALUES (%s,%s,%s,%s,%s,%s)"
            fecha = datetime.now()
            data = (cedula_guia, nombre, apellido, disponibilidad, grupo, fecha)
            cursor.execute(sql, data)
            self.database.connection.commit()

    def delete_user(self, id):
        cursor = self.database.connection.cursor()
        sql = "DELETE FROM GUIAS where id=%s"
        data = (id,)
        cursor.execute(sql, data)
        self.database.connection.commit()

    def edit_user(self, cedula_guia, nombre, apellido, disponibilidad, grupo, id):
        if cedula_guia and nombre and apellido and disponibilidad and grupo:
            cursor = self.database.connection.cursor()
            sql = "UPDATE GUIAS SET cedula_guia = %s, nombre =%s, apellido=%s , disponibilidad=%s, grupo=%s WHERE id = %s"
            data = (cedula_guia, nombre, apellido, disponibilidad, grupo, id)
            cursor.execute(sql, data)
            self.database.connection.commit()

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'view', 'templates')

# Crear una instancia de la clase Database
database = Database(host='localhost', user='root', password='joseph', database='villa_daniela')
database.connect()

# Crear una instancia de la clase MyApp, pasando la instancia de Database
app = MyApp(__name__, template_dir, database)

# Rutas 
@app.route('/')
def home():
    data = app.get_users()
    return render_template('guias_GUI.html', data=data)

# Ruta guardar
@app.route('/user', methods=['POST'])
def add_user():
    cedula_guia = request.form['cedula_guia']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    disponibilidad = request.form['disponibilidad']
    grupo = request.form['grupo']
    app.add_user(cedula_guia, nombre, apellido, disponibilidad, grupo)
    return redirect(url_for('home'))

# Eliminar
@app.route('/delete/<string:id>')
def delete(id):
    app.delete_user(id)
    return redirect(url_for('home'))

# Editar
@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    cedula_guia = request.form['cedula_guia']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    disponibilidad = request.form['disponibilidad']
    grupo = request.form['grupo']
    app.edit_user(cedula_guia, nombre, apellido, disponibilidad, grupo, id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)
