from django.test import TestCase
from assets.models import Asset
from vendors.tests import create_vendor
from locations.tests import create_location

def get_asset(id):
  return Asset.objects.get(id=id)

def create_asset():
  vendor = create_vendor()
  location = create_location()
  data = {
    'name': 'Asset Main',
    'price':'500000',
    'vendor': vendor,
    'location': location,
    'warrantyYears': 2,
    'usefulLife': 10
  }

  return Asset.objects.create(**data)
