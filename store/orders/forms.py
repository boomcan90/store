"""Form for orders module """
from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

from .models import Order, OrderConsistsOf

class AddOrderForm(Form):
    """Add Order Form."""

    qty = IntegerField('qty_of_book', validators=[
                         DataRequired(), Length(min=1, max=15)])

    def __init__(self, *args, **kwargs):
        """Init."""
        super(AddOrderForm, self).__init__(*args, **kwargs)

    def set_user_isbn(self, user, isbn, order):
        self.order_id = order
        self.current_user_id = user
        self.isbn13 = isbn

    def validate(self):
        return True
