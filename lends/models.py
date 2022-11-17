from datetime import date
from django.db import models
from django.conf import settings
from assets.models import Asset, AssetException

STATUS = [
  (1, 'Berjalan'),
  (2, 'Ditutup')
]

class Lend(models.Model):
  asset = models.ForeignKey("assets.DynamicAsset", on_delete=models.CASCADE)
  borrowerName = models.CharField(max_length=50)
  dateBorrow = models.DateField(auto_now_add=True)
  dateReturn = models.DateField(blank=True, null=True, editable=False)
  assetReceiver = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    blank=True,
    null=True,
    editable=False
  )
  status = models.IntegerField(choices=STATUS, default=1, editable=False)

  def updateAssetStatus(self, status):
    self.asset.status = status
    self.asset.save()

  def returnAsset(self, request):
    self.updateAssetStatus(1)
    self.dateReturn = date.today()
    self.assetReceiver = request.user
    self.status = 2
    self.save()

  def delete(self, *args, **kwargs):
    self.updateAssetStatus(1)
    super().delete(*args, **kwargs)
    
  def save(self, *args, **kwargs):
    # update asset status on creation only
    if not self.pk:
      if self.asset.status != 1:
        raise AssetException(f"Asset saat ini sedang dalam proses `{self.asset.get_status_display()}`.")

      self.updateAssetStatus(4)
      self.status = 1
    super().save(*args, **kwargs)
