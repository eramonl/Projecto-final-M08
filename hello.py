from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/el-numero/<int:numero>")
def par_impar(numero):
    if (numero%2) == 0:
        return "Es par"
    else:
        return "Es impar"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hola.html', name=name)


@app.route('/edad100/<nombre>')
@app.route('/edad100/<nombre>/<int:edad>')
def edad100(nombre=None,edad=None):
    año=2023-edad
    cien=str(año+100)
    return render_template('edad100.html', nombre=nombre, edad=edad, cien=cien)