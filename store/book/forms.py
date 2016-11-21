# -*- coding: utf-8 -*-
"""Book forms."""
from flask_wtf import Form
from wtforms.validators import DataRequired, EqualTo, Length

from store.user.models import Book

class AddBookForm(Form):
	"""Add Book Form"""

