"""Feedback models."""

from store.database import db


class Feedback(db.Model):
    """Feedback relationship table."""

    __tablename__ = 'feedback'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(80), db.ForeignKey("user.id"), primary_key=True)
    book_id = db.Column(db.String(13), db.ForeignKey(
        "book.isbn13"), primary_key=True)
    score = db.Column(db.Integer, nullable=False)  # 0 to 10.
    short_text = db.Column(db.String(255), nullable=True, default="")

    #  TODO: add date

    user = db.relationship("User", back_populates="reviews")
    book = db.relationship("Book", back_populates="reviewers")

    def __init__(self, user_id, isbn, score, **kwargs):
        """Create instance."""
        db.Model.__init__(self, user_id=user_id,
                          book_id=isbn, score=score, **kwargs)

    def __repr__(self):
        """Represent instance as an unique string."""
        return '<Feedback({!r}{!r})>score={},text={}'.format(self.user_id, self.book_id, self.score, self.short_text)


class Rates(db.Model):
    """Rate relationship table."""

    __tablename__ = 'rates'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    feedback_id = db.Column(db.Integer, db.ForeignKey(
        'feedback.id'), primary_key=True)
    rater_id = db.Column(db.String(80), db.ForeignKey(
        'user.id'), primary_key=True)
    rated_id = db.Column(db.String(80), db.ForeignKey('user.id'))
    rating = db.Column(db.Integer, nullable=False)

    # raters = db.relationship("User", backref="rates",
    #                            cascade="all, delete-orphan")
    # rated_ = db.relationship("User", backref="rates")
