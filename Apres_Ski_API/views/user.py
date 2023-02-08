from django.shortcuts import render
from rest_framework import viewsets

from Apres_Ski_API.models.user import User
from Apres_Ski_API.serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer