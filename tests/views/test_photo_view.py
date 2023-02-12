import json
import pytest
from django.test import RequestFactory, TestCase

from tests.factories import PhotoFactory, RestaurantFactory
from Apres_Ski_API.models.photo import Photo
from Apres_Ski_API.views.photo import PhotoViewSet


class PhotoViewTests(TestCase):
  def test_photo_200_OK(self):
    photo = PhotoFactory()
    request = RequestFactory().get(f"api/v1/photo/{photo.pk}")
    view = PhotoViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=photo.pk)
    assert response.status_code == 200

  def test_photo_get_all(self):
    PhotoFactory.create_batch(4)
    request = RequestFactory().get(f"api/v1/photo/")
    view = PhotoViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data) == 4

  def test_photo_post(self):
    restaurant_1 = RestaurantFactory()
    photo = {"url": "photo.com", "alt_text": "photo text",
                  "restaurant": f"{restaurant_1.pk}"}
    request = RequestFactory().post("api/v1/photo/", photo)
    view = PhotoViewSet.as_view({'post': 'create'})
    assert not Photo.objects.exists()
    data = json.dumps(photo)
    response = view(request, data)
    assert response.status_code == 201
    assert Photo.objects.count() == 1
    assert Photo.objects.get(pk=1).url == "photo.com"

  def test_photo_delete(self):
    photo = PhotoFactory()
    assert Photo.objects.count() == 1
    request = RequestFactory().delete(f"api/v1/photo/{photo.pk}")
    view = PhotoViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=photo.pk)
    assert not Photo.objects.exists()
    assert response.status_code == 204

  def test_photo_patch(self):
    photo = PhotoFactory()
    photo_update = {"data": {"type": "Photo",
                                  "id": f"{photo.pk}", "attributes": {"url": "url_2.com"}}}
    data = json.dumps(photo_update)
    request = RequestFactory().patch(
        f"api/v1/photo/{photo.pk}", data, content_type='application/vnd.api+json')
    view = PhotoViewSet.as_view({'patch': 'partial_update'})
    response = view(request, pk=photo.pk)
    updated_photo = Photo.objects.get(pk=photo.pk)
    assert updated_photo.url == "url_2.com"
    assert response.status_code == 200

  def test_photo_404(self):
    photo = PhotoFactory()
    request = RequestFactory().get(f"api/v1/photo/{photo.pk + 1}")
    view = PhotoViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=photo.pk + 1)
    assert response.status_code == 404
