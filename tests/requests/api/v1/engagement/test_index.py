import pytest
import json
from django.test import TestCase, Client
from tests.factories import EngagementFactory

class EngagementIndexTests(TestCase):
    def test_engagement_index(self):
        EngagementFactory.create_batch(1)
        client = Client()
        response = client.get('/api/v1/engagement/')

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
          assert entry['type'] == 'Engagement'
          assert isinstance(entry['id'], str)
          assert isinstance(entry['attributes'], dict)
          assert len(entry['attributes']) == 3
          assert isinstance(entry['attributes']['vibe'], str)
          assert isinstance(entry['attributes']['rating'], str)
          assert isinstance(entry['attributes']['favorites'], bool)
   
