# -*- coding: utf-8 -*-
"""Order views."""

from flask import Blueprint, flash, redirect, render_template, request, url_for, abort, jsonify
from flask_login import current_user, login_required  # noqa

from store.orders.models import Order, OrderConsistsOf
from store.orders.forms import AddOrderForm

from store.utils import flash_errors
from store.database import db
from sqlalchemy import func



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

@order_blueprint.route('/orderBook/<customerid>/<isbn13>', methods=['GET', 'POST'])
def order_book(isbn13, customerid):
    form = AddOrderForm(request.form)
    if request.method == 'POST':
        order = Order.create(customer_id=customerid)
        flash('You, {}, have ordered a book!'.format(
               customerid), 'success')
        # order = Order.query.filter_by(customer_id=customerid)
        # order = order.first()
        OrderConsistsOf.create(consists_order_id=order.id, 
                               consists_isbn13=isbn13, consists_qty=form.qty.data)
        flash('You have ordered the book: {}!'.format(
                isbn13), 'success')
        return "Good job!"
    else:
        flash_errors(form)
    return render_template('orders/addorder.html', form=form)

# Order history for the customer
@order_blueprint.route('/orderHistory/<id>', methods=['GET'])
def order_history(id):
    """Order history."""
    q = OrderConsistsOf.query.join(Order, (OrderConsistsOf.consists_order_id == Order.id)).\
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
