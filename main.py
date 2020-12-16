from . import db
from .models import User
from .models import Req
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required

main=Blueprint('main', __name__)
@main.route('/')
def landing():
    return render_template('landing/landing.html')
@main.route("/", methods=['GET','POST'])
def submit(): 
	if "login"==request.form.get("login"):
			return redirect(url_for('auth.login'))
	elif "register"==request.form.get("register"):
			return redirect(url_for('auth.signup'))

@main.route('/profile')
def profile():
    return render_template('profile/profile.html',name=current_user.name, email=current_user.email, address=current_user.address)
@main.route("/profile", methods=['GET','POST'])
def redirection(): 
    if "recycle"==request.form.get("recycle"):
        return redirect(url_for('main.recycle'))
    elif "redeem"==request.form.get("redeem"):
        return redirect(url_for('main.redeem'))
    elif "logout"==request.form.get("logout"):
        return redirect(url_for('auth.logout'))
@main.route('/redeem')
def redeem():
    return render_template('redeem/index.html')

@main.route('/recycle')
def recycle():
    return render_template('recycle/recycle.html')
@main.route("/recycle", methods=['POST'])
@login_required
def new_workout_post():
    ittype = request.form.get('itemtype')
    metal = request.form.get('metal')
    plastic=request.form.get('plastic')
    paper=request.form.get('paper')
    ewaste=request.form.get('ewaste')
    req = Req(metal=metal, plastic=plastic, paper=paper,ewaste=ewaste,address=current_user.address, user_id=current_user.id)
    db.session.add(req)
    db.session.commit()
    flash('Your request has been added!')
    return redirect(url_for('main.profile'))