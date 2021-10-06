from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.relationship('OrderItem')


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(150))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    orders = db.relationship('Order')