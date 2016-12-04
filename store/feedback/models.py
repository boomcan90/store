"""Feedback models."""

from store.database import db


class Feedback(db.Model):
    """Feedback relationship table."""

    __tablename__ = 'feedback'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(80), db.ForeignKey(
        "user.id"), primary_key=True)
    book_id = db.Column(db.String(13), db.ForeignKey(
        "book.isbn13"), primary_key=True)
    score = db.Column(db.Integer, nullable=False)  # 0 to 10.
    short_text = db.Column(db.String(255), nullable=True, default="")

    #  TODO: add date

    user = db.relationship("User", back_populates="reviews")
    book = db.relationship("Book", back_populates="reviewers")

    def __init__(self, user_id, book_id, score, **kwargs):
        """Create instance."""
        db.Model.__init__(self, user_id=user_id,
                          book_id=book_id, score=score, **kwargs)

    def __repr__(self):
        """Represent instance as an unique string."""
        return '<Feedback({!r}:{!r}{!r})>score={},text={}' \
            .format(self.id, self.user_id, self.book_id, self.score, self.short_text)

    def has_rated(self, current_user_id):
        """Check if user has rated feedback."""
        rcount = Rates.query.filter_by(rater_id=current_user_id, feedback_id=self.id).count()
        print(rcount)
        return rcount != 0


class Rates(db.Model):
    """Rate relationship table."""

    __tablename__ = 'rates'

    feedback_id = db.Column(db.Integer, db.ForeignKey(
        'feedback.id'), primary_key=True)
    rater_id = db.Column(db.String(80), db.ForeignKey(
        'user.id'), primary_key=True)
    rated_id = db.Column(db.String(80), db.ForeignKey('user.id'))
    rating = db.Column(db.Integer, nullable=False)

    feedbacks = db.relation("Feedback", backref="ratings")

    rater = db.relationship(
        "User", back_populates="ratings_given", primaryjoin="Rates.rater_id==User.id")

    def __init__(self, feedback_id, rater_id, rated_id, rating, **kwargs):
        """Create instance."""
        db.Model.__init__(self, feedback_id=feedback_id,
                          rater_id=rater_id, rated_id=rated_id, rating=rating, **kwargs)

    def __repr__(self):
        """Represent instance as an unique string."""
        return '<Rates({!r}{!r})>rated_id={},rating={}'.format(self.feedback_id,
                                                               self.rater_id, self.rated_id, self.rating)
