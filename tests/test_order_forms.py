# -*- coding: utf-8 -*-
"""Test Order forms."""

# from store.orders.forms import AddOrderForm
# from store.orders.models import Order, OrderConsistsOf

# class TestAddOrderForm:
#     """Add book form."""

#     def test_add_order_form_is_valid(self, order, consistsof):
#         """Enter orderid that is not already registered."""
#         form = AddOrderForm(order_id='order1', qty=11)
#         form.set_user_isbn(user="cid1", isbn='9780439139595')

#         assert form.validate() is True

#     def test_add_order_form_is_invalid(self, order, consistsof):
#         """Enter orderid that is already registered."""
#         form = AddOrderForm(order_id='order1', qty=11)
#         form.set_user_isbn(user="cid1", isbn='9780439139595')

#         assert form.validate() is False