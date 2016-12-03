"""Feedback models."""

from store.database import db


class Feedback(db.Model):
    """Feedback relationship table."""

    __tablename__ = 'feedback'
    user_id = db.Column(db.String, db.ForeignKey("user.id"), primary_key=True)
    book_id = db.Column(db.String, db.ForeignKey(
        "book.isbn13"), primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    short_text = db.Column(db.String, nullable=True, default="")

    user = db.relationship("User", back_populates="reviews")  # child
    book = db.relationship("Book", back_populates="users")  # parent

    def __init__(self, user_id, isbn, score, **kwargs):
        """Create instance."""
        db.Model.__init__(self, user_id=user_id,
                          book_id=isbn, score=score, **kwargs)

    def __repr__(self):
        """Represent instance as an unique string."""
        return '<Feedback({!r}{!r})>score={},text={}'.format(self.user_id, self.book_id, self.score, self.short_text)


# class Rates(db.Model):
#     """Rate relationship table."""

#     __tablename__ = 'rates'

#     feedback_id = db.Column(db.Integer, db.ForeignKey(
#         'feedback.id'), primary_key=True),
#     rater_id = db.Column(db.Integer, db.ForeignKey(
#         'user.id'), primary_key=True),
#     rated_id = db.Column(db.Integer, db.ForeignKey('user.id')),
#     rating = db.Column(db.Integer, nullable=False),

#     raters = db.relationship("User", backref="rates",
#                                cascade="all, delete-orphan")
#     rated_ = db.relationship("User", backref="rates")
