import pytest
import json
from django.test import TestCase, Client
from tests.factories import UserFactory

class UserCreateTests(TestCase):
    def test_user_create(self):
        client = Client()
        user = {
                      "name": "name",
                      "lat": 'lat',
                      "lon": 'lon'
        }
        response = client.post("/api/v1/user/", user)

        assert response.status_code == 201
        content = json.loads(response.content)
        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['data'], dict)
        assert len(content['data']) == 3

        entry = content['data']
        assert isinstance(entry['type'], str)
        assert entry['type'] == 'User'
        assert isinstance(entry['id'], str)
        assert isinstance(entry['attributes'], dict)
        assert len(entry['attributes']) == 3
        assert isinstance(entry['attributes']['name'], str)
        assert isinstance(entry['attributes']['lat'], str)
        assert isinstance(entry['attributes']['lon'], str)
