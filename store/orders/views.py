# -*- coding: utf-8 -*-
"""Order views."""

from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('orders', __name__, url_prefix='/orders', static_folder='../static')


@blueprint.route('/')
@login_required
def members():
    """List members."""
    return render_template('orders/orderListing.html')
