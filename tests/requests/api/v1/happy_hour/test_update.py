import pytest
import json
from django.test import TestCase, Client
from tests.factories import HappyHourFactory

class HappyHourUpdateTests(TestCase):
    def test_happy_hour_update(self):
        happy_hour = HappyHourFactory()
        client = Client()
        happy_hour_update = {
                      "data": {
                          "type": "HappyHour",
                          "id": f"{happy_hour.pk}",
                          "attributes": {
                            "sunday": "1:00 PM - 3:00 PM"
                          }
                      }
        }
        data = json.dumps(happy_hour_update)
        response = client.patch(f"/api/v1/happy_hour/{happy_hour.pk}/", data, content_type='application/vnd.api+json')

        assert response.status_code == 200
        content = json.loads(response.content)
        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['data'], dict)
        assert len(content['data']) == 4

        entry = content['data']
        assert isinstance(entry['type'], str)
        assert entry['type'] == 'HappyHour'
        assert isinstance(entry['id'], str)
        assert isinstance(entry['attributes'], dict)
        assert len(entry['attributes']) == 8
        assert entry['attributes']['sunday'] == '1:00 PM - 3:00 PM'
        assert isinstance(entry['attributes']['monday'], str)
        assert isinstance(entry['attributes']['tuesday'], str)
        assert isinstance(entry['attributes']['wednesday'], str)
        assert isinstance(entry['attributes']['thursday'], str)
        assert isinstance(entry['attributes']['friday'], str)
        assert isinstance(entry['attributes']['saturday'], str)

    def test_happy_hour_update_404(self):
        happy_hour = HappyHourFactory()
        client = Client()
        response = client.patch(f"/api/v1/happy_hour/{happy_hour.id + 1}/")
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