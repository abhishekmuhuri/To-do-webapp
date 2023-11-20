from flask import flash, abort
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from flask_login import login_user
from werkzeug.security import check_password_hash

from . import app
from . import db
from .forms import UserForm, LoginForm, TaskForm
from .model import User, Task


# Login/Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserForm()
    if form.validate_on_submit():
        # Getting Form data
        username = form.username.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data

        new_user = User(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username)
        if user is not None and check_password_hash(user.hashed_password, password):
            login_user(user)
            flash("Logged in", category='message')
        else:
            return redirect(url_for('home'), code=401)
    return render_template('login.html', form=form)


@app.route('/test')
def test():
    return "<h1>Hello</h1>"


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    all_tasks = Task.query.all()
    return render_template('home.html', tasks=all_tasks)


@app.route('/create_task', methods=['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        title = form.title.data
        priority = form.priority.data
        description = form.description.data

        new_task = Task(current_user.id, title, priority, description)

        db.session.add(new_task)
        db.session.commit()
        flash(f"Task {title} created", category='info')
        return redirect(url_for('home'))
    return render_template('create_task', current_user=current_user)


@app.route("/delete_task", methods=['GET', 'POST'])
@login_required
def delete_task():
    task_id = request.args.get('task_id'.casefold(), default=None)
    if task_id is None:
        abort(400, "Bad Request: Task ID missing")
    else:
        task = Task.query.get(task_id)
        if task is not None and task.user_id == current_user.id:
            db.session.delete(task)
            db.commit()
        else:
            abort(400, "Bad Request: Task ID missing")
    return render_template('delete_task.html', current_user=current_user)
