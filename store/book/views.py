# -*- coding: utf-8 -*-
"""Book views."""
from flask import Blueprint, flash, redirect, render_template, request, url_for, abort
from flask_login import current_user, login_required  # noqa
from store.book.models import Book
from store.book.forms import AddBookForm, UpdateBookForm, SearchBookForm

from store.customer.models import Customer

from store.feedback.models import Feedback, Rates
from store.feedback.forms import FeedbackForm

from flask_login import current_user

from store.utils import flash_errors
from store.database import db
from sqlalchemy import func, and_, desc


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
    return render_template('book/book.html', book=book, form=None)


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
            Book.create(isbn13=form.isbn13.data, title=form.title.data, author=form.author.data,
                        publisher=form.publisher.data, year_of_pub=form.year_of_pub.data,
                        num_of_copies=form.num_of_copies.data, price=form.price.data, format=form.format.data,
                        keywords=form.keywords.data, subject=form.subject.data)
            flash('You are added the book: {}!'.format(
                form.title.data), 'success')
            redirect_url = request.args.get(
                'next') or url_for('book.add_book')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('book/addbooks.html', form=form)


# Route should require login and manager
@book_blueprint.route('/update/<isbn13>', methods=['GET', 'POST'])
def update_book(isbn13=None):
    """Update book."""
    book = Book.query.filter_by(isbn13=isbn13)
    book = book.first()

    if not book:
        abort(404)

    form = UpdateBookForm(obj=book)
    # Handle add book form
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(book)
            Book.update(book)
            flash('You are updated the book!', 'success')
            redirect_url = request.args.get(
                'next') or url_for('book.update_book', isbn13=book.isbn13)
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('book/updatebook.html', form=form)


@book_blueprint.route('/browse', methods=['GET'])
def browse():
    """Browse books."""
    book = Book.query.all()

    return render_template('book/browse.html', books=book)

@book_blueprint.route('/details/<isbn13>', methods=['GET', 'POST'])
@book_blueprint.route('/details/<isbn13>/<int:num_feedbacks>', methods=['GET', 'POST'])
def details(isbn13=None, num_feedbacks=0):
    """Book detail."""
    book = Book.query.filter_by(isbn13=isbn13)
    book = book.first()

    if not book:
        abort(404)

    feedbackform = None
    if current_user.is_authenticated:
        feedbackform = FeedbackForm(request.form, prefix="feedbackform")  # noqa
        feedbackform.set_user_isbn(user=current_user.id, isbn=isbn13)

    if request.method == 'POST' and current_user.is_authenticated:
        if feedbackform.validate_on_submit() and feedbackform.submit.data:
            print("CREATING FEEDBACK")

            newfeedback = Feedback(user_id=current_user.id, book_id=isbn13,
                                   short_text=feedbackform.short_text.data, score=feedbackform.score.data)

            customer = Customer.query.filter_by(id=current_user.id).first()
            print(customer)
            customer.reviews.append(newfeedback)

            customer.save()

            redirect_url = request.args.get(
                'next') or url_for('book.details', isbn13=isbn13)
            return redirect(redirect_url)
        else:
            flash_errors(feedbackform)

    reviews = Feedback.query.filter_by(book_id=isbn13).all()
    if num_feedbacks > 0:
        temp_reviews = db.session.query(Feedback).join(Rates).filter(
            Feedback.book_id == isbn13).group_by(Feedback.id).order_by(func.avg(Rates.rating).desc()).all()
        # reviews = db.session.query(Feedback).join(Rates).filter(Feedback.book_id == isbn13).all()
        if len(temp_reviews) > 0:
            reviews = temp_reviews

    return render_template('book/book.html', book=book, reviews=reviews, feedbackform=feedbackform)


@book_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    """Page for performing conjunctive queries on books.

    Professor said we can just do AND.
    """
    form = SearchBookForm(request.form)
    # TODO: some search form for doing conjunctive queries.
    # t = Book.query.filter(or_(and_(Book.format=="paperback", Book.price < 8), Book.subject=="romance"))
    # t = Book.query.filter(or_(and_(*[Book.format=="paperback", Book.price < 8]),
    # *[Book.subject=="romance", Book.author=="JK"]))
    result = None

    if request.method == 'POST':
        if form.validate_on_submit():
            query_array = []
            for fieldname, value in form.data.items():
                if value and (fieldname is not "order"):
                    # Book.{method}.contains()
                    query_array.append(getattr(Book, fieldname).contains(value))

                if fieldname == "order":
                    if value == "avgfb":
                        # Book.avgfb is a Basequery
                        ordering = desc(Book.avgfb)
                    else:
                        ordering = Book.year_of_pub.desc()
            q = Book.query.filter(and_(*query_array)).order_by(ordering)
            print(q)
            result = q.all()
            print(result)
            return render_template('book/search.html', form=form, result=result)
        else:
            flash_errors(form)
    return render_template('book/search.html', form=form)
