import pytest
import json
from django.test import TestCase, Client
from tests.factories import HourFactory, RestaurantFactory

class HourCreateTests(TestCase):
    def test_hour_create(self):
        restaurant = RestaurantFactory()
        client = Client()
        hour = {
                "sunday": "6:40 AM - 10:00 AM",
                "monday": "6:40 AM - 10:00 AM",
                "tuesday": "6:40 AM - 10:00 AM",
                "wednesday": "6:40 AM - 10:00 AM",
                "thursday": "6:30 AM - 10:00AM; 4:00PM - 9:00 PM",
                "friday": "6:30 AM - 10:00AM; 4:00PM - 9:00 PM",
                "saturday": "6:30 AM - 10:00AM; 4:00PM - 9:00 PM",
                "restaurant": restaurant.pk
        }
        response = client.post("/api/v1/hour/", hour)

        assert response.status_code == 201
        content = json.loads(response.content)

        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['data'], dict)
        assert len(content['data']) == 4

        entry = content['data']
        assert isinstance(entry['type'], str)
        assert entry['type'] == 'Hour'
        assert isinstance(entry['id'], str)
        assert isinstance(entry['attributes'], dict)
        assert len(entry['attributes']) == 7
        assert isinstance(entry['attributes']['sunday'], str)
        assert isinstance(entry['attributes']['monday'], str)
        assert isinstance(entry['attributes']['tuesday'], str)
        assert isinstance(entry['attributes']['wednesday'], str)
        assert isinstance(entry['attributes']['thursday'], str)
        assert isinstance(entry['attributes']['friday'], str)
        assert isinstance(entry['attributes']['saturday'], str)


