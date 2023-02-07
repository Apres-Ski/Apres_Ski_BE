from django.shortcuts import render
from rest_framework import viewsets

from Apres_Ski_API.models.engagement import Engagement
from Apres_Ski_API.serializers.engagement import EngagementSerializer

class EngagementViewSet(viewsets.ModelViewSet):
  queryset = Engagement.objects.all()
  serializer_class = EngagementSerializer