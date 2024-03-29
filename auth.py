from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth=Blueprint('auth',__name__)
@auth.route('/signup')
def signup():
    return render_template('reg/reg.html')
@auth.route('/signup', methods=['POST'])
def signup_post():
    #username=request.form.get('id15')
    email = request.form.get('email-id17')
    name = request.form.get('full-name16')
    password = request.form.get('password19')
    address=request.form.get('address18')
    #usrtyp=request.form.get('usrtyp')
    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()

    print(user)

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'),address=address)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login/login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        print("test because id ont trsut flash")
        return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=True)
    return redirect(url_for('main.profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.landing'))