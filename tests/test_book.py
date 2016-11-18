# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/

TESTS MUST START WITH "test"
"""
from flask import url_for

class TestBook:

    def test_book_is_not_not_found(self, testapp):

        # !!! URL needs the / at the end.
        res = testapp.get('/book/')
        assert res.status_code != 404

    def test_book_is_accessible(self, testapp):

        # testapp made available from the tests module
        res = testapp.get('/book/')
        assert res.status_code == 200

    def test_book_has_book(self, testapp):
        res = testapp.get('/book/book')

        # i have discovered that "string" in res is case sensitive
        # in general to know more see:        # http://webtest.readthedocs.io/en/latest/api.html#webtest-response-testresponse

        # http://webtest.readthedocs.io/en/latest/api.html#webtest-response-testresponse
        assert "Book details" in res

    def test_browse_list_returns_empty_list(self, testapp):
        res = testapp.get('/book/books')

        assert "List of books and details" in res

