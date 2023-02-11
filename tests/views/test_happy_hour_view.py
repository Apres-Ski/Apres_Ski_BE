import json
import pytest
from django.test import RequestFactory, TestCase

from tests.factories import HappyHourFactory, RestaurantFactory
from Apres_Ski_API.models.happyhour import HappyHour
from Apres_Ski_API.views.happyhour import HappyHourViewSet

class HappyHourViewTests(TestCase):
  def test_hour_200_OK(self):
    happyhour = HappyHourFactory()
    request = RequestFactory().get("api/v1/happyhour/{happyhour.pk}")
    view = HappyHourViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=happyhour.pk)
    assert response.status_code == 200
    assert response.data['id'] == happyhour.id

  def test_happyhour_get_all(self):
    HappyHourFactory.create_batch(4)
    request = RequestFactory().get(f"api/v1/happyhour/")
    view = HappyHourViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data) == 4

  def test_happyhour_post(self):
    restaurant_1 = RestaurantFactory()
    happyhour={"monday": "2:00 PM - 6:00 PM",
              "restaurant": f"{restaurant_1.pk}"}
    request = RequestFactory().post("api/v1/happyhour/", happyhour)
    view = HappyHourViewSet.as_view({'post': 'create'})
    assert not HappyHour.objects.exists()
    data = json.dumps(happyhour)
    response = view(request, data)
    assert response.status_code == 201
    assert HappyHour.objects.count() == 1
    assert HappyHour.objects.get(pk=1).monday
