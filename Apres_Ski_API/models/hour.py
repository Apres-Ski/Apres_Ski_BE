from django.db import models
from .restaurant import Restaurant

class Hour(models.Model):
  class Meta:
    app_label = 'Apres_Ski_API'

  sunday = models.CharField(max_length=60, null=True)
  monday = models.CharField(max_length=60, null=True)
  tuesday = models.CharField(max_length=60, null=True)
  wednesday = models.CharField(max_length=60, null=True)
  thursday = models.CharField(max_length=60, null=True)
  friday = models.CharField(max_length=60, null=True)
  saturday = models.CharField(max_length=60, null=True)
  restaurant = models.ForeignKey(Restaurant, related_name='hour', on_delete=models.CASCADE)