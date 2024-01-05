from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)


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
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('name', 'category_name')
    filterset_fields = ('category', 'category_name')


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
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('employer__full_name', 'title',
                     'description', 'region__name', 'district__name')
    filterset_fields = ('region', 'district', 'status',
                        'subcategory', 'employer', 'region__name',
                        'district__name', 'subcategory__name', 'employer__full_name')


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
