# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/

TESTS MUST START WITH "test"
"""
import pytest

from flask import url_for
from store.book.models import Book
from store.dummy_data import books as testdata

@pytest.mark.usefixtures('db')
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

        book = testdata.sample_list[0]
        book.save()

        res = testapp.get('/book/book')

        # i have discovered that "string" in res is case sensitive
        # in general to know more see:        
        # http://webtest.readthedocs.io/en/latest/api.html#webtest-response-testresponse
        assert "9780439708180" in res

    def test_list_returns_empty_list(self, testapp):

        for book in testdata.sample_list:
            book.save()

        res = testapp.get('/book/books')

        assert "9780439064873" in res

        #When program encounters an assert statement, Python evaluates 
        #the accompanying expression, which is hopefully true. 
        #If the expression is false, Python raises an AssertionError 
        #exception.
