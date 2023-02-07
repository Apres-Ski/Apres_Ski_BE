from rest_framework import serializers
from Apres_Ski_API.models.user import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'