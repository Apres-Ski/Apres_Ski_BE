from django.shortcuts import render
from rest_framework import viewsets

from Apres_Ski_API.models.comment import Comment
from Apres_Ski_API.serializers.comment import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer