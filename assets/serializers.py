from rest_framework import serializers
from assets.models import Asset, StaticAsset, DynamicAsset

class AssetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Asset
    exclude = ('polymorphic_ctype', )

class DynamicAssetSerializer(serializers.ModelSerializer):
  class Meta:
    model = DynamicAsset
    exclude = ('polymorphic_ctype', )

class StaticAssetSerializer(serializers.ModelSerializer):
  class Meta:
    model = StaticAsset
    exclude = ('polymorphic_ctype', )
