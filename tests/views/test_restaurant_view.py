import pytest
from rest_framework import status
from django.test import RequestFactory, TestCase

from tests.factories import RestaurantFactory
from Apres_Ski_API.views.restaurant import RestaurantViewSet

# @pytest.mark.django_db
class RestaurantViewTests(TestCase):
  def test_restaurant_200_OK(self):
    request = RequestFactory().get("api/v1/restaurant")
    view = RestaurantViewSet.as_view({'get': 'retrieve'})
    restaurant = RestaurantFactory()
    response = view(request, pk=restaurant.pk)
    # import ipdb; ipdb.set_trace()
    assert response.status_code == status.HTTP_200_OK

  # def test_restaurant_201_created(self):
  #   request = RequestFactory().post("api/v1/restaurant")
  #   view = RestaurantViewSet.as_view({'post': 'create'})
  #   payload =
  #   response = view(request, pk=restaurant.pk)
    # import ipdb; ipdb.set_trace()
    # assert response.status_code == status.HTTP_200_OK

  # Sad path test? How do I get a 404?
  # def test_restaurant_404_Not_Found(self):
  #   request = RequestFactory().get("api/v1/restaurant")
  #   view = RestaurantViewSet.as_view({'get': 'retrieve'})
  #   restaurant = RestaurantFactory()
  #   response = view(request, pk=restaurant.pk)
  #   assert response.status_code == status.HTTP_200_OK




# {
#     'get': 'retrieve',
#     'get': 'list',
#     'post': 'create',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# }