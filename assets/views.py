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
        branch = self.request.query_params.get('branch')
        floor = self.request.query_params.get('floor')
        room = self.request.query_params.get('room')

        if status != None:
            queryset = queryset.filter(status=status)
        if need_inspection != None:
            max_last_inspection = date.today()-timedelta(days=7)
            if need_inspection.lower() == 'true':
                queryset = queryset.filter(lastInspection__lte=max_last_inspection)
            else:
                queryset = queryset.filter(lastInspection__gte=max_last_inspection)

        if branch != None:
            queryset = queryset = queryset.filter(location__branch = branch)
            if floor:
                queryset = queryset = queryset.filter(location__floor = floor)
                if room:
                    queryset = queryset = queryset.filter(location__room = room)

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
