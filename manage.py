from app import create_app, db
from flask_script import Manager, Server
from app.models import Blog, User, Comment
from flask_migrate import Migrate, MigrateCommand

app = create_app('development')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)