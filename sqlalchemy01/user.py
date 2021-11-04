from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./teste.db'
db = SQLAlchemy(app)

## Defiição de uma classe User que será mapeada para uma tabela User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User> id=' + str(self.id) + ' username=' + str(self.username) + ' email=' + str(self.email)


def main():
    ## Criação do Banco de Dados
    db.create_all()

    ## Instanciar objetos (Criar)
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    joao  = User(username='João',  email='joao@example.com')

    ##Persistir os objetos no Banco de Dados (Insert)
    db.session.add(admin)
    db.session.add(guest)
    db.session.add(joao)
    db.session.commit()

    ##Executar um Select *
    print("Select User *")
    print(User.query.all())

    ##Executar um Select com um filtro
    print("Select User com filtro")
    print(User.query.filter_by(username='admin').first())

if __name__ == '__main__':
    main()


