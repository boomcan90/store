# -*- coding: utf-8 -*-
"""Order views."""

from flask import Blueprint, render_template, jsonify
from store.orders.models import Order, Order_Consists_Of

order_blueprint = Blueprint('orders', __name__, url_prefix='/orders', static_folder='../static')

consistsof_blueprint = Blueprint('consists_of', __name__, url_prefix='/consistsof', static_folder='../static') 


@order_blueprint.route('/')
def hello():
    '''
    A trivial route.
    '''
    return "Hello!"

# Explictly declared available methods
# Route using a noun to make Nils proud.
@order_blueprint.route('/orders', methods=['GET'])
def browse():
    '''
    This route should show a list of orders.
    Nope. YOU LIED, ROBIN
    '''
    return "List of NOT beer"

@order_blueprint.route('/ordersList', methods=['GET'])
def browse_list():
    '''
    This route really should show a json list of beer.
    Nils is now proud. Good job!
    .....Pls let dis werkzzzz
    '''
    result = Order.query.all()
    return jsonify(data = [x.toJson() for x in result])

# ---------------------------------------------------------------------------
@consistsof_blueprint.route('/')
def hello():
    return "Hello! Here is a relationship, just not the kind you're looking for"
@consistsof_blueprint.route('/consistsof', methods=['GET'])
def browse_consistsof_fake():
    return "List of NOT beer NOR ORDERS OR BOOKS"

@consistsof_blueprint.route('/ordersList', methods=['GET'])
def browse_consistsof():
    '''
    .....Pls let dis werkzzzz
    '''
    result = Order_Consists_Of.query.all()
    return jsonify(data = [x.toJson() for x in result])

