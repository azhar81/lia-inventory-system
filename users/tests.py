from django.contrib.auth.models import User
from django.test import TestCase

def create_user():
  data = {
    'username': 'TestUser',
    'password': 'TestPassword'
  }

  user = User.objects.create_user(**data)
  return user

def create_user_with_username(username):
  data = {
    'username': username,
    'password': 'TestPassword'
  }

  user = User.objects.create_user(**data)
  return user
