import pytest
import json
from django.test import TestCase, Client
from tests.factories import UserFactory

class UserIndexTests(TestCase):
    def test_user_index(self):
        UserFactory.create_batch(3)
        client = Client()
        response = client.get('/api/v1/user/')

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
          assert entry['type'] == 'User'
          assert isinstance(entry['id'], str)
          assert isinstance(entry['attributes'], dict)
          assert len(entry['attributes']) == 3
          assert isinstance(entry['attributes']['name'], str)
          assert isinstance(entry['attributes']['lat'], str)
          assert isinstance(entry['attributes']['lon'], str)
          