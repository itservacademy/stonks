from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import select

from ..database import database
from ..user.form import SigninForm, SignupForm
from ..user.model import User

blueprint = Blueprint("auth", __name__)


@blueprint.get("/auth/signin")
def render_signin():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.render_dashboard"))

    form = SigninForm()
    return render_template("/auth/signin.html", form=form)


@blueprint.get("/auth/signup")
def render_signup():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.render_dashboard"))

    form = SignupForm()
    return render_template("/auth/signup.html", form=form)


@blueprint.get("/auth/signout")
@login_required
def signout():
    logout_user()
    return redirect(url_for("auth.render_signin"))


@blueprint.post("/auth/signin")
def signin():
    form = SigninForm(request.form)

    if form.validate():
        statement = select(User).where(User.email == form.email.data)
        user = database.session.scalars(statement).one_or_none()

        if not user or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("auth.render_signin"))

        login_user(user)
        next = request.args.get("next")
        return redirect(next or url_for("dashboard.render_dashboard"))

    return render_template("/auth/signin.html", form=form)


@blueprint.post("/auth/signup")
def create_auth():
    form = SignupForm(request.form)

    if form.validate():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)

        database.session.add(user)
        database.session.commit()
        return redirect(url_for("auth.render_signin"))

    return render_template("auth/signup.html", form=form)
