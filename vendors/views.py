from vendors.models import Vendor
from vendors.serializers import VendorSerializer
from rest_framework import generics, permissions


class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all().order_by('id')
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all().order_by('id')
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]
