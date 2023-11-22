import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager = LoginManager()

# create the extension

db = SQLAlchemy()


# create the app
app = Flask(__name__, template_folder='../templates')

login_manager.init_app(app)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo_app.db"
app.config['SECRET_KEY'] = 'my-key'

# initialize the app with the extension
db.init_app(app)
