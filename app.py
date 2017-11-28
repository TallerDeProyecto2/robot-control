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
    return render_template('inicio.html')

# Define la ruta para los movimientos creados
@app.route('/creados', methods = ['GET', 'POST'])
def creados():
    return render_template('creados.html')

# Define la ruta para los movimientos complejos
@app.route('/movimientosComplejos', methods = ['GET', 'POST'])
def movCom():
    # Guardo el nuevo movimiento complejo, con angulo en 0 para los que no se definen por el usuario
    if request.method == 'POST':
        data = request.form
        nombre = data["nombre"]
        descripcion = data["descripcion"]
        servo = []
        for x in range(1, 17):
            numeroServo = "servo"+str(x)
            angulo = data[numeroServo]
            servo.append(angulo)
        # Datos de la conexion a la BD
        cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='robot_control')
        cursor = cnx.cursor()
        cursor.execute('''INSERT into movimiento_compuesto (nombre, descripcion, servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8, servo9, servo10, servo11, servo12, servo13, servo14, servo15, servo16)
                      values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                      (nombre, descripcion, servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0), servo.pop(0)))
        # Commit cambios en la BD
        cnx.commit()
        # Cierro la conexion
        cnx.close()

    return render_template('form.html')

# Definimos la ruta para los movimientos simples (con el slider)
@app.route('/movimientos', methods = ['GET', 'POST'])
def mov():

    # Comunicacion mediante puerto serie
    # Comando para listar los puertos disponibles: python -m serial.tools.list_ports
    # ser = serial.Serial('COM1')  # open serial port
    # print(ser.name)         # check which port was really used
    # ser.write(b'hello')     # write a string
    # ser.close()             # close port

    return render_template('movimiento.html')

# Definimos la ruta para los movimientos predefinidos
@app.route('/predefinidos', methods = ['GET', 'POST'])
def pred():

    # Comunicacion mediante puerto serie
    # Comando para listar los puertos disponibles: python -m serial.tools.list_ports
    # ser = serial.Serial('COM1')  # open serial port
    # print(ser.name)         # check which port was really used
    # ser.write(b'hello')     # write a string
    # ser.close()             # close port

    return render_template('predefinido.html')

@app.route('/movimiento1')
def mov1():

    print("movimiento1")
    # Comunicacion mediante puerto serie
    # Comando para listar los puertos disponibles: python -m serial.tools.list_ports
    # ser = serial.Serial('COM1')  # open serial port
    # print(ser.name)         # check which port was really used
    # ser.write(b'hello')     # write a string
    # ser.close()             # close port

    return render_template('predefinido.html')

@app.route('/movimiento2')
def mov2():

    print("movimiento2")
    # Comunicacion mediante puerto serie
    # Comando para listar los puertos disponibles: python -m serial.tools.list_ports
    # ser = serial.Serial('COM1')  # open serial port
    # print(ser.name)         # check which port was really used
    # ser.write(b'hello')     # write a string
    # ser.close()             # close port

    return render_template('predefinido.html')

@app.route('/movimiento3')
def mov3():

    print("movimiento3")
    # Comunicacion mediante puerto serie
    # Comando para listar los puertos disponibles: python -m serial.tools.list_ports
    # ser = serial.Serial('COM1')  # open serial port
    # print(ser.name)         # check which port was really used
    # ser.write(b'hello')     # write a string
    # ser.close()             # close port

    return render_template('predefinido.html')

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=3606)
