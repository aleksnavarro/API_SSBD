from flask import Flask,request,make_response,jsonify
import mysql.connector
from usuario import Usuario
from invernadero import Invernadero

conexion=mysql.connector.connect(user="alejandro",password="12345",database="invernadero")
cursor=conexion.cursor()

app = Flask(__name__)

@app.route("/home/")
def hello():
    #return "Hello World!"
    respuesta=make_response("hello world")
    respuesta.headers.add('Access-Control-Allow-Origin','*')
    return respuesta

#http://127.0.0.1:5000/login/?usuario=alejandro&password=12345
@app.route("/login/",methods=['GET'])
def login():
    #print(request.args)
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    userDB = Usuario(conexion,cursor)
    respuesta=make_response(str(userDB.login(usuario,password)))
    respuesta.headers.add('Access-Control-Allow-Origin','*')
    #print(userDB.login(usuario,password))
    return respuesta

    #print(usuario,password)
    #return "Para hacer login"
    #return usuario + " " + password

@app.route("/invernadero/",methods=['GET'])
def invernadero():
    usuario=request.args.get('usuario')
    print(usuario)

    inv=Invernadero(conexion,cursor)
    resultado=inv.buscar(usuario)
    print(resultado)

    return jsonify(resultado)

app.run(debug=True)
