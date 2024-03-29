import pytest
import json
from django.test import TestCase, Client
from tests.factories import RestaurantFactory

class RestaurantIndexTests(TestCase):
    def test_restaurant_index(self):
        RestaurantFactory.create_batch(3)
        client = Client()
        response = client.get('/api/v1/restaurant/')

        assert response.status_code == 200
        content = json.loads(response.content)
        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['data'], list)
        assert len(content['data']) == 3

        for entry in content['data']:
          assert isinstance(entry, dict)
          assert len(entry) == 3
          assert isinstance(entry['type'], str)
          assert entry['type'] == 'Restaurant'
          assert isinstance(entry['id'], str)
          assert isinstance(entry['attributes'], dict)
          assert len(entry['attributes']) == 14
          assert isinstance(entry['attributes']['name'], str)
          assert isinstance(entry['attributes']['address'], str)
          assert isinstance(entry['attributes']['food_type'], str)
          assert isinstance(entry['attributes']['cost'], str)
          assert isinstance(entry['attributes']['cover_img'], str)
          assert isinstance(entry['attributes']['alt_text'], str)
          assert isinstance(entry['attributes']['lat'], str)
          assert isinstance(entry['attributes']['lon'], str)
          assert isinstance(entry['attributes']['alcoholic_drinks'], bool)
          assert isinstance(entry['attributes']['has_happy_hour'], bool)
          assert isinstance(entry['attributes']['hour'], list)
          assert isinstance(entry['attributes']['happyhour'], list)
          assert isinstance(entry['attributes']['engagement'], list)
          assert isinstance(entry['attributes']['photo'], list)