# -*- coding: utf-8 -*-
"""Order views."""

from flask import Blueprint, flash, redirect, render_template, request, url_for, abort, jsonify
from flask_login import current_user, login_required  # noqa

from store.orders.models import Order, OrderConsistsOf, Book
from store.orders.forms import AddOrderForm
from store.customer.models import Customer

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


@order_blueprint.route('/popular_books', methods=['GET'])
def pop_books():
    popular_books = []
    q1 = OrderConsistsOf.query.all()
    q2 = db.session.query(OrderConsistsOf.consists_isbn13, func.count(OrderConsistsOf.consists_qty))\
        .group_by(OrderConsistsOf.consists_isbn13).all()
    for p2 in q2:
        count = 0
        for p1 in q1:
            if(p1.to_json()['isbn13'] == p2[0]):
                count += p1.to_json()['quantity']
        popular_books.append((p2[0], count))
    return render_template("user/popular_books.html", popular_books=popular_books)
# ----------------------------------------------------------------


@order_blueprint.route('/popular_authors', methods=['GET'])
def pop_authors():
    popular_authors = []
    q = db.session.query(OrderConsistsOf.consists_isbn13, Book.author, OrderConsistsOf.consists_qty).\
        join(Book).filter(Book.isbn13 == OrderConsistsOf.consists_isbn13).all()
    authors = list(set([p[1] for p in q]))
    for p1 in authors:
        count = 0
        for p2 in q:
            if p1 == p2[1]:
                count += p2[2]
        popular_authors.append((p1, count))
    return render_template("user/popular_authors.html", popular_authors=popular_authors)
# ----------------------------------------------------------------


@order_blueprint.route('/popular_publishers', methods=['GET'])
def pop_publishers():
    popular_publishers = []
    q = db.session.query(OrderConsistsOf.consists_isbn13, Book.publisher, OrderConsistsOf.consists_qty).\
        join(Book).filter(Book.isbn13 == OrderConsistsOf.consists_isbn13).all()
    publishers = list(set([p[1] for p in q]))
    # print(publishers)
    for p1 in publishers:
        count = 0
        for p2 in q:
            if p1 == p2[1]:
                count += p2[2]
        popular_publishers.append((p1, count))
    return render_template("user/popular_publishers.html", popular_publishers=popular_publishers)
# ----------------------------------------------------------------


@order_blueprint.route('/orderBook/<isbn13>', methods=['GET', 'POST'])
@login_required
def order_book(isbn13):
    customerid = current_user.get_id()
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
        return redirect(url_for('book.browse'))
    else:
        flash_errors(form)

    RECOMMENDATIONS = []
    """Get book recommendation."""
    if current_user.is_authenticated:
        id = current_user.get_id()
        # get the book rec
        q1 = db.session.query(OrderConsistsOf.consists_order_id).filter(OrderConsistsOf.consists_isbn13 == isbn13).\
            filter(OrderConsistsOf.consists_order_id != id).all()

        for q in q1:
            isbn13_list = db.session.query(OrderConsistsOf.consists_isbn13).filter(OrderConsistsOf.consists_order_id == q[0]).\
                filter(OrderConsistsOf.consists_isbn13 != isbn13).all()
            if isbn13_list != []:
                for i in isbn13_list:
                    RECOMMENDATIONS.append(db.session.query(
                        Book).filter(Book.isbn13 == i[0]).first())

    return render_template('orders/addorder.html', form=form, recommendations=RECOMMENDATIONS)

# Order history for the customer


@order_blueprint.route('/orderHistory/<id>', methods=['GET'])
def order_history(id):
    """Order history."""
    # q = OrderConsistsOf.query.join(Order, (OrderConsistsOf.consists_order_id == Order.id)).filter(
    #     Order.customer_id == id).all()

    q = Order.query.join(Customer, OrderConsistsOf).filter(Customer.id == id).order_by(Order.date.desc()).all()
    return render_template('orders/orderhistory.html', historicalorders=q, id=id)


@order_blueprint.route('/recommendation/<isbn13>', methods=['GET'])
def recommendation(isbn13):
    RECOMMENDATIONS = []
    """Get book recommendation."""
    if current_user.is_authenticated:
        id = current_user.get_id()
        # get the book rec
        q1 = db.session.query(OrderConsistsOf.consists_order_id).filter(OrderConsistsOf.consists_isbn13 == isbn13).\
            filter(OrderConsistsOf.consists_order_id != id).all()

        for q in q1:
            isbn13_list = db.session.query(OrderConsistsOf.consists_isbn13).filter(OrderConsistsOf.consists_order_id == q[0]).\
                filter(OrderConsistsOf.consists_isbn13 != isbn13).all()
            if isbn13_list != []:
                for i in isbn13_list:
                    RECOMMENDATIONS.append(db.session.query(
                        Book).filter(Book.isbn13 == i[0]).first())

    # return jsonify(data=[x.to_json() for x in RECCOMENDATIONS])
    print(RECOMMENDATIONS)
    return render_template('orders/recommendation.html', recommendations=RECOMMENDATIONS)


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
