import pytest
import json
from django.test import TestCase, Client
from tests.factories import HappyHourFactory

class HappyHourIndexTests(TestCase):
    def test_happy_hour_index(self):
        HappyHourFactory.create_batch(1)
        client = Client()
        response = client.get('/api/v1/happy_hour/')

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
          assert entry['type'] == 'HappyHour'
          assert isinstance(entry['id'], str)
          assert isinstance(entry['attributes'], dict)
          assert len(entry['attributes']) == 8
          assert isinstance(entry['attributes']['sunday'], str)
          assert isinstance(entry['attributes']['monday'], str)
          assert isinstance(entry['attributes']['tuesday'], str)
          assert isinstance(entry['attributes']['wednesday'], str)
          assert isinstance(entry['attributes']['thursday'], str)
          assert isinstance(entry['attributes']['friday'], str)
          assert isinstance(entry['attributes']['saturday'], str)
   
