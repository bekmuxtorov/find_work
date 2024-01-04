from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import generics, status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from . import serializers
from . import models


# Region List API View
class RegionListAPIView(generics.ListAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


# Region Detail API View
class RegionDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


# District List API View
class DistrictListAPIView(generics.ListAPIView):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer


# District Detail API View
class DistrictDetailAPIView(generics.RetrieveAPIView):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer


# User registration API View


class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = serializers.RegisterSerializer

    @swagger_auto_schema(
        operation_description="Registration user",
        request_body=openapi.Schema(
            required=['phone_number', 'full_name', 'password', 'password2'],
            type=openapi.TYPE_OBJECT,
            properties={
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description="Phone number: as shown +998901234567"),
                'full_name': openapi.Schema(type=openapi.TYPE_STRING, description="Full name"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        ),
        responses={
            200: openapi.Response(
                description="User registration",
                examples={
                    'application/json': {
                        "refresh": "8l6YUaZzRQMq2LSowJXWQUNxWbYzDwXPc",
                        "access": "nlMMPgyNm9GQprEm0aedNP4dWOCL5HUuNeU",
                        "user": {
                            "phone_number": "+998901234567",
                            "full_name": "Palonchi"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                            'error': 'Invalid credentials'
                    }
                }
            )
        }
    )
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)[0].key
            response_data = {
                'token': token,
                'user': serializer.data,
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Login user",
        request_body=openapi.Schema(
            required=['phone_number', 'password'],
            type=openapi.TYPE_OBJECT,
            properties={
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        ),
        responses={
            200: openapi.Response(
                description="User login",
                examples={
                    'application/json': {
                        "id": 1,
                        "role": "adminstrator",
                        "phone_number": "+998901040100",
                        "token": "Token 839ec49fasdfasdfasdfasdfasd",
                        "full_name": "Asadbek Muxtorov"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                        'error': 'Password or phone_number error'
                    }
                }
            )
        }
    )
    def post(self, request):
        phone_number = request.data.get("phone_number")
        password = request.data.get("password")

        user = authenticate(phone_number=phone_number, password=password)
        if user:
            user_data = {
                "id": user.id,
                "role": user.role,
                "phone_number": user.phone_number,
                "token": f"Token {Token.objects.get_or_create(user=user)[0].key}",
                "full_name": user.full_name
            }
            return Response(user_data, status=status.HTTP_200_OK)
        return Response({"errors": "Password or phone_number error"}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPIView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = serializers.ChangePasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)[0].key
            response_data = {
                'token': token,
                "role": user.role,
                'phone_number': user.phone_number,
                "full_name": user.full_name
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
