from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    games_played = db.Column(db.Integer, default=0)
    games_won = db.Column(db.Integer, default=0)
    authenticated = db.Column(db.Boolean, default=False)
    
    def __init__(self, name, email, password, games_played):
        self.username = name
        self.email = email
        self.password = password
        self.games_played = games_played
        self.games_won = 0
        self.authenticated = False

    def __repr__(self):
        print "User id:{}".format(self.id)

    def is_authenticated(self):
        return self.authenticated
 
    def is_active(self):
        return True
 
    # def is_anonymous(self):
    #     return False
 
    def get_id(self):
        return unicode(self.id)