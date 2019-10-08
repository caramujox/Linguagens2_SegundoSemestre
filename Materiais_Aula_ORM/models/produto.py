from db import db

class ProdutoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable = False)
    preco = db.Column(db.Float)

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def toDict(self):
        return {'id':self.id, 'nome':self.nome, 'preco':self.preco}

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def select_all(cls):
        return cls.query.all()

    @classmethod
    def select_id(cls, id_entrada):
        prod = cls.query.filter_by(id=id_entrada).first()
        return (prod.toDict())

