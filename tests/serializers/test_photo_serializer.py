import pytest
from django.test import TestCase

from tests.factories import PhotoFactory
from Apres_Ski_API.serializers import PhotoSerializer

class PhotoSerializerTests(TestCase):
  def test_serialize_photo(self):
    photo = PhotoFactory()
    serialized_photo = PhotoSerializer(photo)

    data = serialized_photo.data
    assert isinstance(data, dict)
    assert len(data) == 4
    assert isinstance(data['id'], int)
    assert isinstance(data['url'], str)
    assert isinstance(data['alt_text'], str)
    assert isinstance(data['restaurant'], int)