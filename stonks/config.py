import os
import secrets


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex())
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/stonks.db"


config = Config()
