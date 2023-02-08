from rest_framework import serializers
from Apres_Ski_API.models.hour import Hour

class HourSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hour
    fields = '__all__'