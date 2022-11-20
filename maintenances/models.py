from django.db import models
from django.conf import settings
from datetime import date

CHOICES = (
  (1, 'Approved'),
  (0, 'Rejected'),
  (2, 'Waiting for approval'),
)

class Maintenance(models.Model):
  inspection = models.ForeignKey(
    "inspections.Inspection",
    models.SET_NULL,
    blank=True,
    null=True,
    )
  asset = models.ForeignKey(
    "assets.Asset",
    on_delete=models.CASCADE,
    editable=False,
    )
  assetWorth = models.FloatField(editable=False)
  description = models.TextField()
  cost = models.FloatField()
  date = models.DateField(auto_now_add=True)
  dateStart = models.DateField(editable=False, null=True)
  dateFinished = models.DateField(editable=False, null=True)
  staff = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    models.SET_NULL,
    blank=True,
    null=True,
    editable=False
    )
  staffName = models.CharField(
    max_length=50,
    editable=False
    )
  maintain = models.BooleanField(
    editable=False,
    null=True
  )

  def updateAssetStatus(self, status):
    self.asset.status = status
    self.asset.save()

  def save(self, *args, **kwargs):
    # update maintenance details on creation only
    if not self.pk:
      self.asset = self.inspection.asset
      self.assetWorth = self.asset.get_depreciated_value()
      self.staffName = f'{self.staff.first_name} {self.staff.last_name}'
    super().save(*args, **kwargs)

  def approve(self):
    self.updateAssetStatus(3)
    self.dateStart = date.today()
    self.maintain = True
    self.save()

  def reject(self):
    self.updateAssetStatus(5)
    self.maintain = False
    self.save()

  def finish(self):
    self.updateAssetStatus(1)
    self.dateFinished = date.today()
    self.save()
