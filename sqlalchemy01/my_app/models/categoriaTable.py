from my_app import db
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship

class Categoria(db.Model):
    __tablename__ = "TB_CATEGORIA"
    id   = Column(db.Integer, primary_key=True)
    name = Column(db.String(50), nullable=False)
    posts = relationship("Post")

    def __repr__(self):
        return '<Categoria %r>' % self.name
