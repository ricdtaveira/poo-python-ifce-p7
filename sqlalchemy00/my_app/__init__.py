from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:\\Desenvolvimento\\poo-python-ifce-p7\\sqlalchemy00\\DB_DATA.db'
app.debug = True

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = "TB_PERSON"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='TB_PERSON', lazy=True)

    def __repr__(self):
        return '<Person %r>' % self.name

    def printAddresses(self):
        return 'Name= ' + self.name + 'Addresses= ' + self.addresses

class Address(db.Model):
    __tablename__ = "TB_ADDRESS"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('TB_PERSON.id'),
        nullable=False)

    def __repr__(self):
        return '<Address %r>' % self.email
