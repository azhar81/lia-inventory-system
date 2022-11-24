from datetime import date, timedelta
from assets.models import Asset, StaticAsset, DynamicAsset
from assets.serializers import AssetSerializer, DynamicAssetSerializer, StaticAssetSerializer
from rest_framework import generics, permissions

class AssetList(generics.ListAPIView):
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Asset.objects.all()
        status = self.request.query_params.get('status')
        need_inspection = self.request.query_params.get('need_inspection')

        if status != None:
            queryset = queryset.filter(status=status)
        if need_inspection != None:
            max_last_inspection = date.today()-timedelta(days=7)
            if need_inspection.lower() == 'true':
                queryset = queryset.filter(lastInspection__lte=max_last_inspection)
            else:
                queryset = queryset.filter(lastInspection__gte=max_last_inspection)

        return queryset

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
