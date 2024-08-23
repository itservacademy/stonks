from sqlalchemy import select
from wtforms import (
    EmailField,
    Form,
    PasswordField,
    StringField,
    ValidationError,
    validators,
)

from ..database import database
from .model import User


class SigninForm(Form):
    email = EmailField("Email", [validators.Length(min=6, max=35)])
    password = PasswordField("Password", [validators.DataRequired()])


class SignupForm(Form):
    name = StringField("Name", [validators.DataRequired()])
    email = EmailField("Email", [validators.Length(min=6, max=35)])
    password = PasswordField("New Password", [validators.DataRequired()])

    def validate_email(form, field):
        statement = select(User).where(User.email == field.data)
        user = database.session.scalars(statement).one_or_none()

        if user:
            raise ValidationError("Email already in use")
