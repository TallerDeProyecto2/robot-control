# Aqui se listan los imports
from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
import random
import serial

app = Flask(__name__)

# Define la ruta con la que se ingresara desde el browser
@app.route('/', methods = ['GET', 'POST'])
def index():

    # Comunicacion mediante puerto serie
    # Comando para listar los puertos disponibles: python -m serial.tools.list_ports
    # ser = serial.Serial('COM1')  # open serial port
    # print(ser.name)         # check which port was really used
    # ser.write(b'hello')     # write a string
    # ser.close()             # close port

    if request.method == 'POST':
        data = request.form
        frecuencia = data["frec"]
        # Datos de la conexion a la BD
        cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='estacion')
        cursor = cnx.cursor()
        query = ("UPDATE frecuencia_muestreo SET valor = %s WHERE id=1")
        cursor.execute(query, (frecuencia,))
        # Commit cambios en la BD
        cnx.commit()
        # Cierro la conexion
        cnx.close()

    return render_template('form.html')

@app.route('/movimientos', methods = ['GET', 'POST'])
def mov():

    # Comunicacion mediante puerto serie
    # Comando para listar los puertos disponibles: python -m serial.tools.list_ports
    # ser = serial.Serial('COM1')  # open serial port
    # print(ser.name)         # check which port was really used
    # ser.write(b'hello')     # write a string
    # ser.close()             # close port

    if request.method == 'POST':
        data = request.form
        frecuencia = data["frec"]
        # Datos de la conexion a la BD
        cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='estacion')
        cursor = cnx.cursor()
        query = ("UPDATE frecuencia_muestreo SET valor = %s WHERE id=1")
        cursor.execute(query, (frecuencia,))
        # Commit cambios en la BD
        cnx.commit()
        # Cierro la conexion
        cnx.close()

    return render_template('movimiento.html')


if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=3606)
