# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/

TESTS MUST START WITH "test"
"""
import pytest

from store.dummy_data import books as testdata


@pytest.mark.usefixtures('db')
class TestBook:
    """Tests for book."""

    def test_book_is_not_not_found(self, testapp):
        """Book page 404."""
        res = testapp.get('/book/details', expect_errors=True)
        assert res.status_code == 404

    def test_book_is_accessible(self, testapp):
        """Book page 200."""
        res = testapp.get('/book/book')
        assert res.status_code == 200

    def test_book_has_book(self, testapp):
        """There is a book on book page."""
        book = testdata.sample_list[0]
        book.save()

        res = testapp.get('/book/book')

        # i have discovered that "string" in res is case sensitive
        # in general to know more see:
        # http://webtest.readthedocs.io/en/latest/api.html#webtest-response-testresponse
        assert "9780439708180" in res

    def test_book_has_some_books(self, testapp):
        """There are some books."""
        for book in testdata.sample_list:
            book.save()

        res = testapp.get('/book/browse')

        assert "9780439064873" in res


class TestAddBook:
    """Test adding book."""

    def test_cannot_add_book_if_empty_fields(self, testapp):
        """Cannot add a book if fields are empty."""
        res = testapp.get('/book/add')
        form = res.forms['addBookForm']
        res = form.submit()
        assert "required" in res
