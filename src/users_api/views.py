from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Student
from .serializers import StudentSerializer

class CreateView(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	def perform_create(self, serializer):
		serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

