from django.contrib.auth.models import User
from rest_framework import generics
from users.serializers import UserSerializer
from users import permissions as userpermissions

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [userpermissions.IsAdmin]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [userpermissions.IsAdmin]
