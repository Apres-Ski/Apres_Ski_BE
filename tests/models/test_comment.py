import pytest
from django.test import TestCase
from Apres_Ski_API.models import Comment, Restaurant, User
from tests.factories import CommentFactory, RestaurantFactory, UserFactory


class CommentTests(TestCase):
  def setUp(self):
    self.restaurant_1 = RestaurantFactory()
    self.user_1 = UserFactory()
    self.comment = CommentFactory(comment="This is a comment")
    self.comment.restaurant.set([self.restaurant_1.pk])
    self.comment.user.set([self.user_1.pk])

  def test_comment_instance(self):
    assert isinstance(self.comment, Comment)

  def test_comment_state(self):
    assert self.comment.comment == "This is a comment"
    assert self.comment.restaurant.count() == 1
    assert self.comment.user.count() == 1
