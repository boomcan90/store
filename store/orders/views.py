# -*- coding: utf-8 -*-
"""Order views."""

from flask import Blueprint, render_template, jsonify, abort
from flask_login import current_user
from store.orders.models import Order, Order_Consists_Of

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

# Explictly declared available methods
# Route using a noun to make Nils proud.


@order_blueprint.route('/orders', methods=['GET'])
def browse():
    """
    Route should show a list of orders.

    Nope. YOU LIED, ROBIN
    """
    return "List of NOT beer"


@order_blueprint.route('/ordersList', methods=['GET'])
def browse_list():
    """
    Route really should show a json list of beer.

    Nils is now proud. Good job!
    .....Pls let dis werkzzzz
    """
    result = Order.query.all()
    return jsonify(data=[x.toJson() for x in result])

# ---------------------------------------------------------------------------


@order_blueprint.route('/')
def hello_again():
    return "Hello! Here is a relationship, just not the kind you're looking for"


@order_blueprint.route('/consistsof', methods=['GET'])
def browse_consistsof_fake():
    return "List of NOT beer NOR ORDERS OR BOOKS"


@order_blueprint.route('/ordersList', methods=['GET'])
def browse_consistsof():
    """
    .....Pls let dis werkzzzz
    """
    result = Order_Consists_Of.query.all()
    return jsonify(data=[x.toJson() for x in result])
