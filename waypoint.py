from . import db
from .models import User
from .models import Req
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required

print(User.query.all().address)