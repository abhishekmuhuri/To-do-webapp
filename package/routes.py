from sqlalchemy.exc import IntegrityError

from flask import flash, abort
from flask import request
from flask_login import current_user, login_required
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from flask import render_template

from . import db, app
from .forms import UserForm, LoginForm, TaskForm
from .login_manager import *
from .model import Task


# Login/Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        gender = form.gender.data
        role = form.role.data
        new_user = User(username=username, email=email, first_name=first_name, last_name=last_name, password=password,
                        gender=gender, role=role)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registered successfully!', category='success')
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            if User.query.filter_by(email=email).first() is not None:
                flash("This email is already registered",'error')
            else:
                flash("This username is already registered", 'error')
            return redirect(url_for('register'))
    return render_template('register.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('Logged out!', category='success')
        return redirect(url_for('login'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()  # Use first() to get the user object

        if user is not None and check_password_hash(user.hashed_password, password):
            login_user(user)
            flash("Logged in", category='success')
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password", category='error')

    return render_template('login.html', form=form)


@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    all_tasks = Task.query.all()
    return render_template('home.html', all_tasks=all_tasks)


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
        flash(f"Task {title} created", category='success')

    return render_template('create_task.html', current_user=current_user, form=form)


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


# Remove Task / Task Done
@app.route('/remove_task/<int:task_id>', methods=['POST'])
@login_required
def remove_task(task_id):
    task = Task.query.get_or_404(task_id)
    if current_user.id == task.user_id:
        db.session.delete(task)
        db.session.commit()
        flash(f"Task {task.title} removed", category='success')

    return redirect(url_for('home'))


@app.route('/mark_done/<int:task_id>', methods=['POST', 'GET'])
@login_required
def mark_done(task_id):
    task = Task.query.get_or_404(task_id)
    if current_user.id == task.user_id:
        task.done = True
        db.session.commit()
        flash(f"Task {task.title} marked as done", category='success')

    return redirect(url_for('home'))


@app.route('/mark_undone/<int:task_id>', methods=['POST', 'GET'])
@login_required
def mark_undone(task_id):
    task = Task.query.get_or_404(task_id)
    if current_user.id == task.user_id:
        task.done = False
        db.session.commit()
        flash(f"Task {task.title} marked as undone", category='danger')

    return redirect(url_for('home'))


