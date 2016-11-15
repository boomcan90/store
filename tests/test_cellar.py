# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/

TESTS MUST START WITH "test"
"""
from flask import url_for

class TestRobTheCellar:
    """
    Robbing the cellar
    """

    def test_cellar_is_not_not_found(self, testapp):
        """
        There actually is a cellar... Amazing.
        """

        # !!! URL needs the / at the end.
        res = testapp.get('/cellar/')
        assert res.status_code != 404

    def test_cellar_is_accessible(self, testapp):
        """
        Breaching the cellar?! Success!
        """

        # testapp made available from the tests module
        res = testapp.get('/cellar/')
        assert res.status_code == 200

    def test_cellar_has_list_of_beer(self, testapp):
        """
        Range of beer is available!
        """
        res = testapp.get('/cellar/beer')

        # i have discovered that "string" in res is case sensitive
        # in general to know more see:
        # http://webtest.readthedocs.io/en/latest/api.html#webtest-response-testresponse
        assert "List of beer" in res


