
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,request
from Lista_Doble_Enlazada import  ListaCircularDobleEnlazada
listadoble = ListaCircularDobleEnlazada()

global idusuario
app = Flask ("Drive")

@app.route('/')
def main ():
    return "Servidor en linea"


@app.route('/registro',methods=['POST'])
def registro():

    usuario = str(request.form['usuario'])
    password = str(request.form['password'])
    idusuario = + 1
    user = usuario +","+password
    listadoble.agregar_inicio(str(user))
    print ("usuario :"+usuario+ "+++++"+ "Password :" +password)

 # llamada a lista doble enlazada y a arbol b para crear su carpeta personal

    return "True"

@app.route('/ingreso',methods =['POTS'])
def ingreso():
    usuario = str(request.form['usuario'])
    password = str(request.form['password'])
    user = usuario +","+password
    registrado = listadoble.buscar(str(user))
    #llama a lista doble enlazada y verifica si el usuario es correcoto
    #retona un falsa si es incorrecto y un tru si es correcto
    if registrado ==True:
        return "True"
    else:
        return "False"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')