# # -*- coding: utf-8 -*-
# """Feedback Model unit tests."""
# import datetime as dt

# import pytest

# from store.feedback.models import Feedback


# @pytest.mark.usefixtures('db')
# class TestFeedback:
#     """Test feedback."""

#     def test_create_feedback(self):
#         """Can create feedback."""
#         book0 = Book("book0", "Lalala", "Alvin Tan", "Penguin Books",
#                      2016, 50, 25, "Text-only", "la", "Fiction")
#         book0.save()

#         customer = Customer('foo', 'foo@bar.com', "3241234", "12341234", "coolstreet")

#         customer.save()

