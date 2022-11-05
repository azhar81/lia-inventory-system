from django.db import models
from assets.models import Asset

BRANCH = [
  ('CKL','Cikokol'),
  ('TGR', 'Tanggerang'),
  ('BSD', 'BSD')
]

class Location(models.Model):
  branch = models.CharField(choices=BRANCH, max_length=3)
  floor = models.CharField(max_length=2)
  room = models.CharField(max_length=10)

  def __str__(self):
      return f'{self.branch}-{self.floor}-{self.room}'

  def get_assets_in_branch(self):
    return Asset.objects.filter(location__branch=self.branch)

  def get_assets_in_floor(self):
    return Asset.objects.filter(location__branch=self.branch,
                                location__floor=self.floor)

  def get_assets_in_room(self):
    return Asset.objects.filter(location = self.id)
