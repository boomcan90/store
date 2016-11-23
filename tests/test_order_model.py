
# -*- coding: utf-8 -*-
"""Cellar Model unit tests."""
import datetime as dt

import pytest

from store.orders.models import Order

from .factories import OrderFactory

@pytest.mark.usefixtures('db')
class TestOrder:
    """Order tests"""

    def test_get_by_id(self):
        """Get Order by ID."""
        order1 = Order('order1', 'CUSTOMERID', DATE, 42. False)
        order1.save()

        # this method is inherited from a class in database.py
        retrieved = Order.get_by_id(order1.id)
        assert retrieved == order1


    def test_retreive_list_of_beer(self):
        """Retrieve a list of orders."""

        order_list = []

        # http://factoryboy.readthedocs.io/en/latest/examples.html?highlight=create_batch#factories
        order_list.extend(OrderFactory.create_batch(5))

        for order in order_list:
            order.save()

        l = Order.query.all()
        assert len(l) == 5