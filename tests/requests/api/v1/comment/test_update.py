import pytest
import json
from django.test import TestCase, Client
from tests.factories import CommentFactory

class CommentUpdateTests(TestCase):
    def test_comment_update(self):
        comment = CommentFactory()
        client = Client()
        comment_update = {
                      "data": {
                          "type": "Comment",
                          "id": f"{comment.pk}",
                          "attributes": {
                            "comment": "great food"
                          }
                      }
        }
        data = json.dumps(comment_update)
        response = client.patch(f"/api/v1/comment/{comment.pk}/", data, content_type='application/vnd.api+json')

        assert response.status_code == 200
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
        assert entry['attributes']['comment'] == 'great food'
        assert isinstance(entry['attributes']['comment'], str)


    def test_comment_update_404(self):
        comment = CommentFactory()
        client = Client()
        response = client.patch(f"/api/v1/comment/{comment.id + 1}/")
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