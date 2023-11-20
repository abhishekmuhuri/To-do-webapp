from flask import url_for, redirect

from . import login_manager
from .model import User


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


@login_manager.user_loader
def user_loader(user_id: int):
    return User.query.filter_by(id=user_id).first()
