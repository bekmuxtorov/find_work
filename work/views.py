from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from . import models
from . import serializers
from .permissions import IsAdminstrator


# Category
class CategoryCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminstrator]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminstrator]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdminstrator]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


# SubCategory
class SubCategoryCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminstrator]
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer


class SubCategoryListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer


class SubCategoryDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer


class SubCategoryUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminstrator]
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer


class SubCategoryDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdminstrator]
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer


# Work
class WorkCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminstrator]
    queryset = models.Work.objects.all()
    serializer_class = serializers.WorkSerializer


class WorkListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Work.objects.all()
    serializer_class = serializers.WorkSerializer


class WorkDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Work.objects.all()
    serializer_class = serializers.WorkSerializer


class WorkUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Work.objects.all()
    serializer_class = serializers.WorkSerializer


class WorkDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdminstrator]
    queryset = models.Work.objects.all()
    serializer_class = serializers.WorkSerializer
