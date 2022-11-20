from rest_framework import generics, permissions
from rest_framework.response import Response
from maintenances.models import Maintenance
from maintenances.serializers import MaintenanceSerializer

class MaintenanceList(generics.ListCreateAPIView):
  queryset = Maintenance.objects.all().order_by('id')
  serializer_class = MaintenanceSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(staff=self.request.user)

class MaintenanceDetail(generics.RetrieveAPIView):
  queryset = Maintenance.objects.all()
  serializer_class = MaintenanceSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MaintenanceApprove(generics.RetrieveAPIView):
  queryset = Maintenance.objects.all()
  serializer_class = MaintenanceSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()

      instance.approve()
      return super().retrieve(request, *args, **kwargs)

class MaintenanceReject(generics.RetrieveAPIView):
  queryset = Maintenance.objects.all()
  serializer_class = MaintenanceSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()

      instance.reject()
      return super().retrieve(request, *args, **kwargs)

class MaintenanceFinish(generics.RetrieveAPIView):
  queryset = Maintenance.objects.all()
  serializer_class = MaintenanceSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()

      if not instance.maintain:
        return Response(status=400)

      instance.finish()
      return super().retrieve(request, *args, **kwargs)
