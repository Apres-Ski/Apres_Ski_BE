from django.shortcuts import render
from rest_framework import viewsets

from Apres_Ski_API.models.photo import Photo
from Apres_Ski_API.serializers.photo import PhotoSerializer

class PhotoViewSet(viewsets.ModelViewSet):
  queryset = Photo.objects.all()
  serializer_class = PhotoSerializer