# -*- coding: utf-8 -*-
"""User models."""

import datetime as dt

from flask_login import UserMixin

from store.compat import basestring
from store.database import Column, Model, db
from store.extensions import bcrypt


class User(UserMixin, Model):
    """A user of the app."""

    __tablename__ = 'user'
    id = Column(db.String(80), primary_key=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.Binary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False,
                        default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)
    user_type = Column('type', db.String(50))
    __mapper_args__ = {
        'polymorphic_on': 'user_type',
        'polymorphic_identity': 'manager'}

    def __init__(self, id, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, id=id, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    @classmethod
    def get_by_id(cls, record_id):
        """Get record by ID."""
        if any(
                (isinstance(record_id, basestring),
                 isinstance(record_id, str)),
        ):
            return cls.query.get(str(record_id))
        return None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({id!r})>'.format(id=self.id)
