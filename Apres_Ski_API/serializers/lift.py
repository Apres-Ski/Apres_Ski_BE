from rest_framework import serializers
from Apres_Ski_API.models.lift import Lift

class LiftSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lift
    fields = '__all__'