from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'registration_method']


class InputSerializer(serializers.Serializer):
        email = serializers.CharField(required=True)
        password = serializers.CharField(required=True)