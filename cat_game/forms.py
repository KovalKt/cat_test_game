from flask_wtf import Form
from wtforms.fields import TextField, BooleanField, RadioField
from wtforms.validators import Required, Length


class LoginForm(Form):
    username = TextField('Username', [Required(), Length(min=5, message='Too short username')])
    password = TextField('Password', [Required(), Length(min=6, message='Must be at least 6 symbols')])

class RegisterForm(Form):
    username = TextField('Username', [Required(), Length(min=5, message='Too short username')])
    email = TextField('Email', [Required(), Length(max=80, message='You should provide valid email')])
    password = TextField('Password', [Required(), Length(min=6, message='Must be at least 6 symbols')])

class SettingsForm(Form):
    user_sign = RadioField('Your sign', [Required()], choices=[('X', 'X'), ('O', 'O')], default='O')
