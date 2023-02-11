import pytest
from django.test import RequestFactory, TestCase

from tests.factories import HappyHourFactory
from Apres_Ski_API.views.happyhour import HappyHourViewSet

class HappyHourViewTests(TestCase):
  def test_hour_200_OK(self):
    request = RequestFactory().get("api/v1/happy_hour")
    view = HappyHourViewSet.as_view({'get': 'retrieve'})
    happy_hour = HappyHourFactory()
    response = view(request, pk=happy_hour.pk)
    assert response.status_code == 200
