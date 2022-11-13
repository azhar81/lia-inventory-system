from assets.models import Asset, StaticAsset, DynamicAsset
from assets.serializers import AssetSerializer, DynamicAssetSerializer, StaticAssetSerializer
from rest_framework import generics, permissions

class AssetList(generics.ListAPIView):
    queryset = Asset.objects.all().order_by('id')
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AssetCreateStatic(generics.CreateAPIView):
    queryset = StaticAsset.objects.all().order_by('id')
    serializer_class = StaticAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AssetCreateDynamic(generics.CreateAPIView):
    queryset = DynamicAsset.objects.all().order_by('id')
    serializer_class = DynamicAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
