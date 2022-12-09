from locations.models import Location
from locations.serializers import LocationSerializer
from rest_framework import generics, permissions

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
