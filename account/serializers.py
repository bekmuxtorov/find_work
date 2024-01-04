from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from . import models


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = models.District
        fields = '__all__'


# Password alashmashtirish
class ChangePasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, max_length=20)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def create(self, validated_data):
        phone_number = validated_data.get("phone_number")
        old_password = validated_data.get("old_password")
        new_password = validated_data.get("new_password")

        user = models.User.objects.filter(phone_number=phone_number).first()
        if not user:
            raise serializers.ValidationError(
                {
                    "error": "User not found"
                }
            )
        if not user.check_password(old_password):
            raise serializers.ValidationError(
                {
                    "error": "The old password entered with the current password did not match"
                }
            )

        user.set_password(new_password)
        user.save()
        return user


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = models.User
        fields = ("phone_number", "full_name", "password", "password2")

        extra_fields = {
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def create(self, validated_data):
        phone_number = validated_data.get("phone_number")
        full_name = validated_data.get("full_name")
        password = validated_data.get("password")
        password2 = validated_data.get("password2")

        if password == password2:
            WORKER = "worker"
            user = models.User(
                role=WORKER,
                phone_number=phone_number,
                full_name=full_name,
            )
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError(
                {
                    "error": "Both passwords do not match"
                }
            )
