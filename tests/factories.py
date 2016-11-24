# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from store.database import db
from store.user.models import User
from store.book.models import Book


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """User factory."""

    id = Sequence(lambda n: 'user{0}'.format(n))
    email = Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = PostGenerationMethodCall('set_password', 'example')
    active = True

    class Meta:
        """Factory configuration."""

        model = User


class BookFactory(BaseFactory):
    """Book factory."""

    isbn13= Sequence(lambda n: 'book{0}'.format(n))
    # isbn13 = "book0"
    title = "Lalala"
    author = "Alvin Tan"
    publisher = "Penguin Books"
    year_of_pub = 2016
    num_of_copies = 50
    price = 25
    format = "Text-only"
    keyword = "la"
    subject = "Fiction"

    class Meta:
        """Factory configuration."""

        model = Book

