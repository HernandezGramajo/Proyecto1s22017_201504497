from flask import Flask,request

app = Flask ("Drive")

@app.route('/')
def main ():
    return "Servidor en linea"


@app.route('/registro',methods=['POST'])
def registro():

    usuario = str(request.form['usuario'])
    contraseña = str(request.form['contraseña'])

 # llamada a lista doble enlazada y a arbol b para crear su carpeta personal

    return "Su registro fue existoso"

@app.route('/ingreso',metods =['POTS'])
def ingreso():
    usuario = str(request.form['usuario'])
    contraseña = str(request.form['contraseña'])

    #llama a lista doble enlazada y verifica si el usuario es correcoto
    #retona un falsa si es incorrecto y un tru si es correcto

    return "fals o true"