import pytest
from rest_framework import status
from django.test import RequestFactory, TestCase

from tests.factories import CommentFactory
from Apres_Ski_API.views.comment import CommentViewSet

class CommentViewTests(TestCase):
  def test_comment_200_OK(self):
    request = RequestFactory().get("api/v1/comment")
    view = CommentViewSet.as_view({'get': 'retrieve'})
    comment = CommentFactory()
    response = view(request, pk=comment.pk)
    assert response.status_code == status.HTTP_200_OK
