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

def create_user_with_username_first_last_name(username, first_name, last_name):
  data = {
    'username': username,
    'first_name': first_name,
    'last_name': last_name,
    'password': 'TestPassword'
  }

  user = User.objects.create_user(**data)
  return user
