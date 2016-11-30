# -*- coding: utf-8 -*-
"""Customer forms."""

from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .models import Customer


class RegisterForm(Form):
    """Register form."""

    customername = StringField('Username',
                               validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6, max=40)])
    m_credit_no = StringField('Credit Card no',
                              validators=[DataRequired(), Length(max=16)])

    phone_no = StringField('Phone no',
                           validators=[DataRequired(), Length(max=8)])
    address = StringField('Address',
                          validators=[DataRequired(), Length(min=10, max=255)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Verify password',
                            [DataRequired(), EqualTo('password', message='Passwords must match')])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.customer = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        customer = Customer.query.filter_by(id=self.customername.data).first()
        if customer:
            self.customername.errors.append('Username already registered')
            return False
        customer = Customer.query.filter_by(email=self.email.data).first()
        if customer:
            self.email.errors.append('Email already registered')
            return False
        return True


class LoginFormCustomer(Form):
    """Login form."""

    customername = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginFormCustomer, self).__init__(*args, **kwargs)
        self.customer = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(LoginFormCustomer, self).validate()
        if not initial_validation:
            return False

        self.customer = Customer.query.filter_by(
            id=self.customername.data).first()
        if not self.customer:
            self.customername.errors.append('Unknown username')
            return False

        if not self.customer.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        if not self.customer.active:
            self.customername.errors.append('User not activated')
            return False
        return True
