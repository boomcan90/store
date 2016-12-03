# -*- coding: utf-8 -*-
"""Test forms."""
import pytest
from store.book.models import Book

from store.user.forms import LoginForm, RegisterForm
from store.book.forms import AddBookForm


class TestRegisterForm:
    """Register form."""

    def test_validate_user_already_registered(self, user):
        """Enter username that is already registered."""
        form = RegisterForm(username=user.id, email='foo@bar.com',
                            password='example', confirm='example')

        assert form.validate() is False
        assert 'Username already registered' in form.username.errors

    def test_validate_email_already_registered(self, user):
        """Enter email that is already registered."""
        form = RegisterForm(username='unique', email=user.email,
                            password='example', confirm='example')

        assert form.validate() is False
        assert 'Email already registered' in form.email.errors

    def test_validate_success(self, db):
        """Register with success."""
        form = RegisterForm(username='newusername', email='new@test.test',
                            password='example', confirm='example')
        assert form.validate() is True


class TestLoginForm:
    """Login form."""

    def test_validate_success(self, user):
        """Login successful."""
        user.set_password('example')
        user.save()
        form = LoginForm(username=user.id, password='example')
        assert form.validate() is True
        assert form.user == user

    def test_validate_unknown_username(self, db):
        """Unknown username."""
        form = LoginForm(username='unknown', password='example')
        assert form.validate() is False
        assert 'Unknown username' in form.username.errors
        assert form.user is None

    def test_validate_invalid_password(self, user):
        """Invalid password."""
        user.set_password('example')
        user.save()
        form = LoginForm(username=user.id, password='wrongpassword')
        assert form.validate() is False
        assert 'Invalid password' in form.password.errors

    def test_validate_inactive_user(self, user):
        """Inactive user."""
        user.active = False
        user.set_password('example')
        user.save()
        # Correct username and password, but user is not activated
        form = LoginForm(username=user.id, password='example')
        assert form.validate() is False
        assert 'User not activated' in form.username.errors


@pytest.mark.usefixtures('db')
class TestBookForm:
    """Book Form."""

    # test creating book
    # def test_creating_book_that_already_exists(self, book):
    #     """Enter Book that is already in database."""
    #     form = AddBookForm(isbn13 = "isbn1", title=book.title, author = "example", publisher = "example",
    #         year_of_pub = "1991", num_of_copies = 50, price = 25, format ="Text-only",
    #         keyword = "la", subject = "Fiction")

    #     assert form.validate() is False
    #     assert "Book title already exists" in form.title.errors

    def test_validate_isbn13_already_registered(self, book):
        """Enter ISBN13 that is already registered."""
        # creating a entry to database
        book1 = Book('book1', "Lalala", "Alvin Tan", "Penguin Books",
                     2016, 50, 25, "Text-only", "la", "Fiction")
        book1.save()

        # user entry
        form = AddBookForm(isbn13=book1.isbn13, title="Lololo", author="example", publisher="example",
                           year_of_pub="1991", num_of_copies=50, price=25, format="Text-only",
                           keyword="lo", subject="Fiction")

        assert form.validate() is False
