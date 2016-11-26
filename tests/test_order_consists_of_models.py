# -*- coding: utf-8 -*-
"""Order Model unit tests."""
import datetime as dt

import pytest

from store.orders.models import Order, Order_Consists_Of
from store.book.models import Book

from .factories import OrderFactory, BookFactory, ConsistsOfFactory

@pytest.mark.usefixtures('db')
class TestOrder:
    """Order Consists Of tests"""

    def test_get_by_id(self):
        """Get Order by ID."""
        order1 = Order_Consists_Of('order1', 'CUSTOMERID', 42)
        order1.save()

        # this method is inherited from a class in database.py
        retrieved = Order_Consists_Of.get_by_id(('order1', 'CUSTOMERID'))
        assert (retrieved.consists_order_id, retrieved.consists_isbn13) == ('order1', 'CUSTOMERID')


    def test_retreive_list_of_random_order(self):
        """Retrieve a list of orders."""

        order_consists_of_list = []

        # http://factoryboy.readthedocs.io/en/latest/examples.html?highlight=create_batch#factories
        order_consists_of_list.extend(ConsistsOfFactory.create_batch(5))

        for consistsof in order_consists_of_list:
            consistsof.save()

        l = Order_Consists_Of.query.all()
        assert len(l) == 5

    def test_retreive_list_of_specific_order_and_book(self):
        """Retrieve a list of orders consisting of books"""
        book0 = Book("book0", "Lalala", "Alvin Tan","Penguin Books", 2016 ,50 ,25 ,"Text-only","la","Fiction")
        book1 = Book("book1", "Lololo", "Kelvin Tan","Aweseom Books", 2009 ,500 ,50 ,"Text-Picture","lo","Non-Fiction")
        book_list = [book0, book1]

        order0 = Order("orderid0", "customer0")
        order1 = Order("orderid1", "customer1")
        order_list = [order0, order1]

        consistsof_list = [0]*2

        for i in range(2):
            book_list[i].save()
            order_list[i].save()
            # creating consists of
            consistsof_list[i] = Order_Consists_Of(order_list[i].order_id, book_list[i].isbn13, 42)
            consistsof_list[i].save()

        # asserting the consistof attributes
        for j in range(2):
            retrieved = Order_Consists_Of.get_by_id((order_list[i].order_id, book_list[i].isbn13))
            assert (retrieved.consists_order_id, retrieved.consists_isbn13) == (consistsof_list[i].consists_order_id, consistsof_list[i].consists_isbn13)