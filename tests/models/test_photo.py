import pytest
from django.test import TestCase
from Apres_Ski_API.models import Photo, Restaurant
from tests.factories import PhotoFactory, RestaurantFactory


class PhotoTests(TestCase):
  def setUp(self):
    self.restaurant_1 = RestaurantFactory()
    self.photo = PhotoFactory(url="example_bar.com",
                              alt_text="interior bar",
                              restaurant=self.restaurant_1)

  def test_photo_instance(self):
    assert isinstance(self.photo, Photo)

  def test_photo_state(self):
    assert self.photo.url == "example_bar.com"
    assert self.photo.alt_text == "interior bar"
    assert self.photo.restaurant == self.restaurant_1
