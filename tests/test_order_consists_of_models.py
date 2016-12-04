# -*- coding: utf-8 -*-
"""Order Model unit tests."""

import pytest

from store.orders.models import Order, OrderConsistsOf
from store.book.models import Book
from store.customer.models import Customer

# from .factories import ConsistsOfFactory


@pytest.mark.usefixtures('db')
class TestOrderConsistsOf:
    """Order Consists Of tests."""

    def test_create_order_consists_of_for_order_and_book(self):
        """Retrieve a list of orders consisting of books."""

        b1 = Book('9780439708180', "Harry Potter and the Philosopher's Stone",
                  "J. K. Rowling", "Scholastic", 1999, 10, 6.79, "paperback", "fantasy", "fantasy")
        b1.save()

        c1 = Customer('foo', 'foo@bar.com', "3241234", "12341234", "coolstreet")
        c1.save()

        o1 = Order('o1', c1.id)
        o1.save()

        oco = OrderConsistsOf(o1.order_id, b1.isbn13, 42)
        oco.save()

        q = OrderConsistsOf.query.filter_by(consists_qty=42).all()
        
        assert len(q) == 1


    def test_check_if_book_is_book_in_consists_of(self):

        book = Book('9780439708180', "Harry Potter and the Philosopher's Stone",
                  "J. K. Rowling", "Scholastic", 1999, 10, 6.79, "paperback", "fantasy", "fantasy")
        book.save()

        customer = Customer('foo', 'foo@bar.com', "3241234", "12341234", "coolstreet")
        customer.save()

        order = Order('o1', customer.id)
        order.save()

        oco = OrderConsistsOf(order.order_id, book.isbn13, 42)
        oco.save()

        retrieved = OrderConsistsOf.get_by_id((order.order_id, book.isbn13))

        assert (retrieved.consists_order_id, retrieved.consists_isbn13) == ('o1', '9780439708180')
