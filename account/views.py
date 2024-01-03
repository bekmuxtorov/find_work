from rest_framework import generics

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
