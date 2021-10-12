from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    itemname = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(150), unique=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    orders = db.relationship('Order')
