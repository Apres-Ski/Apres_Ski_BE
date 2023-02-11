import pytest
import json
from django.test import RequestFactory, TestCase, Client

# from tests.factories import UserFactory
# from Apres_Ski_API.models.user import User
from Apres_Ski_API.views.routing import RoutingViewSet

class UserViewTests(TestCase):
  def test_routing_get(self):
    data = {
      "user_lat": 39.47677682,
      "user_lon": -106.0476996,
      "rest_lat": 39.475289,
      "rest_lon": -106.0524277
    }
    client = Client()
    response = client.get("/api/v1/routing/", data)
    import ipdb; ipdb.set_trace()
    # view = UserViewSet.as_view({'get': 'retrieve'})
    # response = view(request)
    # content = json.loads(response.content)
    # assert response.status_code == 200
    # assert response.data['id'] == user.id