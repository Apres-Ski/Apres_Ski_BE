import pytest
from django.test import TestCase
from Apres_Ski_API.models.user import User
from tests.factories import UserFactory

class UserTests(TestCase):
  def setUp(self):
    self.user = UserFactory(name='name',
                            lat='lat',
                            lon='lon')

  def test_user_instance(self):
    assert isinstance(self.user, User)

  def test_user_state(self):
    assert self.user.name == "name"
    assert self.user.lat == "lat"
    assert self.user.lon == "lon"
