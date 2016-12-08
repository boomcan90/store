"""Form for orders module """
from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

from .models import Order, OrderConsistsOf

class AddOrderForm(Form):
    """Add Order Form."""

    order_id = StringField('order_id', validators=[
                        DataRequired(), Length(min=3, max=80)])

    qty = IntegerField('qty_of_book', validators=[
                         DataRequired(), Length(min=1, max=15)])

    def __init__(self, *args, **kwargs):
        """Init."""
        super(AddOrderForm, self).__init__(*args, **kwargs)

    def set_user_isbn(self, user, isbn):
        self.current_user_id = user
        self.isbn13 = isbn

    def validate(self):
        """Validate add order form."""
        initial_validation = super(AddOrderForm, self).validate()
        if not initial_validation:
            return False
        order = Order.query.filter_by(order_id=self.order_id.data, customer_id=self.current_user_id).first()
        consistsof = OrderConsistsOf.query.get((self.order_id.data, self.isbn13))
        if order:
            self.order_id.errors.append('Order_id already exists')
            return False
        elif consistsof:
            self.order_id.errors.append('Order_id, isbn13 relationship already exists')
            return False
        return True
