import pytest
import json
from django.test import TestCase, Client
from tests.factories import RestaurantFactory

class RestaurantShowTests(TestCase):
    def test_restaurant_list(self):
        restaurant = RestaurantFactory()
        client = Client()
        response = client.get(f"/api/v1/restaurant/{restaurant.id}/")

        assert response.status_code == 200
        content = json.loads(response.content)
        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['data'], dict)
        assert len(content['data']) == 3

        entry = content['data']
        assert isinstance(entry['type'], str)
        assert entry['type'] == 'Restaurant'
        assert isinstance(entry['id'], str)
        assert isinstance(entry['attributes'], dict)
        assert len(entry['attributes']) == 13
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