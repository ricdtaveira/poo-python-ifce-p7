from my_app import db

class Categoria(db.Model):
    __tablename__ = "TB_CATEGORIA"
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    posts = db.relationship("Post")

    def __repr__(self):
        return '<Categoria %r>' % self.name
