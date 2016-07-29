from flask import render_template, url_for, redirect, request, abort
from flask import session, flash, g, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from . import app, db, login_manager
from .models import User
from .forms import LoginForm, RegisterForm, SettingsForm
from .helper import get_computer_move, check_winner

BOARD_SIZE = 3
USER_SIGN = 'O'
COMPUTER_SIGN = 'X'
game_board = []

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    
@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
@login_required
def index():
    form = SettingsForm()
    user = current_user
    if request.method == 'POST':
        USER_SIGN = form['user_sign']
        COMPUTER_SIGN = 'X' if USER_SIGN == 'O' else 'O'
        return redirect(url_for('game'))
    return render_template('index.html', user=user, form=form)

@app.route('/game', methods=['GET', 'POST'])
def game():
    global game_board
    if request.method == 'GET':
        game_board = ['' for x in range(BOARD_SIZE*BOARD_SIZE)]
        return render_template('game_play.html', 
            user=current_user, 
            game_board=game_board,
            board_capacity=BOARD_SIZE)
    else:
        print int(request.form['cell_id'])
        position = int(request.form['cell_id'])
        if game_board[position] != '':
            flash('This position already occupied')
            return jsonify({
                'status': 'error'
                })
        else:
            game_board[position] = USER_SIGN
            winner, win_line = check_winner(BOARD_SIZE, game_board)
            print winner
            print win_line
            if winner:
                if winner == USER_SIGN:
                    user = current_user
                    user.games_played += 1
                    db.session.add(user)
                    db.session.commit()
                    flash('Congratulations! You won!')
                else:
                    flash('Computer won! Try next time')
                return jsonify({
                    'status': 'ok',
                    'game_over': 'true',
                    'winner': winner,
                    'win_line': win_line
                })
            else:
                computer_move = get_computer_move(BOARD_SIZE, game_board, COMPUTER_SIGN, USER_SIGN)
                game_board[computer_move] = COMPUTER_SIGN

                return jsonify({ 
                    'status': 'ok',
                    'game_over': 'false',
                    'user_sign': USER_SIGN,
                    'computer_sign': COMPUTER_SIGN,
                    'computer_move': computer_move
                     })


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

# @app.route('/make_move', methods = ['POST'])
# @login_required
# def make_move():
#     return jsonify({
#         'sign': USER_SIGN,
#         'game_over': 'false' })