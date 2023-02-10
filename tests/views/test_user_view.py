import json
import pytest
from rest_framework import status
from django.test import RequestFactory, TestCase, Client

from tests.factories import UserFactory
from Apres_Ski_API.models.user import User
from Apres_Ski_API.views.user import UserViewSet

class UserViewTests(TestCase):
  def test_user_200_OK(self):
    request = RequestFactory().get("api/v1/user/")
    view = UserViewSet.as_view({'get': 'retrieve'})
    user = UserFactory()
    response = view(request, pk=user.pk)
    assert response.status_code == status.HTTP_200_OK

  def test_user_201_CREATE(self):
    user = { "name": "john", "lat": "lat", "lon": "lon" }
    request = RequestFactory().post("api/v1/user/", user)
    view = UserViewSet.as_view({'post': 'create'})
    assert not User.objects.exists()
    data = json.dumps(user)
    response = view(request, data)
    assert response.status_code == 201
    assert User.objects.count() == 1

  # def test_user_204_NO_CONTENT(self):
  #   user = UserFactory()
  #   assert User.objects.count() == 1
  #   request = RequestFactory().delete("api/v1/user/", kwargs={'pk': user.id})
  #   view = UserViewSet.as_view({'delete': 'destroy'})
  #   data = json.dumps(user)
  #   response = view(request, data)
  #   assert not User.objects.exists()
  #   assert response.status_code == 204

  def test_user_404_NOT_FOUND(self):
    request = RequestFactory().get("api/v1/user/10")
    view = UserViewSet.as_view({'get': 'retrieve'})
    user = UserFactory()
    response = view(request, pk=user.pk + 1)
    assert response.status_code == 404


# {
#     'get': 'retrieve',
#     'get': 'list',
#     'post': 'create',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# }