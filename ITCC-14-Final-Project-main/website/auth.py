from os import error
from re import I
from flask import Blueprint, render_template, request, flash,redirect,url_for
from flask.helpers import flash 
from flask.json import jsonify
from sqlalchemy.sql.functions import user
from .import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user,current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.dashB'))
            else:
                flash('Incorrect password or email', category='error')
        else:
            flash('User does not exist.', category='error')
    # jsondata = jsonify(data)
    # print("[RETURN]")
    # print(jsondata)
    # print("[RETURN TYPE]")
    # print(type(jsondata))
    return render_template("login.html",user = current_user, ligma="red is", what="sussy")

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.homepage'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email') 
        userName = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(userName) < 4:
            flash('Username must be greater than 4 characters', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        elif password1 != password2:
            flash('Passwords does not match', category='error')
        else:
            new_user = User(email=email, username=userName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')  
            return redirect(url_for('views.homepage'))

    return render_template("signup.html", user=current_user)