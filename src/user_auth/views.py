from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

"""Creates POST request to generate new user.
"""
class UserListView(generics.ListCreateAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer