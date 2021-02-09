import datetime

from flask import Flask
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

    def __init__(self, username):
        self.username = username

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

@app.route('/usuario/add/')
def addUsuario():
    pass

@app.route('/usuario/del/')
def delUsuario():
    pass

@app.route('/usuario/show/')
def showUsario():
    pass



if __name__ == '__main__':
    db.create_all()

    app.run()