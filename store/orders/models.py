"""User models."""
import datetime as dt
from store.compat import basestring
from store.database import Column, Model, db
from store.book.models import Book
from store.customer.models import Customer


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
# qty is total number of books in 1 order by 1 customer
# Shopping cart part


class Order(Model):
    """Order model."""

    __tablename__ = 'orders'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    customer_id = Column(db.String(80), db.ForeignKey('user.id'))
    customer = db.relationship(Customer, backref="orders")

    main_order = db.relationship("OrderConsistsOf", back_populates="order")


    # customer_id = Column(db.String(80), unique=True, nullable=False)
    date = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    qty = Column(db.Integer, default=1)
    status = Column(db.Boolean(), default=True)

    def __init__(self, customer_id, **kwargs):
        """Create instance."""
        db.Model.__init__(self, customer_id=customer_id, **kwargs)

    @property
    def details(self):
        """Order and customer details."""
        return '{0} {1}'.format(self.id, self.customer_id)

    @classmethod
    def get_by_id(cls, id):
        """Get order by ID."""
        if any(
                (isinstance(id, basestring),
                 isinstance(id, str)),
        ):
            return cls.query.get(str(id))
        return None

    # def get_customer_history(cls, customer_id):
    #     if any(
    #             (isinstance(customer_id, basestring),
    #              isinstance(customer_id, str)),
    #     ):
    #         return cls.query.get(str(customer_id))
    #     return None

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Order({id!r})>'.format(id=self.id)

    def to_json(self):
        """More json."""
        return dict(id=self.id, customer=self.customer_id, status=self.status)

# -------------------------------------------------------------------------------------


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
# qty is number of copies of 1 book for that order id
# order_qty = sum(OrderConsistsOf_qty for every isbn13 in 1 order_id)


class OrderConsistsOf(Model):
    """Books one order consists of."""

    __tablename__ = 'consists_of'

    # use ForeignKey here
    consists_order_id = Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    consists_isbn13 = Column(db.String(13), db.ForeignKey('book.isbn13'), primary_key=True)
    # Non foreign key
    consists_qty = Column(db.Integer, default=1)

    book = db.relationship("Book", back_populates="book_in_order")
    order = db.relationship("Order", back_populates="main_order")

    def __init__(self, consists_order_id, consists_isbn13, consists_qty, **kwargs):
        """Create instance."""
        db.Model.__init__(self, consists_order_id=consists_order_id,
                          consists_isbn13=consists_isbn13, consists_qty=consists_qty, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<OrderConsistsOf({order_id})>'.format(order_id=self.consists_order_id)

    @classmethod
    def get_by_id(cls, tuplething):
        """Get order by ID."""
        if any(
                (isinstance(tuplething[0], basestring) and isinstance(tuplething[1], basestring),
                 isinstance(tuplething[0], str) and isinstance(tuplething[1], str)),
        ):
            return cls.query.get(tuplething)
        
        return None

    def to_json(self):
        """JSON."""
        return dict(id=self.consists_order_id, isbn13=self.consists_isbn13, quantity=self.consists_qty)


