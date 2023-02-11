import pytest
from django.test import TestCase
from Apres_Ski_API.models.lift import Lift
from tests.factories import LiftFactory


class LiftTests(TestCase):
  def setUp(self):
    self.lift = LiftFactory(name="name",
                            lat='lat',
                            lon='lon')

  def test_lift_instance(self):
    assert isinstance(self.userlift, Lift)

  def test_lift_state(self):
  assert self.lift.name == "name"
  assert self.lift.lat == "lat"
  assert self.lift.lon == "lon"
