# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest

from store.app import create_app
from store.database import db as _db
from store.settings import TestConfig
from webtest import TestApp

from .factories import CustomerFactory, UserFactory, OrderFactory
from .factories ConsistsOfFactory, BookFactory



@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)


@pytest.yield_fixture(scope='function')
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


@pytest.fixture
def user(db):
    """A user for the tests."""
    user = UserFactory(password='myprecious')
    db.session.commit()
    return user

@pytest.fixture
def customer(db):
    """cutomer for testing"""
    customer = CustomerFactory(password='myprecious')
    db.session.commit()
    return customer

@pytest.fixture
def order(db):
    """ Some orders for the tests."""
    order = OrderFactory()
    db.session.commit()
    return order

@pytest.fixture
def consistsof(db):
    """ Some orders_consistsof for the tests."""
    consistsof = ConsistsOfFactory()
    db.session.commit()
    return order

