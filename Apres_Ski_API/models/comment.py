from django.db import models
from .restaurant import Restaurant
from .user import User

class Comment(models.Model):
  class Meta:
    app_label = 'Apres_Ski_API'

  comment = models.CharField(max_length=500)
  restaurant = models.ManyToManyField(Restaurant, related_name='comment')
  user = models.ManyToManyField(User)