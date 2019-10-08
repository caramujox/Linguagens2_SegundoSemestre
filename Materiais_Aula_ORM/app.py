from flask import Flask, request, jsonify
from models.produto import ProdutoModel
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prod2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/produto/', methods=['POST'])
def produto_post():
    corpo = request.get_json(force=True)
    prod = ProdutoModel(**corpo)
    try:
        prod.insert()
    except:
        return jsonify({'mensagem: ocorreu um erro interno'}), 500

    return jsonify(prod.toDict()), 201

@app.route('/produto/<int:id_entrada>', methods=['GET'])
def produto_get(id_entrada):
    try:
        prod = ProdutoModel.select_id(id_entrada)
    except:
        return jsonify({'mensagem': 'Ocorreu um erro interno'}), 500

    if prod:
        return jsonify(prod), 200
    else:
        return jsonify({'mensagem':'Produto nao encontrado'}), 404

@app.route('/produtos', methods=['GET'])
def todos_produtos_get():
    try:
        todosProdutos = ProdutoModel.select_all()
    except:
        return jsonify({'mensagem': 'Ocorreu um erro interno'}), 500
    
    lista_prod = []
    for prod in todosProdutos:
        lista_prod.append(prod.toDict())
    return jsonify({'produtos': lista_prod}), 200




@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
