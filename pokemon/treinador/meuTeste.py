'''
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "ola novo player"

@app.route('/player', methods=['PUT'])
def player(nome):
    return nome

if __name__ == "__main__":
    app.run()
'''

def teste(nome, apelido):
    print(nome, apelido)

teste(('josé'),('ana'))