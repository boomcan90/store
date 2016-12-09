# -*- coding: utf-8 -*-
"""Order Model unit tests."""

import pytest

from store.orders.models import Order

from store.customer.models import Customer

# from .factories import OrderFactory


@pytest.mark.usefixtures('db')
class TestOrder:
    """Order tests."""

    def test_retreive_list_of_order(self):
        """Retrieve a list of orders."""
        # http://factoryboy.readthedocs.io/en/latest/examples.html?highlight=create_batch#factories
        customer1 = Customer('foo1', 'foo1@bar.com', "3241234",
                             "12341234", "coolstreet")
        customer1.save()

        order1 = Order(customer1.id)
        order1.save()

        customer2 = Customer('foo2', 'foo2@bar.com', "3241234",
                             "12341234", "coolstreet")
        customer2.save()

        order2 = Order(customer2.id)
        order2.save()

        l = Order.query.all()
        assert len(l) == 2

