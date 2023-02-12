import pytest
import json
from django.test import TestCase, Client
from tests.factories import PhotoFactory

class PhotoIndexTests(TestCase):
    def test_photo_index(self):
        PhotoFactory.create_batch(1)
        client = Client()
        response = client.get('/api/v1/photo/')

        assert response.status_code == 200
        content = json.loads(response.content)
        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['data'], list)
        assert len(content['data']) == 1

        for entry in content['data']:
          assert isinstance(entry, dict)
          assert len(entry) == 4
          assert isinstance(entry['type'], str)
          assert entry['type'] == 'Photo'
          assert isinstance(entry['id'], str)
          assert isinstance(entry['attributes'], dict)
          assert len(entry['attributes']) == 2
          assert isinstance(entry['attributes']['url'], str)
          assert isinstance(entry['attributes']['alt_text'], str)
   
