from my_app import db

class Usuario(db.Model):
    __tablename__ = 'TB_USUARIO'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))