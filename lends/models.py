from datetime import date
from django.db import models
from django.conf import settings
from assets.models import Asset

STATUS = [
  (1, 'Berjalan'),
  (2, 'Ditutup')
]

class Lend(models.Model):
  asset = models.ForeignKey("assets.Asset", on_delete=models.CASCADE)
  borrowerName = models.CharField(max_length=50)
  dateBorrow = models.DateField(auto_now_add=True)
  dateReturn = models.DateField(blank=True, null=True)
  assetReceiver = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    blank=True,
    null=True
  )
  status = models.IntegerField(choices=STATUS, default=1)

  def updateAssetStatus(self, status):
    self.asset.status = status
    self.asset.save()

  def returnAsset(self, request):
    self.updateAssetStatus(1)
    self.dateReturn = date.today()
    self.assetReceiver = request.user
    self.status = 2
    self.save()
