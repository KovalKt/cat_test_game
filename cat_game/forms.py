from flask_wtf import Form
# from flask.ext.wtf.html5 import IntegerField
from wtforms.fields import TextField, BooleanField
from wtforms.validators import Required, Length


class LoginForm(Form):
    username = TextField('Username', [Required(), Length(min=5, message='Too short username')])
    password = TextField('Password', [Required(), Length(min=6, message='Must be at least 6 symbols')])
    remember_me = BooleanField('Remember me')

class RegisterForm(Form):
    username = TextField('Username', [Required(), Length(min=5, message='Too short username')])
    email = TextField('Email', [Required(), Length(max=80, message='You should provide valid email')])
    password = TextField('Password', [Required(), Length(min=6, message='Must be at least 6 symbols')])
