from django.test import TestCase
from rest_framework.test import APIClient
from users.tests import create_user
from assets.tests import create_asset, get_asset
from lends.models import Lend
from lends.serializers import LendSerializer

def create_lend(asset):
  data = {
    'asset': asset.id,
    'borrowerName': 'Borrower'
  }

  serializer = LendSerializer(data=data)
  serializer.is_valid(raise_exception=True)
  serializer.save()

  return serializer.data

class LendTestCase(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.user = create_user()
    self.client.login(username='TestUser', password='TestPassword')
    self.asset = create_asset()

  def test_create_lend_create_object(self):
    self.assertEqual(Lend.objects.all().count(), 0)
    create_lend(self.asset)
    self.assertEqual(Lend.objects.all().count(), 1)

  def test_lend_instance_has_null_values_on_create(self):
    data = create_lend(self.asset)
    self.assertEqual(data['dateReturn'], None)
    self.assertEqual(data['assetReceiver'], None)

  def test_asset_status_become_4_on_being_lent(self):
    # initial
    asset = get_asset(self.asset.id)
    self.assertEqual(asset.status, 1)

    # on creation
    instance = create_lend(self.asset)
    asset = get_asset(instance['asset'])
    self.assertEqual(asset.status, 4)

  def test_asset_status_become_1_on_being_returned(self):
    # initial
    asset = get_asset(self.asset.id)
    instance = create_lend(self.asset)

    # on returning
    instance_id = instance['id']
    response = self.client.get(
      f"/lends/{instance_id}/return",
      content_type="application/json"
    )
    asset = get_asset(instance['asset'])
    self.assertEqual(asset.status, 1)