from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Employee(models.Model):
  JANITOR = 'Janitor'
  TECHNICIAN = 'Technician'
  ADMIN = 'Admin'
  ROLE = [
    (JANITOR, JANITOR),
    (TECHNICIAN, TECHNICIAN),
    (ADMIN, ADMIN)
  ]
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(max_length=10,
                          choices=ROLE,
                          default=JANITOR)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.employee.save()