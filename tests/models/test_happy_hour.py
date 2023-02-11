import pytest
from django.test import TestCase
from Apres_Ski_API.models import HappyHour, Restaurant
from tests.factories import HappyHourFactory, RestaurantFactory


class HappyHourTests(TestCase):
  def setUp(self):
    self.restaurant_1 = RestaurantFactory()
    self.happyhour = HappyHourFactory(sunday='sunday',
                                      monday='monday',
                                      tuesday='tuesday',
                                      wednesday='wednesday',
                                      thursday='thursday',
                                      friday='friday',
                                      saturday='saturday',
                                      special='special',
                                      restaurant=self.restaurant_1)

  def test_hour_instance(self):
    assert isinstance(self.happyhour, HappyHour)

  def test_hour_state(self):
    assert self.happyhour.sunday == 'sunday'
    assert self.happyhour.monday == 'monday'
    assert self.happyhour.tuesday == 'tuesday'
    assert self.happyhour.wednesday == 'wednesday'
    assert self.happyhour.thursday == 'thursday'
    assert self.happyhour.friday == 'friday'
    assert self.happyhour.saturday == 'saturday'
    assert self.happyhour.sunday == 'sunday'
    assert self.happyhour.special == 'special'
    assert self.happyhour.restaurant == self.restaurant_1
