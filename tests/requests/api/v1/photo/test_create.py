import pytest
import json
from django.test import TestCase, Client
from tests.factories import PhotoFactory, RestaurantFactory

class PhotoCreateTests(TestCase):
    def test_photo_create(self):
        resturant = RestaurantFactory()
        client = Client()
        photo = {
                "url": 'url',
                "alt_text": 'alt_text',
                "restaurant": 1
        }
        response = client.post("/api/v1/photo/", photo)

        assert response.status_code == 201
        content = json.loads(response.content)

        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['data'], dict)
        assert len(content['data']) == 4

        entry = content['data']
        assert isinstance(entry['type'], str)
        assert entry['type'] == 'Photo'
        assert isinstance(entry['id'], str)
        assert isinstance(entry['attributes'], dict)
        assert len(entry['attributes']) == 2
        assert isinstance(entry['attributes']['url'], str)
        assert isinstance(entry['attributes']['alt_text'], str)
   
