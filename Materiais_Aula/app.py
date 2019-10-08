from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy​

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/prod.db'
db = SQLAlchemy(app)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable = False)
    price = db.Column(db.Float(120))

    def __init__(self, nome, preco)
    self.nome = name
    self.price = price

    def toDict(self):
        return {'id':self.id, 'name':self.name, 'price':self.price}

@app.route('/produto/', methods=['POST'])
def produto_post():
    corpo = request(force=True)

    prod = Produto(**corpo) #Produto(corpo.name, corpo.price) ou Produto(corpo['name'], corpo.price['preco'])
    db.session.add(prod)
    db.session.commit()

    return jsonify(prod.toDict()), 201



