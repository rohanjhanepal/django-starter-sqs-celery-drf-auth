from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mixins import PublicApiMixin, ApiErrorsMixin
from .utils import (generate_tokens_for_user,
                    )
from .serializers import UserSerializer , InputSerializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.contrib.auth import authenticate
from .models import User

# Create your views here.

class UserView(PublicApiMixin, ApiErrorsMixin, APIView):
    def post(self, request, *args, **kwargs):
        input_serializer = UserSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated_data = input_serializer.validated_data

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            registration_method= "email"
        )
        access_token, refresh_token = generate_tokens_for_user(user)
        response_data = {
            'message': "Success signup",
            'access_token': str(access_token),
            'refresh_token': str(refresh_token)
        }
        return Response(response_data , status=status.HTTP_201_CREATED)
    
#login
class LoginView(PublicApiMixin, ApiErrorsMixin, APIView):
    def post(self, request, *args, **kwargs):
        input_serializer = InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated_data = input_serializer.validated_data
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        if user:
            access_token, refresh_token = generate_tokens_for_user(user)
            response_data = {
                'message': "Success login",
                'access_token': str(access_token),
                'refresh_token': str(refresh_token)
            }
            return Response(response_data , status=status.HTTP_200_OK)
        else:
            return Response({"message":"Invalid credentials"} , status=status.HTTP_401_UNAUTHORIZED)
