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
    Warning eye cancer.
    """
    feedback_id = request.args.get('feedback_id')
    rater = current_user.id
    rating_num = request.args.get('rating')

    try:
        rating_num = int(rating_num)
        if rating_num > 2:
            print("Invalid rating")
            return abort(404)
    except Exception:
        print("Something wrong with int conversion.")
        return abort(404)

    if not feedback_id:
        print("Feedback id link")
        return abort(404)

    fb = Feedback.query.filter_by(id=feedback_id).first()
    # fb = Feedback.query.join(Rates).filter(Feedback.id == feedback_id, rater_id !=current_user.id).first()
    if not fb:
        print("No such feedback object.")
        return abort(404)

    for rating in fb.ratings:
        if rating.rater_id == current_user.id:
            print("You already rated! This feedback!")
            return abort(404)

    if rater and rating_num and feedback_id:
        print(fb.id, rater, fb.user_id, rating_num)
        newrating = Rates(fb.id, rater, fb.user_id, rating_num)
        customer = Customer.query.filter_by(id=rater).first()
        customer.ratings_given.append(newrating)
        customer.save()
    else:
        print("kaboom")
        return abort(404)

    return redirect(url_for('book.details', isbn13=fb.book_id))
