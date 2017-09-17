
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,request

app = Flask ("Drive")

@app.route('/')
def main ():
    return "Servidor en linea"


@app.route('/registro',methods=['POST'])
def registro():

    usuario = str(request.form['usuario'])
    password = str(request.form['password'])

    print ("usuario :"+usuario+ "+++++"+ "Password :" +password)

 # llamada a lista doble enlazada y a arbol b para crear su carpeta personal

    return "Su registro fue existoso"

@app.route('/ingreso',methods =['POTS'])
def ingreso():
    usuario = str(request.form['usuario'])
    password = str(request.form['password'])

    #llama a lista doble enlazada y verifica si el usuario es correcoto
    #retona un falsa si es incorrecto y un tru si es correcto

    return "fals o true"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')