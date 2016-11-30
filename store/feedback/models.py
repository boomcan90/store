"""Feedback models."""


from store.database import db

from store.book.models import Book

from store.customer.models import Customer


class Feedback(db.Model):
    """Feedback relationship table."""

    __tablename__ = 'customer_feedback_book'

    id = db.Column('id', db.Integer, primary_key=True),
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id')),
    isbn = db.Column(db.Integer, db.ForeignKey('book.isbn')),
    score = db.Column(db.String, nullable=False),
    short_text = db.Column(db.String, nullable=True, default="")

    customer = db.relationship(Customer, backref="feedback")
    book = db.relationship(Book, backref="feedback")


class Rates(db.Model):
    """Rate relationship table."""

    __tablename__ = 'customer_rates_feedback'

    feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'), primary_key=True),
    rater_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True),
    rated_id = db.Column(db.Integer, db.ForeignKey('customer.id')),
    rating = db.Column(db.Integer, nullable=False),

    rater_id = db.relationship(Customer, backref="rates")
    rated_id = db.relationship(Customer, backref="rates")
