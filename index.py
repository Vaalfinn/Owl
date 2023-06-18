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
app.config['MYSQL_DB'] = 'owldb_v1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# Inicio de la web (index, hub, hobby)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

# Reder tempalate a login
@app.route('/login')
def login():
    return render_template('login.html')

# Uso de prueba para la conexión de la base de datos
@app.route('/prueba1', methods=['GET','POST'])
def prueba1(): 
    if request.method=='POST':
        #id_usuario = request.form['id_usuario']
        aux_nom_usuario = request.form['nom_usuario']
        aux_nombre = request.form['nombre']
        aux_ap_paterno = request.form['ap_paterno']
        aux_ap_materno = request.form['ap_materno']
        aux_correo = request.form['correo']
        aux_passw = request.form['passw']
        
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='owldb_v1' )
        cursor = conn.cursor()
                
        cursor.execute('insert into usuarios '
                    ' (nom_usuario, nombre, ap_paterno, ap_materno, correo, passw) '
                    ' VALUES (%s, %s, %s, %s, %s, %s) ', 
                    (aux_nom_usuario, aux_nombre, aux_ap_paterno, aux_ap_materno, aux_correo, aux_passw))
        conn.commit()
        conn.close()
    return render_template('prueba1.html')



# confirmar funcionamiento 
#@app.route('/jalo/<string:id>', methods=['GET'])
app.route('/jalo')
def jalo():
    #conn = pymysql.connect(host='localhost', user='root', passwd='', db='owldb_v1' )
    #cursor = conn.cursor()
    #cursor('select count(*) from usuarios from id_usuario ={0}'.format(id))
    #aver=cursor.fetchall()
    return render_template('jalo.html')
    


# fin del programa
if __name__ == '__main__':
    app.run(port=5000,debug=True)
    
    #En caso de cambiar el port, notificar al resto del equipo