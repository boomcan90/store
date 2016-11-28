# -*- coding: utf-8 -*-
"""Book forms."""
from flask_wtf import Form
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired, EqualTo, Length

from store.user.models import Book

class AddBookForm(Form):
	"""Add Book Form"""
    isbn13 = StringField('isbn13',validators=[DataRequired(), Length(min=5, max=13)])
    title =  StringField('title',validators=[DataRequired(), Length(min=3, max=128)])
    author = StringField('author',validators=[DataRequired(), Length(min=3, max=128)])
    publisher = StringField('publisher',validators=[DataRequired(), Length(min=3, max=128)])
    year_of_pub = IntegerField('year_of_pub',validators=[DataRequired(), Length(min=3, max=128), message='Year must be an integer.'])
    num_of_copies = 
    price = 
    format = 
    keywords = 
    subject = 
