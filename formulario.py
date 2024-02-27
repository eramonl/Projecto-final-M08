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
      nom = request.form['Nombre']
      nom = nom.capitalize() #en majúscules la primera lletra
      correu = mail_db.getmaildb(nom)
      return render_template('resultadogettmail.html',nom=nom,correu=correu)
   else:
      return render_template('getmail.html')

@app.route('/addmail',methods = ['POST', 'GET'])
def addmail():
   if request.method == 'POST':
      modif=False
      nom = request.form['Nombre']  #ull! si no ve, això acaba amb error
      nom=nom.capitalize()
      correu = request.form['correu']
      if 'modif' in request.form: #el checkbox és opcional 
         modif = True
      result_msg = mail_db.addmaildb(nom, correu, modif)
      return render_template('resultadoaddmail.html',nom = nom, correu=correu,  result_msg = result_msg)
   else:
      return render_template('addmail.html')

@app.route('/login',methods = ['POST', 'GET'])
def paguinaPublica():
   return render_template('Paguina_publica.html')

@app.route('/private' ,methods = ['POST', 'GET'])
def paguinaprivada():
   return render_template('Paguina_privada.html')

if __name__ == '__main__':
   app.run(debug = True)