from flask import Blueprint,render_template

auth=Blueprint('auth',__name__)
@auth.route('/signup')
def signup():
    return 's'
@auth.route('/login')
def login():
    return "l"

@auth.route('/')
def logout():
    return "lo"