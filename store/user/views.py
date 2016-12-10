# -*- coding: utf-8 -*- 
"""User views."""

from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_login import login_required, login_user, logout_user

from .forms import LoginForm, RegisterForm

from store.utils import flash_errors

from store.utils import manager_only


blueprint = Blueprint('user', __name__, url_prefix='/user',
                      static_folder='../static')


@blueprint.route('/members')
@login_required
def members():
    """
    - the list of the m most popular books (in terms of copies sold in this month)
    - the list of m most popular authors
    - the list of m most popular publishers 
    """
    return render_template('user/members.html')


@blueprint.route('/denied')
@login_required
@manager_only
def cannot_go_here():
    """Should not be here."""
    return "Should not see this."


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """Login route."""
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('user/login.html', form=form)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        User.create(id=form.username.data, email=form.email.data,
                    password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('user/register.html', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))
