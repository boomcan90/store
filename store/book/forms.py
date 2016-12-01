# -*- coding: utf-8 -*-
"""Book forms."""
from flask_wtf import Form
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired, EqualTo, Length

from store.book.models import Book

class AddBookForm(Form):
    """Add Book Form"""

    isbn13 = StringField('isbn13',validators=[DataRequired(), Length(min=1, max=13)])
    title =  StringField('title',validators=[DataRequired(), Length(min=3, max=128)])
    author = StringField('author',validators=[DataRequired(), Length(min=3, max=128)])
    publisher = StringField('publisher',validators=[DataRequired(), Length(min=3, max=128)])
    year_of_pub = IntegerField('year_of_pub',validators=[DataRequired()])
    num_of_copies = IntegerField('num_of_copies',validators=[DataRequired()])
    price = IntegerField('price',validators=[DataRequired()])
    format = StringField('format',validators=[DataRequired(), Length(min=3, max=128)])
    keywords = StringField('keywords',validators=[DataRequired(), Length(min=3, max=128)])
    subject = StringField('subject',validators=[DataRequired(), Length(min=3, max=128)])

    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        self.book = None

    def validate(self):
        """validate add book form"""
        initial_validation = super(AddBookForm, self).validate()
        if not initial_validation:
            return False
        book = Book.query.filter_by(isbn13=self.isbn13.data).first()
        if book:
            self.isbn13.errors.append('Book ID already exists')
            return False
        return True

# class DeleteBookForm(Form):

