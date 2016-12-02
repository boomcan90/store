
# -*- coding: utf-8 -*-
"""User views."""

from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_login import login_required, login_user, logout_user

from .forms import RegisterForm

from .forms import LoginFormCustomer

from store.utils import flash_errors

from .models import Customer


customer_blueprint = Blueprint(
    'customer', __name__, url_prefix='/customer', static_folder='../static')


@customer_blueprint.route('/members')
@login_required
def members():
    """Customer Index Route."""
    return "customer"


@customer_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """Customer Login."""
    form = LoginFormCustomer(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.customer)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get(
                'next') or url_for('customer.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('customer/login.html', form=form)


@customer_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        Customer.create(id=form.customername.data, email=form.email.data, m_credit_no=form.m_credit_no.data,
                        phone_no=form.phone_no.data, address=form.address.data,
                        password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('customer/register.html', form=form)


@customer_blueprint.route('/logout')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))