from rest_framework import serializers
from Apres_Ski_API.models.photo import Photo

class PhotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Photo
    fields = '__all__'