#importando o flask pra criar um servidor REST

from flask import Flask, request
import banco

app = Flask(__name__)

@app.route('/', methods=["GET"])  #define o endpoint
def test():                       # realiza o processamento
    return "teste servidor OK \n" + banco.testeBanco()


@app.route('/', methods=["POST"])    #path
def cadastrar():
    print(request.json)
    return "cadastrar"

@app.route('/buscar', methods =["GET"])
def buscar():
    print(request.args.get('cpf'))
    return "buscar"

@app.route('/listar', methods = ["GET"])
def listar():
    return "listar"

@app.route('/', methods =["DELETE"])
def deletar():
    print(request.args.get("cpf"))
    return "deletar"

app.run(host='0.0.0.0', port=81)
