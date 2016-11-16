# -*- coding: utf-8 -*-
"""Cellar Model unit tests."""
import datetime as dt

import pytest

from store.cellar.models import Alcohol

from .factories import AlcoholFactory

@pytest.mark.usefixtures('db')
class TestAlcohol:
    """Alcohol tests"""

    def test_get_by_id(self):
        """Get alcohol by ID."""
        beer = Alcohol('beer0', 'beer', 5)
        beer.save()

        # this method is inherited from a class in database.py
        retrieved = Alcohol.get_by_id(beer.id)
        assert retrieved == beer


    def test_retreive_list_of_beer(self):
        """Retrieve a list of beer."""

        beer_bucket = []

        # http://factoryboy.readthedocs.io/en/latest/examples.html?highlight=create_batch#factories
        beer_bucket.extend(AlcoholFactory.create_batch(5))

        for beer in beer_bucket:
            beer.save()

        l = Alcohol.query.all()
        assert len(l) == 5