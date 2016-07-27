from flask import render_template, url_for, redirect, request, abort
from flask import session, flash, g
from flask_login import login_user, logout_user, current_user, login_required
from . import app, db, login_manager
from .models import User
from .forms import LoginForm, RegisterForm


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    
@app.route('/')
@app.route('/index')
@login_required
def index():
    user_data = current_user
    return render_template('index.html', user_data=user_data)

@app.route('/register' , methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    user = User(request.form['username'], request.form['email'], request.form['password'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))
 
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = User.query.filter_by(username=username, password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user, remember = remember_me)
    session['logged_in'] = True
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()

    logout_user()
    return redirect(url_for('login'))