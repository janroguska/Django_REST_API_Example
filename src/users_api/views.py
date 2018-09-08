from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Users
from .serializers import UserSerializer
from .permissions import IsOwner
from django.contrib.auth.models import User

class CreateView(generics.ListCreateAPIView):
	queryset = Users.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwner)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Users.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwner)

class UserView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer