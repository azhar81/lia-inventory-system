from datetime import date

from django.test import TestCase
from rest_framework.test import APIClient
from users.tests import create_user_with_username, \
  create_user_with_username_first_last_name
from assets.tests import create_asset, get_asset
from inspections.tests import create_inspection

from maintenances.models import Maintenance

def get_maintenance(id):
  return Maintenance.objects.get(id=id)

class MaintenanceTest(TestCase):
  def create_maintenance(self):
    data = {
      'inspection': self.inspection.id,
      'description': 'desc',
      'cost': 200000,
    }
    response = self.client.post(
      "/maintenances/",
      data=data,
      format='json'
    )
    instance = get_maintenance(id=response.json()['id'])
    return response, instance

  def setUp(self):
    self.user = create_user_with_username_first_last_name(
      'maintenancestaff', 'Maintenance', 'Staff'
      )
    self.asset = create_asset()
    self.client = APIClient()
    self.inspection = create_inspection(True, self.asset, user=self.user)
    self.inspection.delete_photo()
    self.client.login(username='maintenancestaff', password='TestPassword')

  def test_create_maintenance(self):
    self.assertEqual(Maintenance.objects.all().count(), 0)
    response, _ = self.create_maintenance()
    self.assertEqual(response.status_code, 201)
    self.assertEqual(Maintenance.objects.all().count(), 1)
    
  def test_staffName_set_on_create(self):
    _, instance = self.create_maintenance()
    self.assertEqual(instance.staffName, f"{self.user.first_name} {self.user.last_name}")

  def test_asset_set_on_create(self):
    _, instance = self.create_maintenance()
    self.assertEqual(instance.asset, self.asset)

  def test_assetWorth_set_on_create(self):
    _, instance = self.create_maintenance()
    self.assertEqual(instance.assetWorth, self.asset.get_depreciated_value())

  def test_changes_on_approval(self):
    self.create_maintenance()
    response = self.client.get(
      "/maintenances/1/approve"
    )
    self.assertEqual(response.status_code, 200)

    instance = get_maintenance(response.json()['id'])
    self.assertEqual(instance.dateStart, date.today())
    self.assertTrue(instance.maintain)

    self.assertEqual(instance.asset.status, 3)

  def test_changes_on_rejection(self):
    self.create_maintenance()
    response = self.client.get(
      "/maintenances/1/reject"
    )
    self.assertEqual(response.status_code, 200)

    instance = get_maintenance(response.json()['id'])
    self.assertFalse(instance.maintain)

    self.assertEqual(instance.asset.status, 5)

  def test_can_not_finish_asset_not_marked_to_be_maintained(self):
    self.create_maintenance()
    response = self.client.get(
      "/maintenances/1/finish"
    )
    self.assertEqual(response.status_code, 400)

    asset = get_asset(id=self.asset.id)
    self.assertNotEqual(asset.status, 1)

  def test_can_not_finish_asset_marked_to_be_rejected(self):
    self.create_maintenance()
    self.client.get(
      "/maintenances/1/reject"
    )
    response = self.client.get(
      "/maintenances/1/finish"
    )
    self.assertEqual(response.status_code, 400)

    asset = get_asset(id=self.asset.id)
    self.assertNotEqual(asset.status, 1)

  def test_can_finish_asset_marked_to_be_approved(self):
    self.create_maintenance()
    self.client.get(
      "/maintenances/1/approve"
    )
    response = self.client.get(
      "/maintenances/1/finish"
    )
    self.assertEqual(response.status_code, 200)

    asset = get_asset(id=self.asset.id)
    self.assertEqual(asset.status, 1)
