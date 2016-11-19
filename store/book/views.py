# -*- coding: utf-8 -*-
"""Book views."""
from flask import Blueprint, render_template, jsonify
from store.book.models import Book


book_blueprint = Blueprint('book', __name__, url_prefix='/book', static_folder='../static')


@book_blueprint.route('/')
def hello():
    '''
    A trivial route.
    '''
    return "hello!"

@book_blueprint.route('/book', methods=['GET'])
def book():
    """List 1 book"""
    #return render_template('books/index.html')
    return"Book details"

@book_blueprint.route('/books', methods=['GET'])
def bookList():
    return "List of books and details"
    # result = Book.query.all()
    # return jsonify(data = [x.to_json() for x in result])