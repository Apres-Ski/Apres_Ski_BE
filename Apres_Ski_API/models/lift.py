from django.db import models

class Lift(models.Model):
  class Meta:
    app_label = 'Apres_Ski_API'

  name = models.CharField(max_length=60, unique=True)
  lat = models.CharField(max_length=60)
  lon = models.CharField(max_length=60)