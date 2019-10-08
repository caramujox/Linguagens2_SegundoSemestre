from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'caiao'
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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('cadastro.html', titulo = 'Cadastre o seu novo Jogo')

@app.route('/criar_jogo', methods = ['POST',])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if  'mestra' == request.form['senha']:
        session ['usuario_ogado'] = request.form['usuario']
        flash(request.form['usuario'] + 'logado')
        proxima_pagina =  request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
        return redirect('/')
    else:
        flash('Não logado, tente de novo!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('None user logado')
    return redirect ('/')

app.run(debug = True)