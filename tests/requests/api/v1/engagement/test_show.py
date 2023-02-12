import pytest
import json
from django.test import TestCase, Client
from tests.factories import EngagementFactory

class EngagementShowTests(TestCase):
    def test_engagement_show(self):
        engagement = EngagementFactory()
        client = Client()
        response = client.get(f"/api/v1/engagement/{engagement.id}/")

        assert response.status_code == 200
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

    def test_engagement_show_404(self):
        engagement = EngagementFactory()
        client = Client()
        response = client.get(f"/api/v1/engagement/{engagement.id + 1}/")
        assert response.status_code == 404

        content = json.loads(response.content)
        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['errors'], list)
        assert len(content['errors']) == 1

        error = content['errors'][0]
        assert isinstance(error, dict)
        assert len(error) == 3
        assert error['detail'] == 'Not found.'
        assert error['status'] == '404'
        assert error['code'] == 'not_found'