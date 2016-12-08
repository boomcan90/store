# -*- coding: utf-8 -*-
"""Test book forms."""

from store.book.forms import AddBookForm, SearchBookForm, UpdateBookForm
from store.book.models import Book


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


class TestSearchForm:
    """Search book form."""

    def test_search_form_valid(self, book):
        """Search Form should be valid."""
        # form = SearchBookForm(author="J. K. Rowling",
        #                       option1="and",
        #                       publisher="Scholastic",
        #                       option2="and",
        #                       title="Harry Potter",
        #                       option3="and",
        #                       subject="fantasy")
        form = SearchBookForm(author="J. K. Rowling",
                              publisher="Scholastic",
                              title="Harry Potter",
                              subject="fantasy")
        assert form.validate() is True

    # def test_search_form_invalid(self, book):
    #     """Search Form should be invalid.

    #     Author length is <4.
    #     """
    #     form = SearchBookForm(author="J",
    #                           publisher="Scholastic",
    #                           title="Harry Potter",
    #                           subject="fantasy")

    #     assert form.validate() is False


class TestUpdateBookForm:
    """Search book form."""

    def test_search_form_valid(self, book):
        """Update Form should be valid."""
        b = Book(isbn13='9780439136358', title="Harry Potter And The Prisoner Of Azkaban",
                 author="J. K. Rowling", publisher="Scholastic", year_of_pub=1999, num_of_copies=11,
                 price=15.24, format="hardcover", keywords="fantasy", subject="fantasy")
        b.save()

        form = UpdateBookForm(isbn13='9780439136358', title="Harry Potter And The Prisoner Of Azkaban",
                              author="J. K. Rowling", publisher="Scholastic", year_of_pub=1999, num_of_copies=11,
                              price=15.24, format="hardcover", keywords="fantasy", subject="fantasy")

        assert form.validate() is True

    def test_search_form_invalid(self, book):
        """Update Form should be invalid.

        invalid isbn
        """
        form = UpdateBookForm(isbn13='9780439139999', title="Harry Potter And The Prisoner Of Azkaban",
                              author="J. K. Rowling", publisher="Scholastic", year_of_pub=1999, num_of_copies=11,
                              price=15.24, format="hardcover", keywords="fantasy", subject="fantasy")

        assert form.validate() is False
