import pytest
from django.test import TestCase
from Apres_Ski_API.models import Engagement, Restaurant, User
from tests.factories import EngagementFactory, RestaurantFactory, UserFactory


class EngagementTests(TestCase):
  def setUp(self):
    self.restaurant_1 = RestaurantFactory()
    self.user_1 = UserFactory()
    self.engagement = EngagementFactory(vibe="Lively",
                                        rating="4.5",
                                        favorites=False,
                                        restaurant= self.restaurant_1,
                                        user= self.user_1)

  def test_engagement_instance(self):
    assert isinstance(self.engagement, Engagement)

  def test_engagement_state(self):
    assert self.engagement.vibe == "Lively"
    assert self.engagement.rating == "4.5"
    assert self.engagement.favorites == False
    assert self.engagement.restaurant == self.restaurant_1
    assert self.engagement.user == self.user_1
