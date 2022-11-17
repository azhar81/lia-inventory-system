from rest_framework import serializers
from lends.models import Lend

class LendSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lend
    fields = '__all__'
