import pytest
from django.test import RequestFactory, TestCase

from tests.factories import RestaurantFactory
from Apres_Ski_API.views.restaurant import RestaurantViewSet

class RestaurantViewTests(TestCase):
  def test_restaurant_200_OK(self):
    request = RequestFactory().get("api/v1/restaurant")
    view = RestaurantViewSet.as_view({'get': 'retrieve'})
    restaurant = RestaurantFactory()
    response = view(request, pk=restaurant.pk)
    assert response.status_code == 200
