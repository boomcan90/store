# -*- coding: utf-8 -*-
"""Test forms."""

from store.customer.forms import RegisterForm, LoginFormCustomer


class TestRegisterForm:
    """Register form."""

    def test_validate_user_already_registered(self, customer):
        """Enter username that is already registered. Uniqueness check."""
        form = RegisterForm(customername=customer.id, email='foo@bar.com',
                            m_credit_no='1223445', phone_no='123445', address='Somapah road 8',
                            password='example', confirm='example')

        assert form.validate() is False
        assert 'Username already registered' in form.customername.errors

    def test_validate_email_already_registered(self, customer):
        """Enter email that is already registered."""
        # form = RegisterForm(username='unique', email=user.email,
        #                     password='example', confirm='example')
        form = RegisterForm(customername='unique', email=customer.email, m_credit_no='1223445',
                            phone_no='123445', address='Somapah road 8',
                            password='example', confirm='example')
        assert form.validate() is False
        assert 'Email already registered' in form.email.errors

    def test_validate_success(self, db):
        """Register with success."""
        form = RegisterForm(username='newusername', email='new@test.test',
                            password='example', confirm='example')
        form = RegisterForm(customername='newusername', email='new@test.test',
                            m_credit_no='1223445', phone_no='123445', address='Somapah road 8',
                            password='example', confirm='example')
        assert form.validate() is True


class TestLoginForm:
    """Login form."""

    def test_validate_success(self, customer):
        """Login successful."""
        customer.set_password('example')
        customer.save()
        form = LoginFormCustomer(customername=customer.id, password='example')
        assert form.validate() is True
        assert form.customer == customer

    def test_validate_unknown_username(self, db):
        """Unknown username."""
        form = LoginFormCustomer(customername='unknown', password='example')
        assert form.validate() is False
        assert 'Unknown username' in form.customername.errors
        assert form.customer is None

    def test_validate_invalid_password(self, customer):
        """Invalid password."""
        customer.set_password('example')
        customer.save()
        form = LoginFormCustomer(
            customername=customer.id, password='wrongpassword')
        assert form.validate() is False
        assert 'Invalid password' in form.password.errors

    def test_validate_inactive_user(self, customer):
        """Inactive user."""
        customer.active = False
        customer.set_password('example')
        customer.save()
        # Correct username and password, but user is not activated
        form = LoginFormCustomer(customername=customer.id, password='example')
        assert form.validate() is False
        assert 'User not activated' in form.customername.errors
