from flask import Blueprint, render_template

main=Blueprint('main', __name__)
@main.route('/')
def landing():
    return 'bruh'

@main.route('/profile')
def profile():
    return ''

@main.route('/redeem')
def redeem():
    return ""

@main.route('/recycle')
def recycle():
    return ""