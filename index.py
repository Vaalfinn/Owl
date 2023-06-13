# Se importan los frameworks 
from flask import Flask, g, render_template, request, redirect, url_for, session, json, jsonify
import pymysql
from flask_mysqldb import MySQL,MySQLdb

# Nombre de la aplicación para la ejecución 
app = Flask(__name__)
# sesion
app.secret_key = 'mysecretkey'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'owldb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


app=Flask(__name__)

# Inicio de la web (index, hub, hobby)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

# Uso de prueba para la conexión de la base de datos
@app.route('/prueba1')
def prueba1(): 
    if request.method=='POST':
        #id_usuario = request.form['id_usuario']
        nom_usuario = request.form['nom_usuario']
        nombre=request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_paterno']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='owldb')
        cursor = conn.cursor()
        cursor.execute('insert into usuario (id_usuario, nom_usuario, nombre, ap_paterno, ap_materno, correo, contrasena) VALUES (%s, %s, %s, %s, %s, %s)', (nom_usuario, nombre, ap_paterno, ap_materno, correo, contrasena))
        conn.close()
        cursor.fetchall()
    return render_template('prueba1.html')

# Reder tempalate a login
@app.route('/login')
def login():
    return render_template('login.html')

# fin del programa
if __name__ == '__main__':
    app.run(port=5000,debug=True)
    
    #En caso de cambiar el port, notificar al resto del equipo