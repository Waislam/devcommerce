"""
2. CustomUserDetailsSerializer
3. UserSerializer
"""

from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

UserModel = get_user_model()


# ============================== 2. CustomUserDetailsSerializer ===============================
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep


# ============================= 3. UserSerializer ===================================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        user = super().update(instance, validated_data)
        return user

