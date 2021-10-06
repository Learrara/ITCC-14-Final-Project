from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", ligma="red is", what="sussy")

@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/signup')
def signup():
    return render_template("signup.html")