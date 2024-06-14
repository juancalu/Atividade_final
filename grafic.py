import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bem vindo ao site de animes</h1>'

@app.route('/anime')
def livros():
    dados = pd.read_csv('anime.csv')
    todos = dados['NOME'].tolist()  # Converter a série para lista
    return jsonify(todos)


if __name__ == '__main__':
    app.run(debug=True)