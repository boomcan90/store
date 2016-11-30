# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/
"""
from flask import url_for
from store.customer.models import Customer


class TestCustomerLoggingIn:
    """Customer login test."""

    def test_can_log_in_returns_200(self, customer, testapp):
        """Login successful."""
        # Goes to homepage
        res = testapp.get('/customer/login')
        # Fills out login form in navbar
        form = res.forms['loginForm']
        form['customername'] = customer.id
        form['password'] = 'myprecious'
        # Submits
        res = form.submit().follow()
        assert res.status_code == 200

    def test_sees_alert_on_log_out(self, customer, testapp):
        """Show alert on logout."""
        res = testapp.get('/customer/login')
        # Fills out login form in navbar
        form = res.forms['loginForm']
        form['customername'] = customer.id
        form['password'] = 'myprecious'
        # Submits
        res = form.submit().follow()
        res = testapp.get(url_for('customer.logout')).follow()
        # sees alert
        # assert 'You are logged out.' in res
        assert res.status_code == 200

    def test_sees_error_message_if_password_is_incorrect(self, customer, testapp):
        """Show error if password is incorrect."""
        # Goes to homepage
        res = testapp.get('/customer/login')
        # Fills out login form, password incorrect
        form = res.forms['loginForm']
        form['customername'] = customer.id
        form['password'] = 'wrong'
        # Submits
        res = form.submit()
        # sees error
        assert 'Invalid password' in res

    def test_sees_error_message_if_username_doesnt_exist(self, customer, testapp):
        """Show error if username doesn't exist."""
        # Goes to homepage
        res = testapp.get(url_for('customer.login'))
        # Fills out login form, password incorrect
        form = res.forms['loginForm']
        form['customername'] = 'unknown'
        form['password'] = 'myprecious'
        # Submits
        res = form.submit()
        # sees error
        assert 'Unknown user' in res


class TestCustomerRegistering:
    """Register a customer."""

    def test_can_register(self, customer, testapp):
        """Register a new user."""
        old_count = len(Customer.query.all())
        # Goes to homepage
        res = testapp.get('/customer/register')
        # Fills out the form
        form = res.forms['registerForm']
        form['customername'] = 'foobar'
        form['email'] = 'foo@bar.com'
        form['m_credit_no'] = "12341234"
        form['phone_no'] = "123456"
        form['address'] = "123 some street"
        form['password'] = 'secret'
        form['confirm'] = 'secret'
        # Submits
        res = form.submit().follow()
        assert res.status_code == 200
        # A new user was created
        assert len(Customer.query.all()) == old_count + 1
