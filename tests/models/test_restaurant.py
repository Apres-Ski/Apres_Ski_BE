import pytest
from django.test import TestCase
from Apres_Ski_API.models.restaurant import restaurant
from tests.factories import RestaurantFactory

class RestaurantTests(TestCase): 
    def setUp(self): 
        self.restaurant = RestaurantFactory(name="name",
                                            address='address',
                                            food_type='food_type',
                                            cost='cost',
                                            vibe='vibe',
                                            cover_img='cover_img',
                                            alt_text='alt_text',
                                            lat='lat',
                                            lon='lon',
                                            alcoholic_drinks='alcoholic_drinks',
                                            has_happy_hour='has_happy_hour')