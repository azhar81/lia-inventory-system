from django.test import TestCase
from locations.models import Location

def create_location():
  data = {
    'branch' : 'Main',
    'floor': '1',
    'room': '1101'
  }
  return Location.objects.create(**data)
