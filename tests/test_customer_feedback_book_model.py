# -*- coding: utf-8 -*-
"""Feedback Model unit tests."""
import pytest

from store.customer.models import Customer
from store.book.models import Book
from store.feedback.models import Feedback


@pytest.mark.usefixtures('db')
class TestFeedback:
    """Test feedback."""

    def test_create_feedback(self):
        """Can create feedback."""
        book0 = Book("book0", "Lalala", "Alvin Tan", "Penguin Books",
                     2016, 50, 25, "Text-only", "la", "Fiction")
        book0.save()

        customer = Customer('foo', 'foo@bar.com', "3241234", "12341234", "coolstreet")

        customer.save()

        fb1 = Feedback(customer.id, book0.isbn13, score=5, short_text="very nice book.")

        customer.reviews.append(fb1)

        customer.save()

        q = Customer.query.filter_by(id=customer.id).first()
        # print(q.reviews)
        assert q is not None
        assert len(q.reviews) > 0
