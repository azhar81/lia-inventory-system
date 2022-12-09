from django.contrib.auth.models import User
from .models import Employee
from rest_framework import serializers

class ExtendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['role']

class UserSerializer(serializers.ModelSerializer):
    employee = ExtendedSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'employee']
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        role = validated_data.pop('employee')['role']

        user = User.objects.create(
            username=validated_data.get('username'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        user.set_password(validated_data.get('password'))
        user.save()

        if role == 'Admin':
            user.is_staff = True
            user.save()

        employee = user.employee
        employee.role = role
        employee.save()

        return user

