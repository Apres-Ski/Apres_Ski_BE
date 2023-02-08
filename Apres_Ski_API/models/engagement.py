from django.db import models
from .restaurant import Restaurant
from .user import User

class Engagement(models.Model):
  from .restaurant import Restaurant
  class Meta:
    app_label = 'Apres_Ski_API'

  vibe = models.CharField(max_length=200)
  rating = models.CharField(max_length=200)
  favorites = models.BooleanField()
  restaurant = models.ManyToManyField(Restaurant, related_name='engagement')
  user = models.ManyToManyField(User)