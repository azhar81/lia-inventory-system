from rest_framework import serializers
from maintenances.models import Maintenance

class MaintenanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Maintenance
    fields = '__all__'
