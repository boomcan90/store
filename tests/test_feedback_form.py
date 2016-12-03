# -*- coding: utf-8 -*-
"""Test feedback forms."""

from store.feedback.forms import FeedbackForm


class TestFeedbackForm:
    """Create feedback form."""

    def test_search_form_valid(self, book):
        """Feedback Form should be valid."""
        form = FeedbackForm(short_text="Very good.",
                            score=10)

        assert form.validate() is True

    def test_search_form_invalid(self, book):
        """Feedback Form should be invalid."""
        form = FeedbackForm(short_text="Not so good.")

        assert form.validate() is False

    def test_invalid_score_too_big(self, book):
        """Feedback Form should be invalid."""
        form = FeedbackForm(short_text="Too good.",
                            score=999)

        assert form.validate() is False
