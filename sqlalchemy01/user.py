from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./teste.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


def main():
    ## Criação do Banco de Dados
    db.create_all()

    ## Instaciar objetos (Criar)
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    joao  = User(username='João', email='joao@example.com')

    ##Persistir os objetos no Banco de Dados (Insert)
    db.session.add(admin)
    db.session.add(guest)
    db.session.add(joao)
    db.session.commit()

    ##Executar um Select * e Consulta
    print("Select User *")
    print(User.query.all())
    print("Select User com filtro")
    print(User.query.filter_by(username='admin').first())

if __name__ == '__main__':
    main()


