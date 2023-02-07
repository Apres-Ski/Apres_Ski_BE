from rest_framework import serializers
from Apres_Ski_API.models.engagement import Engagement

class EngagementSerializer(serializers.ModelSerializer):
  class Meta:
    model = Engagement
    fields = '__all__'