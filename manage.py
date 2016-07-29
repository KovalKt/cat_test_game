import os
from flask_script import Manager
from cat_game import app

manager = Manager(app)


@manager.command
def init_db():
    '''Initialise database. Create schema'''
    from cat_game import app, db
    with app.app_context():
        db.create_all()


@manager.command
def add_records_for_test():
    '''Add few test records to table User '''
    from cat_game import app, db
    from cat_game.models import User
    with app.app_context():
        user1 = User('Ivan', 'ivan@gmail.com', '123456', 1)
        user2 = User('admin', 'admin@ukr.net', 'default', 5)
        user3 = User('Vasia', 'vasiliy@mail.ru', 'qwerty', 0)

        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.commit()

@manager.command
def run_app():
    init_db()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    manager.run()