from django.shortcuts import render
from rest_framework import viewsets

from Apres_Ski_API.models.lift import Lift
from Apres_Ski_API.serializers.lift import LiftSerializer

class LiftViewSet(viewsets.ModelViewSet):
  queryset = Lift.objects.all()
  serializer_class = LiftSerializer