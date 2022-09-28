#importando o flask pra criar um servidor REST

from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():
    return 'hello world'

app.run(host='0.0.0.0', port=81)
