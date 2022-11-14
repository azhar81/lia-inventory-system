import os

from django.db import models
from django.conf import settings
from rest_framework.exceptions import APIException

class AssetException(APIException):
  status_code = 400
  default_detail = 'Cannot inspect currently inspected asset.'
  default_code = 'asset_unavailable'

class Inspection(models.Model):
  asset = models.ForeignKey("assets.Asset", on_delete=models.CASCADE)
  photo = models.ImageField(upload_to='inspections/')
  description = models.TextField()
  broken = models.BooleanField(blank=True, default=False)
  date = models.DateField(auto_now_add=True)
  inspector = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    editable=False
    )
  ongoing = models.BooleanField(editable=False, blank=True, null=True, default=False)

  def delete_photo(self):
    self.photo.delete()

  def updateAssetStatus(self, status):
    self.asset.status = status
    self.asset.save()

  def closeInspection(self):
    self.updateAssetStatus(1)

    self.ongoing = False
    self.save()
    self.delete_photo()

  def save(self, *args, **kwargs):
    # update asset status on creation only
    if not self.pk:
      if self.asset.status == 2:
        raise AssetException()
      if self.broken:
        self.updateAssetStatus(2)
        self.ongoing = True
    super().save(*args, **kwargs)

  def delete(self, *args, **kwargs):
    self.delete_photo()
    self.updateAssetStatus(1)
    super().delete(*args, **kwargs)
