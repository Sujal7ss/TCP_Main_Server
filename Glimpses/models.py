from django.db import models
from decouple import config

#Model for glimpses
class Glimpse(models.Model):
    
    year = models.CharField(max_length=5)
    img = models.ImageField(upload_to="static/uploads/glimpses/", null = True, blank=True)