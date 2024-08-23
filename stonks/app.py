from flask import Flask

from .config import config
from .dashboard.route import blueprint as dashboard_blueprint
from .database import database
from .security import login_manager
from .user.route import blueprint as user_blueprint


def create_app():
    app = Flask(__name__, template_folder="../templates")
    register_config(app)
    register_database(app)
    register_login_manager(app)
    register_blueprints(app)
    return app


def register_config(app: Flask):
    app.config.from_object(config)
    app.json.sort_keys = False


def register_database(app: Flask):
    database.init_app(app)

    with app.app_context():
        database.create_all()


def register_login_manager(app: Flask):
    login_manager.init_app(app)


def register_blueprints(app: Flask):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(dashboard_blueprint)
