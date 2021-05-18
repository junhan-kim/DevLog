import os
import unittest
import logging

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user
from app.main.model import blacklist


# app setting
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# logger setting
LOG_FORMATTER = logging.Formatter(
    '%(asctime)s | %(levelname)s | Message : %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(LOG_FORMATTER)
logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@manager.command
def run():
    logger.info('App is running.')
    app.run(host='0.0.0.0', port=5000)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
