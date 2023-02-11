import pytest
from rest_framework import status
from django.test import RequestFactory, TestCase

from tests.factories import HourFactory
from Apres_Ski_API.views.hour import HourViewSet

class HourViewTests(TestCase):
  def test_hour_200_OK(self):
    request = RequestFactory().get("api/v1/hour")
    view = HourViewSet.as_view({'get': 'retrieve'})
    hour = HourFactory()
    response = view(request, pk=hour.pk)
    assert response.status_code == status.HTTP_200_OK
