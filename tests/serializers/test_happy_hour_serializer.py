import pytest
from django.test import TestCase

from tests.factories import HappyHourFactory
from Apres_Ski_API.serializers import HappyHourSerializer

class HappyHourSerializerTests(TestCase):
  def test_serialize_hour(self):
    happy_hour = HappyHourFactory()
    serialized_happy_hour = HappyHourSerializer(happy_hour)

    data = serialized_happy_hour.data
    assert isinstance(data, dict)
    assert len(data) == 10
    assert isinstance(data['id'], int)
    assert isinstance(data['sunday'], str)
    assert isinstance(data['monday'], str)
    assert isinstance(data['tuesday'], str)
    assert isinstance(data['wednesday'], str)
    assert isinstance(data['thursday'], str)
    assert isinstance(data['friday'], str)
    assert isinstance(data['saturday'], str)
    assert isinstance(data['special'], str)
    assert isinstance(data['restaurant'], int)