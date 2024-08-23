from flask_login import LoginManager

from .database import database
from .user.model import User

login_manager = LoginManager()
login_manager.login_view = "/auth/signin"


@login_manager.user_loader
def load_user(id: str):
    return database.session.get(User, id)
