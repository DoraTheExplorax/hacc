from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    address=db.Column(db.Text)
    #username=db.Column(db.Text)
    requests = db.relationship('Req', backref='author', lazy=True)
    
    


class Req(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plastic=db.Column(db.Integer,nullable=True)
    metal=db.Column(db.Integer,nullable=True)
    paper=db.Column(db.Integer,nullable=True)
    ewaste=db.Column(db.Integer,nullable=True)
    address=db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
