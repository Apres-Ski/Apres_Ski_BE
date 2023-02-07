from django.db import models

class User(models.Model):
  class Meta:
    app_label = 'Apres_Ski_API'

  name = models.CharField(max_length=60)