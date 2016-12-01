# -*- coding: utf-8 -*-
"""Test book forms."""

from store.book.forms import AddBookForm


class TestAddBookForm:
    """Add book form."""

    def test_add_book_form_is_valid(self, book):
        """Enter username that is already registered."""
        form = AddBookForm(isbn13='9780439136358', title="Harry Potter And The Prisoner Of Azkaban",
                           author="J. K. Rowling", publisher="Scholastic", year_of_pub=1999, num_of_copies=11,
                           price=15.24, format="hardcover", keywords="fantasy", subject="fantasy")

        assert form.validate() is True

    def test_add_book_form_is_invalid(self, book):
        """Enter username that is already registered."""
        form = AddBookForm(isbn13='123', title="Harry Potter And The Prisoner Of Azkaban",
                           author="J. K. Rowling", publisher="Scholastic", year_of_pub=1999, num_of_copies=11,
                           price=15.24, format="hardcover", keywords="fantasy", subject="fantasy")

        assert form.validate() is False
