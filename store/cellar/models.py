# -*- coding: utf-8 -*-
"""Cellar models."""

from store.database import Column, Model, SurrogatePK, db

class Alcohol(SurrogatePK, Model):
    """Alcohol. Enough said."""

    __tablename__ = 'alcohol'
    name = Column(db.String(80), unique=True, nullable=False)
    alcohol_type = Column(db.String(80), unique=False, nullable=False)
    quantity = Column(db.Integer, nullable=False, default=0)

    def __init__(self, name, alcohol_type, quantity, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, alcohol_type=alcohol_type, quantity=quantity, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Alcohol({name})>'.format(name=self.name)

    def to_json(self):
        return dict(id=self.id, name=self.name,
                alcohol_type=self.alcohol_type, quantity = self.quantity)
