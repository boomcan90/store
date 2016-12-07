# -*- coding: utf-8 -*-
"""Order views."""

from flask import Blueprint, render_template, jsonify, abort # noqa
from flask_login import current_user
from .models import Order, OrderConsistsOf

order_blueprint = Blueprint(
    'orders', __name__, url_prefix='/orders', static_folder='../static')


@order_blueprint.route('/')
def place_order():
    """A trivial route."""
    if current_user.is_authenticated:
        return current_user.get_id()
    else:
        # should redirect to more pleasant message
        return abort(401)


@order_blueprint.route('/orders', methods=['GET'])
def browse():
    """Route should show a list of orders."""
    return "List of NOT beer"


@order_blueprint.route('/ordersList', methods=['GET'])
def browse_list():
    """
    Route really should show a json list of beer.

    Nils is now proud. Good job!
    .....Pls let dis werkzzzz
    """
    result = Order.query.all()
    return jsonify(data=[x.to_json() for x in result])


# Order history for the customer
@order_blueprint.route('/orderHistory/', methods=['GET'])
def order_history():
    """Order history."""
    if current_user.is_authenticated:
        id = current_user.get_id()
        # now, to return order history of the user- returns isbn13 of book that customer has ordered
        q = OrderConsistsOf.query.join(Order, (OrderConsistsOf.consists_order_id == Order.order_id)).\
            filter(Order.customer_id == id).all()

        return jsonify(data=[x.to_json() for x in q])

# @order_blueprint.route('/recommend/<isbn13>', methods=['GET'])
# def reccomendation(isbn13):
#     """Get book recommendation"""
#     if current_user.is_authenticated:
#         id = current_user.get_id()
#         # get the book rec
#         q1 = OrderConsistsOf.query.filter(OrderConsistsOf.consists_isbn13).all()

#         list_of_orderid = [x.to_json() for x in result]

#         for element in list

# ---------------------------------------------------------------------------


@order_blueprint.route('/')
def hello_again():
    """Hello."""
    return "Hello! Here is a relationship, just not the kind you're looking for"


@order_blueprint.route('/consistsof', methods=['GET'])
def browse_consistsof_fake():
    """Test."""
    return "List of NOT beer NOR ORDERS OR BOOKS"


@order_blueprint.route('/ordersList', methods=['GET'])
def browse_consistsof():
    """Browse consists of."""
    result = OrderConsistsOf.query.all()
    return jsonify(data=[x.to_json() for x in result])
