import pytest
import json
from django.test import TestCase, Client
from tests.factories import EngagementFactory, RestaurantFactory, UserFactory

class EngagementCreateTests(TestCase):
    def test_engagement_create(self):
        restaurant = RestaurantFactory()
        user = UserFactory()
        client = Client()
        engagement = {
                      "vibe": "casual",
                      "rating": "4.5",
                      "favorites": True,
                      "restaurant": restaurant.pk,
                      "user": user.pk
        }
        response = client.post("/api/v1/engagement/", engagement)

        assert response.status_code == 201
        content = json.loads(response.content)

        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['data'], dict)
        assert len(content['data']) == 4

        entry = content['data']
        assert isinstance(entry['type'], str)
        assert entry['type'] == 'Engagement'
        assert isinstance(entry['id'], str)
        assert isinstance(entry['attributes'], dict)
        assert len(entry['attributes']) == 3
        assert isinstance(entry['attributes']['vibe'], str)
        assert isinstance(entry['attributes']['rating'], str)
        assert isinstance(entry['attributes']['favorites'], bool)
