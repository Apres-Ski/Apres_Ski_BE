import pytest
from rest_framework import status
from django.test import RequestFactory, TestCase

from tests.factories import LiftFactory
from Apres_Ski_API.views.lift import LiftViewSet

class LiftViewTests(TestCase):
  def test_lift_200_OK(self):
    request = RequestFactory().get("api/v1/lift")
    view = LiftViewSet.as_view({'get': 'retrieve'})
    lift = LiftFactory()
    response = view(request, pk=lift.pk)
    assert response.status_code == status.HTTP_200_OK
