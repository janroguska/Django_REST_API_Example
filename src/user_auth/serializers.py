from rest_framework import serializers
from .models import CustomUser

"""Formats the custom user.
"""
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('username', 'name', )