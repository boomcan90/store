
# import datetime as dt

import pytest

from store.customer.models import Customer

from .factories import CustomerFactory


@pytest.mark.usefixtures('db')
class TestCustomer:
    """Some customer tests"""

    def test_get_list_of_id(self):
        id_bucket = []

        id_bucket.extend(CustomerFactory.create_batch(5))

        for i in id_bucket:
            i.save()

        l = Customer.query.all()
        assert len(l) == 5

    def test_is_a_customer_for_real(self):

        # id, email, m_credit_no, phone_no, address, password=None
        customer = Customer('foo', 'foo@bar.com', "3241234", "12341234", "coolstreet")

        customer.save()

        retrieved = Customer.get_by_id(customer.id)

        assert customer == retrieved
        assert customer.user_type == 'customer'
