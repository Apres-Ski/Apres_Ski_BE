from django.shortcuts import render
from rest_framework import viewsets

from Apres_Ski_API.models.happyhour import HappyHour
from Apres_Ski_API.serializers.happyhour import HappyHourSerializer

class HappyHourViewSet(viewsets.ModelViewSet):
  queryset = HappyHour.objects.all()
  serializer_class = HappyHourSerializer