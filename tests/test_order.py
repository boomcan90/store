# -*- coding: utf-8 -*-
"""Functional tests using WebTest.
See: http://webtest.readthedocs.org/
TESTS MUST START WITH "test"
"""
from flask import url_for

class TestBreakTheOrder:
    """
    Breaking the order
    """

    def test_order_is_not_not_found(self, testapp):
        """
        There actually is an order... Amazing. 
        I know, right?
        """

        # !!! URL needs the / at the end.
        res = testapp.get('/orders/')
        assert res.status_code != 404

    def test_order_is_accessible(self, testapp):
        """
        Breaching the order?! Success!
        """

        # testapp made available from the tests module
        res = testapp.get('/orders/')
        assert res.status_code == 200

    def test_order_has_list_of_not_beer(self, testapp):
        """
        Range of beer is NOT available!
        Do I look like Robin?
        """
        res = testapp.get('/orders/orders')

        # i have discovered that "string" in res is case sensitive
        # in general to know more see:
        # http://webtest.readthedocs.io/en/latest/api.html#webtest-response-testresponse
        assert "List of NOT beer" in res

    def test_browse_list_returns_empty_list(self, order, testapp):
        """
        Range of order available?
        """
        res = testapp.get('/orders/ordersList')

        assert "data" in res
