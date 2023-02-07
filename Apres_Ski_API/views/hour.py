from django.shortcuts import render
from rest_framework import viewsets

from Apres_Ski_API.models.hour import Hour
from Apres_Ski_API.serializers.hour import HourSerializer

class HourViewSet(viewsets.ModelViewSet):
  queryset = Hour.objects.all()
  serializer_class = HourSerializer