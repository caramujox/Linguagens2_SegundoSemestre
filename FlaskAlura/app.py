from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "HelloWorld!"


@app.route('/jogoteca')
def jogoteca():
    return render_template('lista.html')

app.run()