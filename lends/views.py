from rest_framework import generics, permissions, status
from rest_framework.response import Response
from lends.models import Lend
from lends.serializers import LendSerializer

class LendList(generics.ListCreateAPIView):
    queryset = Lend.objects.all()
    serializer_class = LendSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LendDetail(generics.RetrieveAPIView):
    queryset = Lend.objects.all().order_by('id')
    serializer_class = LendSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LendReturn(generics.RetrieveAPIView):
    queryset = Lend.objects.all().order_by('id')
    serializer_class = LendSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # update instances on returns (updating status to 1)
    def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()

      # if asset is not being borrowed
      if instance.asset.status == 1:
        return Response(status=status.HTTP_400_BAD_REQUEST)

      instance.returnAsset(request)
      return super().retrieve(request, *args, **kwargs)

class LendOngoingList(generics.ListCreateAPIView):
    queryset = Lend.objects.filter(status=1)
    serializer_class = LendSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
