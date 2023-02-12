import json
import pytest
from django.test import RequestFactory, TestCase

from tests.factories import HourFactory,RestaurantFactory
from Apres_Ski_API.models.hour import Hour
from Apres_Ski_API.views.hour import HourViewSet

class HourViewTests(TestCase):
  def test_hour_200_OK(self):
    hour = HourFactory()
    request = RequestFactory().get(f"api/v1/hour/{hour.pk}")
    view = HourViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=hour.pk)
    assert response.status_code == 200
    assert response.data['id'] == hour.id

  def test_hour_get_all(self):
    HourFactory.create_batch(4)
    request = RequestFactory().get(f"api/v1/hour/")
    view = HourViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data) == 4

  def test_hour_post(self):
    restaurant_1 = RestaurantFactory()
    
    hour = {"monday": "8:00 AM - 10:00 AM",
                  "restaurant": f"{restaurant_1.pk}"}
    request = RequestFactory().post("api/v1/hour/", hour)
    view = HourViewSet.as_view({'post': 'create'})
    assert not Hour.objects.exists()
    data = json.dumps(hour)
    response = view(request, data)
    assert response.status_code == 201
    assert  Hour.objects.count() == 1
    assert Hour.objects.get(pk = 1).monday == '8:00 AM - 10:00 AM'

  def test_hour_delete(self): 
    hour = HourFactory()
    assert Hour.objects.count() == 1
    request = RequestFactory().delete(f"api/v1/hour/{hour.pk}")
    view = HourViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=hour.pk)
    assert not Hour.objects.exists()
    assert response.status_code == 204

  def test_hour_patch(self):
    hour = HourFactory()
    hour_update = {"data": {"type": "Hour", "id": f"{hour.pk}",
                            "attributes": {"monday": '9:00 AM - 10:00 AM'}}}
    data = json.dumps(hour_update)
    request = RequestFactory().patch(f"api/v1/hour/{hour.pk}", data, content_type='application/vnd.api+json') 
    view = HourViewSet.as_view({'patch': 'partial_update'})
    response = view(request, pk=hour.pk)
    updated_hour = Hour.objects.get(pk = hour.pk)
    assert updated_hour.monday == '9:00 AM - 10:00 AM'
    assert response.status_code == 200

  def test_hour_404(self):
    hour = HourFactory()
    request = RequestFactory().get(f"api/v1/hour/{hour.pk + 1}")
    view = HourViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=hour.pk + 1)
    assert response.status_code == 404
