import json
import pytest
from django.test import RequestFactory, TestCase

from tests.factories import RestaurantFactory
from Apres_Ski_API.models.restaurant import Restaurant
from Apres_Ski_API.views.restaurant import RestaurantViewSet

class RestaurantViewTests(TestCase):
  def test_restaurant_200_OK(self):
    restaurant = RestaurantFactory()
    request = RequestFactory().get(f"api/v1/restaurant/{restaurant.pk}")
    view = RestaurantViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=restaurant.pk)
    assert response.status_code == 200

  def test_restaurant_get_all(self):
    RestaurantFactory.create_batch(4)
    request = RequestFactory().get(f"api/v1/restaurant/")
    view = RestaurantViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data) == 4

  def test_commment_post(self):
    # restaurant_1 = RestaurantFactory()
    restaurant = {"name":'name 1',
                  "address":'address',
                  "food_type":'food_type',
                  "cost":'cost',
                  "cover_img":'cover_img',
                  "alt_text":'alt_text',
                  "lat":'lat',
                  "lon":'lon',
                  "alcoholic_drinks":True,
                  "has_happy_hour":True}
    request = RequestFactory().post("api/v1/restaurant/", restaurant)
    view = RestaurantViewSet.as_view({'post': 'create'})
    assert not Restaurant.objects.exists()
    data = json.dumps(restaurant)
    response = view(request, data)
    assert response.status_code == 201
    assert Restaurant.objects.count() == 1
    assert Restaurant.objects.get(pk=1).name == "name 1"

  def test_restaurant_delete(self):
    restaurant = RestaurantFactory()
    assert Restaurant.objects.count() == 1
    request = RequestFactory().delete(f"api/v1/restaurant/{restaurant.pk}")
    view = RestaurantViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=restaurant.pk)
    assert not Restaurant.objects.exists()
    assert response.status_code == 204

  def test_restaurant_patch(self):
    restaurant = RestaurantFactory()
    restaurant_update = {"data": {"type": "restaurant",
                               "id": f"{restaurant.pk}", "attributes": {"name": "correct name"}}}
    data = json.dumps(restaurant_update)
    request = RequestFactory().patch(
        f"api/v1/restaurant/{restaurant.pk}", data, content_type='application/vnd.api+json')
    view = RestaurantViewSet.as_view({'patch': 'partial_update'})
    response = view(request, pk=restaurant.pk)
    updated_restaurant = Restaurant.objects.get(pk=restaurant.pk)
    assert updated_restaurant.name == "correct name"
    assert response.status_code == 200

  def test_user_404(self):
    restaurant = RestaurantFactory()
    request = RequestFactory().get(f"api/v1/restaurant/{restaurant.pk + 1}")
    view = RestaurantViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=restaurant.pk + 1)
    assert response.status_code == 404
