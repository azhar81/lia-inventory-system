from django.contrib.auth.models import User
from django.test import TestCase

def create_user():
  data = {
    'username': 'TestUser',
    'password': 'TestPassword'
  }

  user = User.objects.create_user(**data)
  return user