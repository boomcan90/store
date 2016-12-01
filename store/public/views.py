# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, render_template

from store.extensions import login_manager
from store.user.models import User
from store.customer.models import Customer
from store.book.models import Book

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(str(user_id))


@login_manager.user_loader
def load_customer(customer_id):
    """Load customer by login name."""
    return Customer.get_by_id(str(customer_id))


@blueprint.route('/index', methods=['GET', 'POST'])
@blueprint.route('/index/<int:page>', methods=['GET', 'POST'])
@blueprint.route('/', methods=['GET', 'POST'])
def home(page=1):
    """Home page."""
    # Should be top grossing books.
    books = Book.query.paginate(page, 6, False)
    return render_template('index.html', best=books, books=books)
