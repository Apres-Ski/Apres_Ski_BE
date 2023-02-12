import pytest
from django.test import RequestFactory, TestCase

from tests.factories import LiftFactory
from Apres_Ski_API.views.lift import LiftViewSet

class LiftViewTests(TestCase):
  def test_lift_200_OK(self):
    lift = LiftFactory()
    request = RequestFactory().get(f"api/v1/lift/{lift.pk}")
    view = LiftViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=lift.pk)
    assert response.status_code == 200
    assert response.data['id'] == lift.id

  def test_lift_get_all(self):
    LiftFactory.create_batch(3)
    request = RequestFactory().get(f"api/v1/lift/")
    view = LiftViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data) == 3

  def test_lift_post(self):
    lift = {"name": "lift_1", "lat": "lat", "lon": "lon"}
    request = RequestFactory().post("api/v1/lift/", lift)
    view = LiftViewSet.as_view({'post': 'create'})
    assert not Lift.objects.exists()
    data = json.dumps(lift)
    response = view(request, data)
    assert response.status_code == 201
    assert Lift.objects.count() == 1
    assert Lift.objects.get(pk=1).name == 'lift_1'

  def test_lift_delete(self):
    lift = LiftFactory()
    assert Lift.objects.count() == 1
    request = RequestFactory().delete(f"api/v1/lift/{lift.pk}")
    view = LiftViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=lift.pk)
    assert not Lift.objects.exists()
    assert response.status_code == 204

  def test_lift_patch(self):
    lift = LiftFactory(name='paul')
    lift_update = {"data": {"type": "lift",
                            "id": f"{lift.pk}", "attributes": {"name": "john"}}}
    data = json.dumps(lift_update)
    request = RequestFactory().patch(
        f"api/v1/lift/{lift.pk}", data, content_type='application/vnd.api+json')
    view = liftViewSet.as_view({'patch': 'partial_update'})
    response = view(request, pk=lift.pk)
    updated_lift = lift.objects.get(pk=lift.pk)
    assert updated_lift.name == 'lift_1'= 200

  def test_lift_404(self):
    lift = LiftFactory()
    request = RequestFactory().get(f"api/v1/lift/{lift.pk + 1}")
    view = LiftViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=lift.pk + 1)
    assert response.status_code == 404
