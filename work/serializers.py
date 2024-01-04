from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from account.serializers import EmployerSerializer

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.SubCategory
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    employer = EmployerSerializer()

    class Meta:
        model = models.Work
        fields = '__all__'
