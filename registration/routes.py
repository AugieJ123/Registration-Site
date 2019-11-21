from flask import render_template, url_for, flash, redirect
from registration import app
from registration.forms import RegistrationForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html', title='Home')


@app.route('/testing')
def testing():
    return render_template('testing.html')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)
