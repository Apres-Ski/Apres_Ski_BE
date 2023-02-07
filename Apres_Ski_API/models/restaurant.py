from django.db import models

class Restaurant(models.Model):
  class Meta:
    app_label = 'Apres_Ski_API'

  name = models.CharField(max_length=60, unique=True)
  address = models.CharField(max_length=200, unique=True)
  food_type = models.CharField(max_length=200)
  cost = models.CharField(max_length=200)
  vibe = models.CharField(max_length=200)
  cover_img = models.CharField(max_length=200, unique=True)
  alt_text = models.CharField(max_length=200)
  lat = models.CharField(max_length=60)
  lon = models.CharField(max_length=60)
  alcoholic_drinks = models.BooleanField()
  has_happy_hour = models.BooleanField()