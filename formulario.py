from flask import Flask
from flask import render_template
from flask import request
import sys
from flask import Flask, redirect, url_for, request
import mysql.connector
import mail_db
app = Flask(__name__)




#NOTROBAT = "NOTROBAT"
#AFEGIT = "AFEGIT"
#MODIFICAT = "MODIFICAT"
#JAEXISTEIX = "JAEXISTEIX"

# def agregar_usuario(user):
#        cursor = self.conexion.obtener_cursor()
#        nombre = str(input("Ingresa el nombre del nuevo usuario: "))
#        correo = str(input("Ingresa el correo del nuevo usuario: "))
#        cursor.execute("INSERT INTO alumnos (Nombre, Correo) VALUES (%s, %s)", (nombre, correo))
#        self.conexion.connection.commit()
#        print("Usuario agregado correctamente.")

#def getmaillista(nom):
#    if nom in lista:
#        return lista[nom]
#    else:
#        return "No esta"

@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
   if request.method == 'POST':
      modif=False
      contraseña = request.form['Contraseña']
      correu = request.form['correu']
      #comprobar si existe en BD
      #si existe - LOGIN OK
      #session['correu']=correu ----> Linea Buena
      return render_template('Paguina_privada.html', correu = correu, contraseña = contraseña)
      #si no existe - redirect al getmail
   else:
      return render_template('getmail.html')

@app.route('/addmail',methods = ['POST', 'GET'])
def addmail():
   if request.method == 'POST':
      modif=False
      contraseña = request.form['Contraseña']  #ull! si no ve, això acaba amb error
      correu = request.form['correu']
      if 'modif' in request.form: #el checkbox és opcional 
         modif = True
      result_msg = mail_db.addmaildb(contraseña, correu, modif)
      return render_template('Paguina_privada.html',contraseña = contraseña, correu=correu,  result_msg = result_msg)
   else:
      return render_template('addmail.html')

@app.route('/',methods = ['POST', 'GET'])
def paginaPublica():
   if session.get('correu'):
      return render_template('Paguina_privada.html', correu = session['correu'])
   else:
      return render_template('Paguina_publica.html')

@app.route('/private' ,methods = ['POST', 'GET'])
def paguinaprivada():
   return render_template('Paguina_privada.html')

@app.route('/patatas' ,methods = ['POST', 'GET'])
def patatas():
   return render_template('patatas.html')

@app.route('/flask' ,methods = ['POST', 'GET'])
def flask():
   return render_template('Practicas_flask.html')

@app.route('/ej1' ,methods = ['POST', 'GET'])
def ej1():
   return render_template('edad+100.py')


@app.route('/logout')
def logout():
   if session.get('correu'):
      session.pop('correu',default=None)
   return redirect(url_for('paginaPublica'))

if __name__ == '__main__':
   app.run(debug = True)