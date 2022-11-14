from rest_framework import generics, permissions
from inspections.models import Inspection
from inspections.serializers import InspectionSerializer

class InspectionList(generics.ListCreateAPIView):
  queryset = Inspection.objects.all().order_by('id')
  serializer_class = InspectionSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(inspector=self.request.user)

class InspectionDetail(generics.RetrieveAPIView):
  queryset = Inspection.objects.all()
  serializer_class = InspectionSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InspectionClose(generics.RetrieveAPIView):
  queryset = Inspection.objects.all()
  serializer_class = InspectionSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()

      instance.closeInspection()
      return super().retrieve(request, *args, **kwargs)

class InspectionListOngoing(generics.ListAPIView):
  queryset = Inspection.objects.filter(ongoing=True)
  serializer_class = InspectionSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]