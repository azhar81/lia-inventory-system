from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.exceptions import APIException
from django.core.files.uploadedfile import SimpleUploadedFile

from users.tests import create_user_with_username, create_user
from assets.tests import create_asset, get_asset
from .models import Inspection, AssetException
from .serializers import InspectionSerializer

def create_inspection_helper(broken=False):
  img = SimpleUploadedFile(name='test_image.png', content=open("test_image.png", 'rb').read(), content_type='image/png')
  user = create_user_with_username("TestUserInspection")
  asset = create_asset()

  data = {
    'photo': img,
    'broken': broken,
    'description': 'desc',
    'asset': asset.id
  }

  serializer = InspectionSerializer(data=data)
  serializer.is_valid(raise_exception=True)
  instance = serializer.save(inspector=user)

  return instance

def create_inspection(broken, asset, client=None, login=None, user=None):
  img = SimpleUploadedFile(name='test_image.png', content=open("test_image.png", 'rb').read(), content_type='image/png')
  data = {
    'photo': img,
    'broken': broken,
    'description': 'desc',
    'asset': asset.id
  }

  if client:
    client.login(username=login.username, password=login.username)
    response = client.post(
      "/inspections",
      data,
      content_type="application/json"
    )
    return response

  if user:
    serializer = InspectionSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    inspection = serializer.save(inspector=user)

    return inspection

class InspectionTestCase(TestCase):
  def setUp(self):
  #   self.client = APIClient()
    self.asset = create_asset()
    self.user = create_user()
  #   self.client.login(username='TestUser', password='TestPassword')

  def tearDown(self):
    try:
      self.inspection.delete_photo()
    except:
      pass

  def test_create_inspection(self):
    self.assertEqual(Inspection.objects.all().count(), 0)
    self.inspection = create_inspection(False, self.asset, user=self.user)
    self.assertEqual(Inspection.objects.all().count(), 1)

  def test_not_update_asset_status_on_inspection_not_broken(self):
    self.inspection = create_inspection(False, self.asset, user=self.user)

    asset = get_asset(self.inspection.asset.id)
    self.assertEqual(asset.status, 1)

  def test_update_asset_status_on_inspection_broken(self):
    self.inspection = create_inspection(True, self.asset, user=self.user)

    asset = get_asset(self.inspection.asset.id)
    self.assertEqual(asset.status, 2)

  def test_prevent_inspection_for_broken_asset(self):
    self.inspection = create_inspection(True, self.asset, user=self.user)

    self.assertEqual(Inspection.objects.all().count(), 1)
    try:
      create_inspection(True, self.asset, user=self.user)
    except AssetException:
      pass
    self.assertEqual(Inspection.objects.all().count(), 1)
    
  def test_ongoing_true_when_created(self):
    self.inspection = create_inspection(True, self.asset, user=self.user)

    self.assertTrue(self.inspection.ongoing)
    
  def test_ongoing_false_when_closed(self):
    self.inspection = create_inspection(True, self.asset, user=self.user)
    self.inspection.closeInspection()
    self.assertFalse(self.inspection.ongoing)