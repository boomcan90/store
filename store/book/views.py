# -*- coding: utf-8 -*-
"""Book views."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from store.book.models import Book
from store.book.forms import AddBookForm

from store.utils import flash_errors


book_blueprint = Blueprint(
    'book', __name__, url_prefix='/book', static_folder='../static')


@book_blueprint.route('/')
def hello():
    """A trivial route."""
    return "hello!"


@book_blueprint.route('/book', methods=['GET'])
def book():
    """List 1 book."""
    book = Book.query.first()
    # return "Book details"
    return render_template('book/book.html', book=book)


@book_blueprint.route('/books', methods=['GET'])
def book_list():
    """Return list of books."""
    book = Book.query.all()

    return render_template('book/booklist.html', books=book)


@book_blueprint.route('/add', methods=['GET', 'POST'])
def add_book():
    """Add book."""
    form = AddBookForm(request.form)
    # Handle add book form
    if request.method == 'POST':
        if form.validate_on_submit():
            Book.create(book)
            flash('You are added the book!', 'success')
            redirect_url = request.args.get(
                'next') or url_for('book.add_book')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('book/addbooks.html', form=form)
