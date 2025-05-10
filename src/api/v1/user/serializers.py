from rest_framework import serializers

from apps.user.models import ProfileUser


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('last_name', 'first_name', 'password', 'username', 'phone', 'email')
