from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.transaction import atomic
from .models import UserProfileModel 
UserModel = get_user_model()


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ('id', 'name', 'surname', 'age')
class UserSerializer(ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password','is_staff', 'is_superuser', 'is_active', 'last_login', 'profile')
        read_only_fields = ('id', 'is_staff', 'is_superuser', 'is_active', 'last_login')
        extra_kwargs = {
            "password":{
                "write_only":True
            }
        }

    def validate(self, attrs):
        print(attrs)
        name = attrs['profile']['name']
        surname = attrs['profile']['surname']
        if name.lower().strip() == surname.lower().strip():
            raise serializers.ValidationError('Name can not be same to surname')
        return attrs

    @atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        profile = UserProfileModel.objects.create(**profile)
        user = UserModel.objects.create_user(**validated_data, profile = profile)
        return user
