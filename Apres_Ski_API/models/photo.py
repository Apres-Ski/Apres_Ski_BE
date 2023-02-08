from django.db import models
from .restaurant import Restaurant

class Photo(models.Model):
  class Meta:
    app_label = 'Apres_Ski_API'

  url = models.CharField(max_length=500, unique=True)
  alt_text = models.CharField(max_length=100)
  restaurant = models.ForeignKey(Restaurant, related_name='photo', on_delete=models.CASCADE)