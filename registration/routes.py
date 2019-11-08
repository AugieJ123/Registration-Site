from flask import render_template, url_for, flash, redirect
from registration import app
from registration.forms import LoginForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'augie@demo.com' and form.password.data == 'password':
            flash('You have been logged in to your account', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login is Unsuccessful')
    return render_template('login.html', title='Login', form=form)

