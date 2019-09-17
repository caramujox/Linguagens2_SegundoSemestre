from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Resource, Api

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "HelloWorld!"

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Super Mario', 'Acao', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
lista = [jogo1, jogo2]       


@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos = lista)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo = 'Cadastre o seu novo Jogo')

@app.route('/criar_jogo', methods = ['POST',])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

app.run(debug = True)