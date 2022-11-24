from django.db import models
from datetime import date
from rest_framework.exceptions import APIException
from polymorphic.models import PolymorphicModel

class AssetException(APIException):
  status_code = 400
  default_detail = 'Asset not available to be processed.'
  default_code = 'asset_unavailable'

STATUS = [
  (1, 'Normal'),
  (2, 'Perlu diperiksa'),
  (3, 'Diperbaiki'),
  (4, 'Dipinjam'),
  (5, 'Rusak')
]

class Asset(PolymorphicModel):
  name = models.CharField(max_length=100)
  status = models.IntegerField(choices=STATUS, default=1, editable=False)
  merk = models.CharField(max_length=100, blank=True)
  vendor = models.ForeignKey('vendors.Vendor', on_delete=models.RESTRICT, blank=True, null=True)
  location = models.ForeignKey('locations.Location', on_delete=models.RESTRICT)
  price = models.FloatField()
  datePurchased = models.DateField(default = date.today)
  warrantyYears = models.IntegerField()
  usefulLife = models.IntegerField()
  lastInspection = models.DateField(editable=False, auto_now_add=True)

  def get_depreciated_value(self):
    currTime = date.today()
    yearDiff = currTime.year - self.datePurchased.year

    if yearDiff < self.warrantyYears:
      return self.price

    monthDiff = currTime.month - self.datePurchased.month
    assetAgeInMonths = (yearDiff*12) + monthDiff
    usefulLifeInMonths = self.usefulLife * 12

    monthlyDepreciation = self.price / usefulLifeInMonths

    return self.price - (monthlyDepreciation * assetAgeInMonths)

  def update_last_inspect(self):
    self.lastInspection = date.today()
    self.save()

  def __str__(self):
      return f'{self.name}-{self.id}/{self.datePurchased}'

class StaticAsset(Asset):
  pass

class DynamicAsset(Asset):
  pass
