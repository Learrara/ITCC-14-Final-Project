from re import I
from flask import Blueprint, render_template, request, flash
from flask.helpers import flash 
from flask.json import jsonify

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form 
    print("")
    print(data)
    print("")
    # jsondata = jsonify(data)
    # print("[RETURN]")
    # print(jsondata)
    # print("[RETURN TYPE]")
    # print(type(jsondata))
 
    return render_template("login.html", ligma="red is", what="sussy")

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return "logout"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email') 
        userName = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(userName) < 4:
            flash('Username must be greater than 4 characters', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        elif password1 != password2:
            flash('Passwords does not match', category='error')
        else:
            flash('Account created', category='success')  

    return render_template("signup.html")