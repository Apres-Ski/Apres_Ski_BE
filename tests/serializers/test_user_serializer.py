import pytest
from django.test import TestCase

from tests.factories import UserFactory
from Apres_Ski_API.serializers import UserSerializer

class UserSerializerTests(TestCase):
  def test_serialize_user(self):
    user = UserFactory()
    serialized_user = UserSerializer(user)

    data = serialized_user.data
    assert isinstance(data, dict)
    assert len(data) == 4
    assert isinstance(data['id'], int)
    assert isinstance(data['name'], str)
    assert isinstance(data['lat'], str)
    assert isinstance(data['lon'], str)