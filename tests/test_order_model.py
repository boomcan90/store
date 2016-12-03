# -*- coding: utf-8 -*-
"""Cellar Model unit tests."""

import pytest

from store.orders.models import Order

from store.customer.models import Customer

# from .factories import OrderFactory


@pytest.mark.usefixtures('db')
class TestOrder:
    """Order tests."""

    def test_save_an_order(self):
        """Save an Order."""
        customer = Customer('foo', 'foo@bar.com', "3241234",
                            "12341234", "coolstreet")
        customer.save()

        order1 = Order('order1', customer.id)
        order1.save()

        # this method is inherited from a class in database.py
        retrieved = Order.get_by_id('order1')
        assert retrieved.order_id == 'order1'

    def test_retreive_list_of_order(self):
        """Retrieve a list of orders."""
        # http://factoryboy.readthedocs.io/en/latest/examples.html?highlight=create_batch#factories
        customer1 = Customer('foo1', 'foo1@bar.com', "3241234",
                             "12341234", "coolstreet")
        customer1.save()

        order1 = Order('order1', customer1.id)
        order1.save()

        customer2 = Customer('foo2', 'foo2@bar.com', "3241234",
                             "12341234", "coolstreet")
        customer2.save()

        order2 = Order('order2', customer2.id)
        order2.save()

        l = Order.query.all()
        assert len(l) == 2

    def test_check_if_customer_is_customer_in_order(self):
        """Test if customer is in customer order."""
        # id, email, m_credit_no, phone_no, address, password=None
        customer = Customer('foo', 'foo@bar.com', "3241234", "12341234", "coolstreet")
        customer.save()

        order = Order('order0', customer.id)
        order.save()

        retrieved = Order.get_by_id('order0')

        assert customer.id == retrieved.customer_id
        # assert customer.user_type == 'customer'
