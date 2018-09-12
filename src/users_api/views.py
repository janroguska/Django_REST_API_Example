from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Student
from .serializers import StudentSerializer

"""Handles POST requests. queryset GETS/POSTS all fields from
Student object.  serializer_class, calls StudentSerializer to format fields.
"""
class CreateView(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	def perform_create(self, serializer):
		serializer.save()

"""Handles GET, PUT, DELETE requests.
"""
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

