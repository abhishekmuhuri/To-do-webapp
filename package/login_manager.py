from . import app
from . import login_manager
from .model import User
from flask import render_template, url_for, redirect


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


@login_manager.user_loader
def user_loader(user_id: int):
    return User.query.filter_by(id=user_id)
