# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from flask import flash
from functools import wraps
from flask import abort
from flask_login import current_user


def flash_errors(form, category='warning'):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash('{0} - {1}'.format(getattr(form, field).label.text, error), category)


def manager_only(f):
    """Permission decorator."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.user_type == "manager":
            abort(401)
        return f(*args, **kwargs)
    return decorated_function
