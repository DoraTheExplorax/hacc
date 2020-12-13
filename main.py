from . import db
from .models import User
from .models import Req
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required

main=Blueprint('main', __name__)
@main.route('/')
def landing():
    return render_template('landing\\landing.html')

@main.route('/profile')
def profile():
    return render_template('profile\\profile.html',name=current_user.name, username=current_user.username, email=current_user.email, address=current_user.address)

@main.route('/redeem')
def redeem():
    return render_template('redeem\\index.html')

@main.route('/recycle')
def recycle():
    return render_template('recycle\\recycle.html')
@main.route("/recycle", methods=['POST'])
@login_required
def new_workout_post():
    ittype = request.form.get('itemtype')
    quantity = request.form.get('quantity')
    req = Req(item=ittype, quantity=quantity, author=current_user, address=current_user.address)
    db.session.add(req)
    db.session.commit()
    flash('Your request has been added!')
    return redirect(url_for('main.profile'))