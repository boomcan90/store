"""Forms for feedback module."""
from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, HiddenField  # noqa
from wtforms.validators import DataRequired, NumberRange

from .models import Feedback


class FeedbackForm(Form):
    """Feedback form."""

    short_text = StringField('short_text')
    score = IntegerField('score', validators=[
                         DataRequired(), NumberRange(min=1, max=10)])
    submit = HiddenField()

    def __init__(self, *args, **kwargs):
        """Init."""
        super(FeedbackForm, self).__init__(*args, **kwargs)

    def set_user_isbn(self, user, isbn):
        """Set some info."""
        self.current_user_id = user
        self.isbn13 = isbn

    def validate(self):
        """Validate search form."""
        initial_validation = super(FeedbackForm, self).validate()
        if not initial_validation:
            return False
        fb = Feedback.query.filter_by(
            user_id=self.current_user_id, book_id=self.isbn13).first()
        if fb:
            self.submit.errors.append('You already submitted feedback for this book.')
            return False
        return True
