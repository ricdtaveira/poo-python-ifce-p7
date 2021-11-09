from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:\\Desenvolvimento\\poo-python-ifce-p7\\sqlalchemy01\\my_app\\data\\DB_DATA.db'
app.debug = True

db = SQLAlchemy(app)

