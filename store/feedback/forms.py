"""Forms for feedback module."""
from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class FeedbackForm(Form):
    """Feedback form."""

    short_text = StringField('short_text')
    score = IntegerField('score', validators=[DataRequired(), NumberRange(min=1, max=10)])

    def __init__(self, *args, **kwargs):
        """Init."""
        super(FeedbackForm, self).__init__(*args, **kwargs)

    def validate(self):
        """Validate search form."""
        initial_validation = super(FeedbackForm, self).validate()
        if not initial_validation:
            return False
        return True
