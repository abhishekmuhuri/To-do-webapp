from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, AnyOf


class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired(), Length(min=1, max=64)])
    password = PasswordField("Password :", validators=[DataRequired()])
    submit = SubmitField("Login")


class UserForm(FlaskForm):
    first_name = StringField("First Name:", validators=[DataRequired(), Length(min=1, max=64)])
    last_name = StringField("Last Name:", validators=[DataRequired(), Length(min=1, max=64)])
    username = StringField("Username:", validators=[DataRequired(), Length(min=1, max=64)])
    email = StringField("Email:", validators=[DataRequired(), Email(), Length(min=3, max=320)])
    password = PasswordField("Password:",
                             validators=[DataRequired(), EqualTo('confirm_pass', "Passwords doesn't match"),
                                         Length(min=5, max=64)])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired(), AnyOf(['male', 'female'], message='Invalid gender')])
    confirm_pass = PasswordField("Confirm Password:", validators=[DataRequired(), Length(min=5, max=64)])
    role = StringField("Job Role:", validators=[DataRequired()])
    submit = SubmitField("Register")


class TaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=1, max=64)])
    priority = SelectField("Task Priority: ", choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired(), Length(0, 256)])
