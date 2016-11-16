# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from store.database import db
from store.user.models import User

from store.cellar.models import Alcohol


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """User factory."""

    username = Sequence(lambda n: 'user{0}'.format(n))
    email = Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = PostGenerationMethodCall('set_password', 'example')
    active = True

    class Meta:
        """Factory configuration."""

        model = User


class AlcoholFactory(BaseFactory):
    """Alcohol factory. 'factory' refers to the factory-boy plugin
    http://factoryboy.readthedocs.io/en/latest/introduction.html
    """

    name = Sequence(lambda n: 'beer{0}'.format(n))
    alcohol_type = 'beer'
    quantity = 5

    class Meta:
        """Factory configuration."""

        model = Alcohol
