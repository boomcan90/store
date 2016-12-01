# -*- coding: utf-8 -*-
"""Book views."""
from flask import Blueprint, render_template, jsonify
from store.book.models import Book


book_blueprint = Blueprint('book', __name__, url_prefix='/book', static_folder='../static')

#127.0.0.1:5000/book/
@book_blueprint.route('/')
def hello():
    '''
    A trivial route.
    '''
    return "hello!"

#127.0.0.1:5000/book/book
@book_blueprint.route('/book', methods=['GET'])
def book():
    """List 1 book"""
    book = Book.query.first()
    # return "Book details"
    return render_template('book/book.html', book=book)

#127.0.0.1:5000/book/books
@book_blueprint.route('/books', methods=['GET'])
def bookList():

    # recipe = session.query(Recipe, Ingredient).filter(Recipe.id==Ingredient.recipe_id).filter(Ingredient.name.contains(query)).all()
    book = Book.query.all()

    # return jsonify(data = [x.to_json() for x in result])
    return render_template('book/booklist.html', books=book)
    