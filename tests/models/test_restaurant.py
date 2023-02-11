import pytest
from django.test import TestCase
from Apres_Ski_API.models.restaurant import Restaurant
from tests.factories import RestaurantFactory

class RestaurantTests(TestCase): 
  def setUp(self): 
      self.restaurant = RestaurantFactory(name='name',
                                          address='address',
                                          food_type='food_type',
                                          cost='cost',                               
                                          cover_img='cover_img',
                                          alt_text='alt_text',
                                          lat='lat',
                                          lon='lon',
                                          alcoholic_drinks=True,
                                          has_happy_hour=True)
  
  def test_restaurant_instance(self):
     assert isinstance(self.restaurant, Restaurant)
  
  def test_restaurant_state(self):
     assert self.restaurant.name == 'name'
     assert self.restaurant.address == 'address'
     assert self.restaurant.food_type == 'food_type'
     assert self.restaurant.cover_img == 'cover_img'
     assert self.restaurant.alt_text == 'alt_text'
     assert self.restaurant.lat == 'lat'
     assert self.restaurant.lon == 'lon'
     assert self.restaurant.alcoholic_drinks == True
     assert self.restaurant.has_happy_hour == True