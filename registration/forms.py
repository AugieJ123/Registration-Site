from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField  # it import string field and password like username and others...
from wtforms.validators import DataRequired, Length, Email, EqualTo


# creating a class for the login forms

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# creating a class for the registration forms

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=4, max=50)])
    middle_name = StringField('Middle Name', validators=[DataRequired(), Length(min=4, max=50)])
    surname_name = StringField('Surname', validators=[DataRequired(), Length(min=4, max=50)])
    mother_name = StringField("Mother's Name", validators=[DataRequired(), Length(min=4, max=50)])
    father_name = StringField("Father's Name", validators=[DataRequired(), Length(min=4, max=50)])
    address = StringField('Address', validators=[DataRequired(), Length(min=4, max=50)])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])   # Check the username and also check for validation
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
