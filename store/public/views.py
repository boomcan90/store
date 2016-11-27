# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, render_template

from store.extensions import login_manager
# from store.public.forms import LoginForm
# from store.user.forms import RegisterForm
from store.user.models import User
# from store.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(str(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    return render_template('index.html')


# @blueprint.route('/about/')
# def about():
#     """About page."""
#     form = LoginForm(request.form)
#     return render_template('public/about.html', form=form)
