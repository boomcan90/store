# -*- coding: utf-8 -*-
"""User views."""

from flask import Blueprint


blueprint = Blueprint('customer', __name__, url_prefix='/customer', static_folder='../static')


@blueprint.route('/')
def index():
    """Customer Index Route"""
    return "customer"
