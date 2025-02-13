from rest_framework import serializers

from apps.user.models import ProfileUser


class UserAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        # print(f' This is user auth\t{AUTH_USER_MODEL}')
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = '__all__'
