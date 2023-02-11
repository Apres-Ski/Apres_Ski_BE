import pytest
from django.test import TestCase

from tests.factories import LiftFactory
from Apres_Ski_API.serializers import LiftSerializer

class LiftSerializerTests(TestCase):
  def test_serialize_lift(self):
    lift = LiftFactory()
    serialized_lift = LiftSerializer(lift)

    data = serialized_lift.data
    assert isinstance(data, dict)
    assert len(data) == 4
    assert isinstance(data['id'], int)
    assert isinstance(data['name'], str)
    assert isinstance(data['lat'], str)
    assert isinstance(data['lon'], str)