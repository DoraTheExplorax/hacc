from flask import Blueprint, render_template

main=Blueprint('main', __name__)
@main.route('/')
def landing():
    return 'bruh'

@main.route('/profile')
def profile():
    return render_template('profile.html')

@main.route('/redeem')
def redeem():
    return render_template('index.html')

@main.route('/recycle')
def recycle():
    return ""