import pytest
from django.test import TestCase

from tests.factories import EngagementFactory
from Apres_Ski_API.serializers import EngagementSerializer

class EngagementSerializerTests(TestCase):
  def test_serialize_engagement(self):
    engagement = EngagementFactory()
    serialized_engagement = EngagementSerializer(engagement)

    data = serialized_engagement.data
    assert isinstance(data, dict)
    assert len(data) == 6
    assert isinstance(data['id'], int)
    assert isinstance(data['vibe'], str)
    assert isinstance(data['rating'], str)
    assert isinstance(data['favorites'], bool)
    assert isinstance(data['restaurant'], list)
    assert isinstance(data['user'], list)