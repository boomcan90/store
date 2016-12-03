# -*- coding: utf-8 -*-
"""Book models."""

from store.database import Column, Model, db
from store.compat import basestring


class Book(Model):
    """Book."""

    __tablename__ = 'book'
    isbn13 = Column(db.String(13), nullable=False, primary_key=True)
    title = Column(db.String(128), nullable=False)
    author = Column(db.String(128), nullable=False)
    publisher = Column(db.String(128), nullable=False)
    year_of_pub = Column(db.Integer, nullable=False)
    num_of_copies = Column(db.Integer, nullable=False)
    price = Column(db.Integer, nullable=False)
    format = Column(db.String(9), nullable=False)
    keywords = Column(db.String(128), nullable=False)
    subject = Column(db.String(128), nullable=False)

    users = db.relationship("Feedback", back_populates="book")

    def __init__(self, isbn13, title, author, publisher, year_of_pub,
                 num_of_copies, price, format, keywords, subject):
        """Init."""
        db.Model.__init__(self, isbn13=isbn13, title=title, author=author,
                          publisher=publisher, year_of_pub=year_of_pub,
                          num_of_copies=num_of_copies, price=price, format=format,
                          keywords=keywords, subject=subject)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<isbn13({isbn13})>'.format(isbn13=self.isbn13)

    def to_json(self):
        """To json."""
        return dict(isbn13=self.isbn13, title=self.title,
                    author=self.author, publisher=self.publisher,
                    year_of_pub=self.year_of_pub, num_of_copies=self.num_of_copies,
                    price=self.price, format=self.format, keywords=self.keywords,
                    subject=self.subject)

    @classmethod
    def get_by_id(cls, isbn13):
        """Get by id."""
        if any(
                (isinstance(isbn13, basestring), isinstance(isbn13, str)),
        ):
            return cls.query.get(str(isbn13))
        return None

    @property
    def book_title(self):
        """Book title."""
        return '{0} {1}'.format(self.title)
