import datetime

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask02.config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
#migrate = Migrate(app, db)

tags = db.Table(
    'TB_POST_TAGS',
    db.Column('post_id', db.Integer, db.ForeignKey('TB_POST.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('TB_TAG.id'))
)


# Define uma Tabela User
class User(db.Model):
    __tablename__ = 'TB_USER'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False, index=True, unique=True)
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy='subquery')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        # formats what is shown in the shell when print is
        # called on it
        return '<Usuário {}>'.format(self.username)

#Define uma Tabela Post
class Post(db.Model):
    __tablename__ = 'TB_POST'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime(), default=datetime.datetime.now)
    user_id = db.Column(db.Integer(), db.ForeignKey('TB_USER.id'))
    comments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )
    tags = db.relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)


class Comment(db.Model):
    __tablename__ = 'TB_COMMENT'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.datetime.now)
    post_id = db.Column(db.Integer(), db.ForeignKey('TB_POST.id'))

    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])


class Tag(db.Model):
    __tablename__ = 'TB_TAG'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Tag '{}'>".format(self.title)


@app.route('/')
def home():
    result = "<h1>Tabelas</h1><br><ul>"
    for table in db.metadata.tables.items():
        result += "<li>%s</li>" % str(table)
    result += "</ul>"
    return result


@app.route('/usuario', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Favor entrar todos os valores dos campos', 'error')
        else:
            user = User(request.form['username'], request.form['password'])
            db.session.add(user)
            db.session.commit()
           ## flash('Registro foi inserido com sucesso')
            return redirect(url_for('showUsuarios'))
    return render_template('usuario.html', title='Usuários')

@app.route('/usuario/add/')
def addUsuario():
    result = "<h1>Adição de Usuários</h1><br><ul>"
    admin = User(username='admin', password='123456')
    guest = User(username='guest', password='654321')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    result +=  "<p>Usuários Adicionados</p>"
    return result

@app.route('/usuario/del/<int:id>')
def delUsuario(id):
    result = "<h1>Exclusão de Registro</h1><br><ul>"
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    result += '<p>Usuário -> Id=' + str(user.id) + ' Excluido!</p>'
    return result

@app.route('/usuario/show/<int:id>')
def showUsario(id):
    user=User.query.get(id)
    result = "<h1>Consulta a Registro</h1><br><ul>"
    result += "<p> Id=" + str(user.id) + "</p>"
    result += "<p> Nome="  + user.username + "</p>"
    result += "<p> Senha=" + user.password + "</p>"
    return result

@app.route('/usuarios')
def showUsuarios():
    users=User.query.order_by(User.username).all()
    result=  '<h1>Usuários</h1><br><ul>'
    for user in users:
        result += '<p>'
        result += 'Id=' + str(user.id)
        result += ' Nome=' + user.username
        result += ' Senha=' + user.password
        result += '</p>'
    return result


if __name__ == '__main__':
    db.create_all()

    app.run()