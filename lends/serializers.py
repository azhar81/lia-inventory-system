from rest_framework import serializers
from lends.models import Lend

class LendSerializer(serializers.ModelSerializer):

  def create(self, validated_data):
    # Change status of asset on creation of lend instance
    instance = super().create(validated_data)
    instance.updateAssetStatus(4)
    return instance

  class Meta:
    model = Lend
    fields = '__all__'
