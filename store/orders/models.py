# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from store.database import Column, Model, SurrogatePK, db, reference_col, relationship

"""
CREATE TABLE Consists_of (
    order_id VARCHAR(20),
    isbn VARCHAR(13),
    qty INTEGER(100),
    FOREIGN KEY order_id REFERENCES Order(order_id),
    FOREIGN KEY isbn REFERENCES Book(isbn),
    PRIMARY KEY(order_id, isbn)
);
"""
class Order_Consists_Of(SurrogatePK, Model):
    """books one order consists of."""

    __tablename__ = 'consists_of'
    order_id = Column(db.String(80), unique=True, nullable=False)
    isbn = reference_col('customers', nullable=False)
    qty = Column(db.Integer, default=1)

    # what is this for? user = relationship('User', backref='roles')

    def __init__(self, order_id, isbn, **kwargs):
        """Create instance."""
        db.Model.__init__(self, order_id=order_id, isbn=isbn, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Order_Consists_Of({order_id})>'.format(order_id=self.order_id)



"""
CREATE TABLE Order_places_order (
    order_id VARCHAR(20),
    customer_id VARCHAR(20)  NOT NULL,
    date DATE,
    qty INTEGER,
    status VARCHAR(20),
    FOREIGN KEY customer_id REFERENCES Customer(customer_id),
    PRIMARY KEY(order_id)
);
"""
# what else goes in here?
class Order(SurrogatePK, Model):
    """Shopping cart part"""

    __tablename__ = 'orders'
    # Primary key (necessary to mention primary_key = True??)
    order_id = Column(db.String(80), unique=True, nullable=False, primary_key=True)
    # Foreign key- get name correctly later!
    # Is this how to create a foreign key? HOW TO USE reference_col??????
    customer_id = Column(db.String(80), unique=True, ForeignKey='customers', nullable=False)
    date = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    qty = Column(db.Integer, default=1)
    status = Column(db.Boolean(), default=True)

    def __init__(self, order_id, customer_id, **kwargs):
        """Create instance."""
        db.Model.__init__(self, order_id=order_id, customer_id=customer_id, **kwargs)
    @property
    def details(self):
        """order and customer details."""
        return '{0} {1}'.format(self.order_id, self.customer_id)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Order({order_id!r})>'.format(order_id=self.order_id)
