"""Feedback Views."""
from flask import Blueprint, redirect, url_for, request, abort
from flask_login import current_user
from .models import Feedback, Rates  # noqa
from store.customer.models import Customer

feedback_blueprint = Blueprint(
    'feedback', __name__, url_prefix='/feedback', static_folder='../static')


@feedback_blueprint.route('/rate', methods=['GET'])
def rate_feedback():
    """Rate a feeback.

    Hacky GET request method.
    """
    feedback_id = request.args.get('feedback_id')
    rater = current_user.id
    rating = request.args.get('rating')

    if not feedback_id:
        print("failed fb_id")
        return abort(404)

    fb = Feedback.query.filter_by(id=feedback_id).first()
    if not fb:
        print("no such fb")
        return abort(404)

    if rater and rating and feedback_id:
        print(fb.id, rater, fb.user_id, rating)
        newrating = Rates(fb.id, rater, fb.user_id, rating)
        customer = Customer.query.filter_by(id=rater).first()
        customer.ratings_given.append(newrating)
        customer.save()
    else:
        print("kaboom")
        return abort(404)

    return redirect(url_for('book.details', isbn13=fb.book_id))
