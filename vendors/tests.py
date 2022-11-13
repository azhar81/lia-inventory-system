from django.test import TestCase
from vendors.models import Vendor

def create_vendor():
  data = {
    'name' : 'Vendor Main',
    'phone': '500505'
  }
  return Vendor.objects.create(**data)
