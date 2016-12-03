# -*- coding: utf-8 -*-
"""Book views."""
from flask import Blueprint, flash, redirect, render_template, request, url_for, abort
from store.book.models import Book
from store.book.forms import AddBookForm

from store.feedback.models import Feedback

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


# Route should require login and manager
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


@book_blueprint.route('/browse', methods=['GET'])
def browse():
    """Browse books."""
    book = Book.query.all()

    return render_template('book/browse.html', books=book)


@book_blueprint.route('/details/<isbn13>', methods=['GET'])
def details(isbn13=None):
    """Book detail."""
    book = Book.query.filter_by(isbn13=isbn13)
    book = book.first()

    if not book:
        abort(404)

    reviews = Feedback.query.filter_by(book_id=isbn13).all()

    return render_template('book/book.html', book=book, reviews=reviews)


@book_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    """Page for performing conjunctive queries on books."""
    # TODO: some search form for doing conjunctive queries.
    # t = Book.query.filter(or_(and_(Book.format=="paperback", Book.price < 8), Book.subject=="romance"))
    # SELECT book.isbn13 AS book_isbn13, book.title AS book_title, book.author AS book_author, book.publisher AS book_publisher, book.year_of_pub AS book_year_of_pub, book.num_of_copies AS book_num_of_copies, book.price AS book_price, book.format AS book_format, book.keywords AS book_keywords, book.subject AS book_subject
    # FROM book
    # WHERE book.format = ? AND book.price < ? OR book.subject = ?
    return render_template('book/search.html')
