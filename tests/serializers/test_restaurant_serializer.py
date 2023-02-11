import pytest
from django.test import TestCase

from tests.factories import RestaurantFactory
from Apres_Ski_API.serializers import RestaurantSerializer

class RestaurantSerializerTests(TestCase):
  def test_serialize_restaurant(self):
    restaurant = RestaurantFactory()
    serialized_restaurant = RestaurantSerializer(restaurant)

    data = serialized_restaurant.data
    assert isinstance(data, dict)
    assert len(data) == 14
    assert isinstance(data['id'], int)
    assert isinstance(data['name'], str)
    assert isinstance(data['address'], str)
    assert isinstance(data['food_type'], str)
    assert isinstance(data['cost'], str)
    assert isinstance(data['cover_img'], str)
    assert isinstance(data['alt_text'], str)
    assert isinstance(data['lat'], str)
    assert isinstance(data['lon'], str)
    assert isinstance(data['alcoholic_drinks'], bool)
    assert isinstance(data['has_happy_hour'], bool)
    assert isinstance(data['hour'], list)
    assert isinstance(data['happyhour'], list)
    assert isinstance(data['engagement'], list)
