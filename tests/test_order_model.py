# -*- coding: utf-8 -*-
"""Cellar Model unit tests."""

import datetime as dt

import pytest

from store.orders.models import Order

from store.customer.models import Customer

from .factories import OrderFactory

@pytest.mark.usefixtures('db')
class TestOrder:
    """Order tests"""
    def test_retreive_list_of_beer(self):
        order1 = Order('order1', 'CUSTOMERID')
        order1.save()

        # this method is inherited from a class in database.py
        retrieved = Order.get_by_id('order1')
        assert retrieved.order_id == 'order1'


    def test_retreive_list_of_order(self):
        """Retrieve a list of orders."""

        order_list = []

        # http://factoryboy.readthedocs.io/en/latest/examples.html?highlight=create_batch#factories
        order_list.extend(OrderFactory.create_batch(5))

        for order in order_list:
            order.save()

        l = Order.query.all()
        assert len(l) == 5

    def test_check_if_customer_is_customer_in_order(self):
        # id, email, m_credit_no, phone_no, address, password=None
        customer = Customer('foo', 'foo@bar.com', "3241234", "12341234", "coolstreet")
        customer.save()

        order = Order('order0', customer.id)
        order.save()

        retrieved = Order.get_by_id('order0')

        assert customer.id == retrieved.customer_id
        # assert customer.user_type == 'customer'