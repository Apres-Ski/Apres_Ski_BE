from rest_framework import serializers
from Apres_Ski_API.models.happyhour import HappyHour

class HappyHourSerializer(serializers.ModelSerializer):
  class Meta:
    model = HappyHour
    fields = '__all__'