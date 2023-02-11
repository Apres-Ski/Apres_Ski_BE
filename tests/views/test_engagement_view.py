import pytest
from rest_framework import status
from django.test import RequestFactory, TestCase

from tests.factories import EngagementFactory
from Apres_Ski_API.views.engagement import EngagementViewSet

class EngagementViewTests(TestCase):
  def test_engagement_200_OK(self):
    request = RequestFactory().get("api/v1/engagement")
    view = EngagementViewSet.as_view({'get': 'retrieve'})
    engagement = EngagementFactory()
    response = view(request, pk=engagement.pk)
    assert response.status_code == status.HTTP_200_OK
