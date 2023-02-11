import pytest
from django.test import TestCase
from Apres_Ski_API.models import Hour, Restaurant
from tests.factories import HourFactory, RestaurantFactory


class HourTests(TestCase):
  def setUp(self):
    self.restaurant_1 = RestaurantFactory()
    self.hour = HourFactory(sunday='sunday',
                            monday='monday',
                            tuesday='tuesday',
                            wednesday='wednesday',
                            thursday='thursday',
                            friday='friday',
                            saturday='saturday',
                            restaurant=self.restaurant_1)

  def test_hour_instance(self):
    assert isinstance(self.hour, Hour)

  def test_hour_state(self):
    assert self.hour.sunday == 'sunday'
    assert self.hour.monday == 'monday'
    assert self.hour.tuesday == 'tuesday'
    assert self.hour.wednesday == 'wednesday'
    assert self.hour.thursday == 'thursday'
    assert self.hour.friday == 'friday'
    assert self.hour.saturday == 'saturday'
    assert self.hour.sunday == 'sunday'
    assert self.hour.restaurant == self.restaurant_1
