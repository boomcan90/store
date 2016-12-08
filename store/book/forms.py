# -*- coding: utf-8 -*-
"""Book forms."""
from flask_wtf import Form
from wtforms import StringField, IntegerField, RadioField, DecimalField  # noqa
from wtforms.validators import DataRequired, Length

from store.book.models import Book


class SearchBookForm(Form):
    """Search book form."""

    author = StringField('author', validators=[])
    publisher = StringField('publisher', validators=[])
    title = StringField('title', validators=[])
    subject = StringField('subject', validators=[])
    order = RadioField(
        'order',
        validators=[DataRequired()],
        choices=[('year', 'Publish Year'), ('avgfb', 'Average feedback score')], default='year'
    )

    def __init__(self, *args, **kwargs):
        """Init."""
        super(SearchBookForm, self).__init__(*args, **kwargs)

    def validate(self):
        """Validate search form."""
        initial_validation = super(SearchBookForm, self).validate()
        if not initial_validation:
            return False
        return True

# class SearchBookForm(Form):
#     """Search book form."""

#     author = StringField('author', validators=[Length(min=3)])
#     option1 = RadioField(
#         'andor1',
#         validators=[DataRequired()],
#         choices=[('and', 'AND'), ('or', 'OR')], default='and'
#     )
#     publisher = StringField('publisher', validators=[Length(min=3)])
#     option2 = RadioField(
#         'andor2',
#         validators=[DataRequired()],
#         choices=[('and', 'AND'), ('or', 'OR')], default='and'
#     )
#     title = StringField('title', validators=[Length(min=3)])
#     option3 = RadioField(
#         'andor3',
#         validators=[DataRequired()],
#         choices=[('and', 'AND'), ('or', 'OR')], default='and'
#     )
#     subject = StringField('subject', validators=[Length(min=3)])

#     def __init__(self, *args, **kwargs):
#         """Init."""
#         super(SearchBookForm, self).__init__(*args, **kwargs)

#     def validate(self):
#         """Validate search form."""
#         initial_validation = super(SearchBookForm, self).validate()
#         if not initial_validation:
#             return False
#         return True


class AddBookForm(Form):
    """Add Book Form."""

    isbn13 = StringField('isbn13', validators=[
                         DataRequired(), Length(min=13, max=13)])
    title = StringField('title', validators=[
                        DataRequired(), Length(min=3, max=128)])
    author = StringField('author', validators=[
                         DataRequired(), Length(min=3, max=128)])
    publisher = StringField('publisher', validators=[
                            DataRequired(), Length(min=3, max=128)])
    year_of_pub = IntegerField('year_of_pub', validators=[DataRequired()])
    num_of_copies = IntegerField('num_of_copies', validators=[DataRequired()])
    price = DecimalField('price', validators=[DataRequired()])
    format = StringField('format', validators=[
                         DataRequired(), Length(min=3, max=128)])
    keywords = StringField('keywords', validators=[
                           DataRequired(), Length(min=3, max=128)])
    subject = StringField('subject', validators=[
                          DataRequired(), Length(min=3, max=128)])

    def __init__(self, *args, **kwargs):
        """Init."""
        super(AddBookForm, self).__init__(*args, **kwargs)
        self.book = None

    def validate(self):
        """Validate add book form."""
        initial_validation = super(AddBookForm, self).validate()
        if not initial_validation:
            return False
        book = Book.query.filter_by(isbn13=self.isbn13.data).first()
        if book:
            self.isbn13.errors.append('Book ID already exists')
            return False
        return True


class UpdateBookForm(Form):
    """Add Book Form."""

    isbn13 = StringField('isbn13', validators=[
                         DataRequired(), Length(min=13, max=13)])
    title = StringField('title', validators=[
                        DataRequired(), Length(min=3, max=128)])
    author = StringField('author', validators=[
                         DataRequired(), Length(min=3, max=128)])
    publisher = StringField('publisher', validators=[
                            DataRequired(), Length(min=3, max=128)])
    year_of_pub = IntegerField('year_of_pub', validators=[DataRequired()])
    num_of_copies = IntegerField('num_of_copies', validators=[DataRequired()])
    price = DecimalField('price', validators=[DataRequired()])
    format = StringField('format', validators=[
                         DataRequired(), Length(min=3, max=128)])
    keywords = StringField('keywords', validators=[
                           DataRequired(), Length(min=3, max=128)])
    subject = StringField('subject', validators=[
                          DataRequired(), Length(min=3, max=128)])

    def __init__(self, *args, **kwargs):
        """Init."""
        super(UpdateBookForm, self).__init__(*args, **kwargs)
        self.book = None

    def validate(self):
        """Validate add book form."""
        initial_validation = super(UpdateBookForm, self).validate()
        if not initial_validation:
            return False
        book1 = Book.query.filter_by(isbn13=self.isbn13.data).first()
        if not book1:
            self.isbn13.errors.append('Book ID does not exist.')
            return False
        return True
