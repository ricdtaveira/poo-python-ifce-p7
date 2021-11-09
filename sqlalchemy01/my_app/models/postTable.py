from my_app import db
from datetime import datetime
"""
A Classe Post (Filho) está relacionada com a Classe Categoria (Pai)
da seguinte forma:     
    Um Post está relacionado a uma Categoria
    Uma Categoria está relacionada a muitos Posts 
No lado da classe Post (Filho) é definido a chave estrangeira categoria_id.
"""
class Post(db.Model):
    __tablename__ = "TB_POST"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    categoria_id = db.Column(db.Integer, db.ForeignKey('TB_CATEGORIA.id'),
        nullable=False)
    categoria = db.relationship('Categoria',
        backref=db.backref('TB_POST', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title