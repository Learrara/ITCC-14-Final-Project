from flask import Blueprint, render_template, request, jsonify
from flask_sqlalchemy import sqlalchemy
from flask.json import jsonify
from flask_login import  login_required,current_user
from . import db
from sqlalchemy.sql.functions import user
from .models import User, Order
import json

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template("home.html", user=current_user)

@views.route('/about')
def about():
    return render_template("about.html")
@views.route('/contact')
def contact():
    return render_template ("contact.html")

@views.route('/homeMenu')
def homeMenu():
    return render_template ("homeMenu.html", user=current_user)

@views.route('/order')
def order():
    return render_template ("order.html")

@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashB():
    if request.method == 'POST':
        order = request.form.get('orderbutton')
        new_order = Order(itemname=order, user_id=current_user.id)
        db.session.add(new_order)
        db.session.commit()
        return render_template ("cart.html", user=current_user)
  
    return render_template ("dashboard.html", user=current_user)
    
    
@views.route('cart', methods=['GET', 'POST'])
@login_required
def cart():
    if request.method == 'POST':
        order = request.form.get('orderbutton')
        new_order = Order(itemname=order, user_id=current_user.id)
        db.session.add(new_order)
        db.session.commit()

    return render_template ("cart.html", user=current_user)

@views.route('/delete-order', methods=['POST'])
def delete_order():
    order = json.loads(request.data)
    orderId = order['orderId']
    order = Order.query.get(orderId)
    if order:
        if order.user_id == current_user.id:
            db.session.delete(order)
            db.session.commit()
    return jsonify({})


 
@views.route('/add-order', methods=['POST']) 
def add_order(): 
    new_order = Order(itemname=order, user_id=current_user.id)
    db.session.add(new_order)
    db.session.commit() 

@views.route('/clear-order', methods=['POST'])
def clear_orders():  
    user = current_user
    for order in user.orders:
        db.session.delete(order)
        db.session.commit()
    return jsonify({})