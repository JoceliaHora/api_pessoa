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
    return banco.salvaNoBanco(request.json)


@app.route('/listar', methods = ["GET"])
def listar():
    return banco.listarPessoas()

@app.route('/', methods =["DELETE"])
def deletar():
    cpf = request.args.get("cpf")
    return banco.deletarPessoa(cpf)

app.run(host='0.0.0.0', port=81)
