import os
from flask import Flask
from models import db
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from . import views