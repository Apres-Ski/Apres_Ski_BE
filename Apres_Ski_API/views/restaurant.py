from django.shortcuts import render
from rest_framework import viewsets

from Apres_Ski_API.models.restaurant import Restaurant
from Apres_Ski_API.serializers.restaurant import RestaurantSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
  queryset = Restaurant.objects.all()
  serializer_class = RestaurantSerializer