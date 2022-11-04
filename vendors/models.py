from django.db import models

class Vendor(models.Model):
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=20, unique=True)
  address = models.TextField(blank=True, default='')
  description = models.TextField(blank=True, default='')
