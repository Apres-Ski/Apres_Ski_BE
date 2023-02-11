import pytest
from django.test import TestCase

from tests.factories import HourFactory
from Apres_Ski_API.serializers import HourSerializer

class HourSerializerTests(TestCase):
  def test_serialize_hour(self):
    hour = HourFactory()
    serialized_hour = HourSerializer(hour)

    data = serialized_hour.data
    assert isinstance(data, dict)
    assert len(data) == 9
    assert isinstance(data['id'], int)
    assert isinstance(data['sunday'], str)
    assert isinstance(data['monday'], str)
    assert isinstance(data['tuesday'], str)
    assert isinstance(data['wednesday'], str)
    assert isinstance(data['thursday'], str)
    assert isinstance(data['friday'], str)
    assert isinstance(data['saturday'], str)
    assert isinstance(data['restaurant'], int)

