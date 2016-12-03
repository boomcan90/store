"""Feedback unit tests."""
import pytest
from store.feedback.models import Feedback
from store.customer.models import Customer
from store.book.models import Book


@pytest.mark.usefixtures('db')
class FeedbackTest:
    """Feeback tests."""

    def test_create_feedback_for_a_book(self):
        """Able to create feedback."""
        c1 = Customer('cid1', 'cid1@email.com', '1234531',
                      '987654321', '1, coolstreet', 'abcd', active=True)

        b1 = Book('9780439708180', "Harry Potter and the Philosopher's Stone",
                  "J. K. Rowling", "Scholastic", 1999, 10, 6.79, "paperback", "fantasy", "fantasy")

        c1.save()
        b1.save()

        fb = Feedback(c1.id, b1.isbn13, 3, short_text="hello")

        fb.save()

        q = Feedback.query.filter_by(score=3).first()

        assert len(q) == 1
