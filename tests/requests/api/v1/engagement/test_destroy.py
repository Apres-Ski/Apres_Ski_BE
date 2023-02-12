import pytest
import json
from django.test import TestCase, Client
from tests.factories import EngagementFactory

class EngagementShowTests(TestCase):
    def test_engagement_destroy_204(self):
        engagement = EngagementFactory()
        client = Client()
        response = client.delete(f"/api/v1/engagement/{engagement.id}/")

        assert response.status_code == 204

    def test_engagement_destroy_404(self):
        engagement = EngagementFactory()
        client = Client()
        response = client.delete(f"/api/v1/engagement/{engagement.id + 1}/")
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