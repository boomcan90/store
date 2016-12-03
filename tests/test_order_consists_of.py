# # -*- coding: utf-8 -*-
# """Functional tests using WebTest.
# See: http://webtest.readthedocs.org/
# TESTS MUST START WITH "test"
# """
# from flask import url_for

# class TestBreakTheOrder:
#     """
#     Breaking the order
#     """

#     def test_order_conists_of_is_not_not_found(self, testapp):

#         # !!! URL needs the / at the end.
#         res = testapp.get('/consistsof/')
#         assert res.status_code != 404

#     def test_OrderConsistsOf_is_accessible(self, testapp):
#         # testapp made available from the tests module
#         res = testapp.get('/consistsof/')
#         assert res.status_code == 200

#     def test_OrderConsistsOf_has_list_of_not_stuff(self, testapp):
#         res = testapp.get('/consistsof/consistsof')

#         # i have discovered that "string" in res is case sensitive
#         # in general to know more see:
#         # http://webtest.readthedocs.io/en/latest/api.html#webtest-response-testresponse
#         assert "List of NOT beer NOR ORDERS OR BOOKS" in res

#     def test_browse_consists_of_returns_empty_list(self, order, testapp):
#         res = testapp.get('/consistsof/ordersList')

#         assert "data" in res
