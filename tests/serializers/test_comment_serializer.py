import pytest
from django.test import TestCase

from tests.factories import CommentFactory
from Apres_Ski_API.serializers import CommentSerializer

class CommentSerializerTests(TestCase):
  def test_serialize_comment(self):
    comment = CommentFactory()
    serialized_comment = CommentSerializer(comment)

    data = serialized_comment.data
    assert isinstance(data, dict)
    assert len(data) == 4
    assert isinstance(data['id'], int)
    assert isinstance(data['comment'], str)
    assert isinstance(data['restaurant'], list)
    assert isinstance(data['user'], list)