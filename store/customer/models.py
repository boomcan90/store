

from store.database import Column, db
from store.user.models import User


class Customer(User):
    """Customer class inherit from User table."""

    __mapper_args__ = {'polymorphic_identity': 'customer'}

    id = Column(db.String, db.ForeignKey('user.id'), primary_key=True)
    m_credit_no = Column(db.String(64), nullable=True)
    phone_no = Column(db.String(15), nullable=True)
    address = Column(db.String(255), nullable=True)

    def __init__(self, id, email, m_credit_no, phone_no, address, password=None, **kwargs):
        """init."""
        super(Customer, self).__init__(id, email, password, **kwargs)
        self.m_credit_no = m_credit_no
        self.phone_no = phone_no
        self.address = address

    def address(self):
        """address."""
        return '{0}'.format(self.address)

    def __repr__(self):
        """Represent instance as an unique string."""
        return '<Customer({id!r})>'.format(id=self.id)
