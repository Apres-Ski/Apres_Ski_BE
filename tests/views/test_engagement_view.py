import json
import pytest
from django.test import RequestFactory, TestCase

from tests.factories import EngagementFactory, RestaurantFactory, UserFactory
from Apres_Ski_API.models.engagement import Engagement
from Apres_Ski_API.views.engagement import EngagementViewSet

class EngagementViewTests(TestCase):
  def test_engagement_200_OK(self):
    engagement = EngagementFactory()
    request = RequestFactory().get(f"api/v1/engagement/{engagement.pk}")
    view = EngagementViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=engagement.pk)
    assert response.status_code == 200
    assert response.data['id'] == engagement.id

  def test_engagement_get_all(self):
    EngagementFactory.create_batch(4)
    request = RequestFactory().get(f"api/v1/engagement/")
    view = EngagementViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data) == 4

  def test_engagement_post(self):
    restaurant_1 = RestaurantFactory()
    user_1 = UserFactory()
    engagement = {"vibe": "Lively", "rating": "4.5", "favorites": True,
                  "restaurant": f"{restaurant_1.pk}", "user": f"{user_1.pk }"}
    request = RequestFactory().post("api/v1/engagement/", engagement)
    view = EngagementViewSet.as_view({'post': 'create'})
    assert not Engagement.objects.exists()
    data = json.dumps(engagement)
    response = view(request, data)
    assert response.status_code == 201
    assert  Engagement.objects.count() == 1
    assert Engagement.objects.get(pk = Engagement.objects.last().pk).vibe == 'Lively'

  def test_engagement_delete(self):
    engagement = EngagementFactory()
    assert Engagement.objects.count() == 1
    request = RequestFactory().delete(f"api/v1/engagement/{engagement.pk}")
    view = EngagementViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=engagement.pk)
    assert not Engagement.objects.exists()
    assert response.status_code == 204

  def test_engagement_patch(self):
    engagement = EngagementFactory(vibe='Lively')
    engagement_update = { "data": { "type": "Engagement", "id": f"{engagement.pk}", "attributes": {"vibe": "Family Friendly"}}}
    data = json.dumps(engagement_update)
    request = RequestFactory().patch(f"api/v1/engagement/{engagement.pk}", data, content_type='application/vnd.api+json')
    view = EngagementViewSet.as_view({'patch': 'partial_update'})
    response = view(request, pk=engagement.pk)
    updated_engagement = Engagement.objects.get(pk = engagement.pk)
    assert updated_engagement.vibe == 'Family Friendly'
    assert response.status_code == 200

  def test_engagement_404(self):
    engagement = EngagementFactory()
    request = RequestFactory().get(f"api/v1/engagement/{engagement.pk + 1}")
    view = EngagementViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=engagement.pk + 1)
    assert response.status_code == 404

