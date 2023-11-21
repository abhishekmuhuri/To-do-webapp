from . import db
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, unique=False, nullable=False)
    last_name = db.Column(db.String, unique=False, nullable=False)
    hashed_password = db.Column(db.String, unique=False, nullable=False)
    gender = db.Column(db.String, unique=False, nullable=False)
    role = db.Column(db.String, unique=False, nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True, cascade='all, delete-orphan')

    def __init__(self, username: str, email: str, first_name: str, last_name: str, password: str, gender: str,
                 role: str):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.hashed_password = generate_password_hash(password=password)
        self.gender = gender
        self.role = role

    def __repr__(self):
        return f"User : {self.username}, ID : {self.id}, Email : {self.email}"


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.Integer, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Integer, nullable=False, default="None")
    done = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, user_id: int, title: str, priority: str, description: str):
        self.user_id = user_id
        self.title = title
        self.priority = priority
        self.description = description

    def __repr__(self):
        return f"User ID {self.user_id}, Title: {self.title}, Priority: {self.priority}, Description: {self.description}"
