from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./Posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name

def main():
    ## Criação do Banco de Dados
    db.create_all()

    ## Criar uma Categoria
    py = Category(name='Python')

    ## Criar um Post e associar a categoria py
    Post(title='Hello Python!', body='Python is pretty cool', category=py)

    ## Cria um Post p
    p = Post(title='Snakes', body='Ssssssss')

    ## Associa o p ao conjunto de Posts da Categoria py
    py.posts.append(p)
    db.session.add(py)
    db.session.commit()

    ##Executar um Select com um filtro
    print("Select Posts filtro")
    print(Post.query.filter_by(category_id=1).all())

    ## print(py.posts)

if __name__ == '__main__':
    main()


