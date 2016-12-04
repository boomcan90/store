"""Feedback Views."""
from flask import Blueprint
from .models import Feedback  # noqa

feedback_blueprint = Blueprint(
    'feedback', __name__, url_prefix='/feedback', static_folder='../static')
