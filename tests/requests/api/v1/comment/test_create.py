import pytest
import json
from django.test import TestCase, Client
from tests.factories import CommentFactory, RestaurantFactory, UserFactory

class CommentCreateTests(TestCase):
    def test_comment_create(self):
        resturant = RestaurantFactory()
        user = UserFactory()
        client = Client()
        comment = { "comment": "super cool",
                    "restaurant": [1],
                    "user": [1]
        }
        response = client.post("/api/v1/comment/", comment)

        assert response.status_code == 201
        content = json.loads(response.content)

        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['data'], dict)
        assert len(content['data']) == 4

        entry = content['data']
        assert isinstance(entry['type'], str)
        assert entry['type'] == 'Comment'
        assert isinstance(entry['id'], str)
        assert isinstance(entry['attributes'], dict)
        assert len(entry['attributes']) == 1
        assert isinstance(entry['attributes']['comment'], str)
