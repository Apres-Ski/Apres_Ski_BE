import pytest
from django.test import RequestFactory, TestCase

from tests.factories import PhotoFactory
from Apres_Ski_API.views.photo import PhotoViewSet

class PhotoViewTests(TestCase):
  def test_photo_200_OK(self):
    request = RequestFactory().get("api/v1/photo")
    view = PhotoViewSet.as_view({'get': 'retrieve'})
    photo = PhotoFactory()
    response = view(request, pk=photo.pk)
    assert response.status_code == 200
