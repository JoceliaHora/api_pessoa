#importando o flask pra criar um servidor REST

from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():
    return 'hello world'

@app.route('/cadastrar')    #path
def cadastrar():
    return "cadastrar"

@app.route('/buscar')
def buscar():
    return "buscar"

@app.route('/listar')
def listar():
    return "listar"

app.run(host='0.0.0.0', port=81)
